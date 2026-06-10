import os
import glob
from datetime import date

import frontmatter
import yaml
import markdown as markdown_lib
from jinja2 import Environment, FileSystemLoader

# ── Constants ──────────────────────────────────────────

LAYER_ORDER = ["pvl", "abo", "bodm", "todm"]

CHAIN_DISPLAY = {
    "revenue-growth": "Revenue Growth",
    "cost-savings": "Cost Savings",
    "risk-reduction": "Risk Reduction",
    "esg-sustainability": "ESG / Sustainability",
    "productivity-workflow": "Productivity",
}

# ── Parser functions (pure, unit-tested) ───────────────

def extract_definition(body: str) -> str:
    for line in body.split("\n"):
        if line.startswith("**Definition:**"):
            return line.replace("**Definition:**", "").strip()
    return ""


def extract_why_it_matters(body: str) -> str:
    lines = body.split("\n")
    in_section = False
    for line in lines:
        if "**Why It Matters" in line:
            in_section = True
            rest = line.split("**Why It Matters")[-1]
            rest = rest.lstrip("*:").strip()
            if rest:
                return rest.lstrip("- ").strip()
            continue
        if in_section and line.strip():
            return line.strip().lstrip("- ").strip()
    return ""


def get_chain_class(metric: dict) -> str:
    chains = metric.get("chains", [])
    if chains:
        return chains[0]
    return "default"


def build_breadcrumb(metric: dict, registry: dict) -> str:
    layer = metric["layer"]
    chains = metric.get("chains", [])
    primary_chain = chains[0] if chains else ""
    chain_label = CHAIN_DISPLAY.get(primary_chain, primary_chain)
    name = metric["name"]

    if layer == "pvl":
        return name
    elif layer == "abo":
        return f"{chain_label} → {name}"
    elif layer == "bodm":
        parent_id = metric.get("parent_abo", "")
        parent = registry.get(parent_id, {})
        parent_name = parent.get("name", parent_id)
        return f"{chain_label} → {parent_name} → {name}"
    elif layer == "todm":
        enables = metric.get("enables_bodm", [])
        if enables:
            parent = registry.get(enables[0], {})
            parent_name = parent.get("name", enables[0])
            return f"{chain_label} → {parent_name} → {name}"
        return f"{chain_label} → {name}"
    return name


# ── Loader ─────────────────────────────────────────────

def load_metrics(metrics_root: str) -> dict:
    registry = {}
    for layer in LAYER_ORDER:
        pattern = os.path.join(metrics_root, layer, "*.md")
        for path in sorted(glob.glob(pattern)):
            post = frontmatter.load(path)
            meta = dict(post.metadata)
            meta["body"] = post.content
            meta["layer"] = layer
            meta["definition"] = extract_definition(post.content)
            meta["why_it_matters"] = extract_why_it_matters(post.content)
            registry[meta["id"]] = meta
    return registry


# ── Renderer ───────────────────────────────────────────

def render_cards(registry: dict, env: Environment) -> str:
    pages = []

    # Orientation cards
    with open("content/orientation-cards.yaml") as f:
        orientation_data = yaml.safe_load(f)
    tmpl = env.get_template("card-orientation.html")
    for card in orientation_data["cards"]:
        pages.append(tmpl.render(card=card))

    # Metric cards — sorted by layer then name
    metric_tmpl = env.get_template("card-metric.html")
    for layer in LAYER_ORDER:
        layer_metrics = [m for m in registry.values() if m["layer"] == layer]
        layer_metrics.sort(key=lambda m: m["name"])
        for metric in layer_metrics:
            metric["breadcrumb"] = build_breadcrumb(metric, registry)
            metric["chain_class"] = get_chain_class(metric)
            pages.append(metric_tmpl.render(metric=metric))

    # Facilitator card
    with open("content/facilitator-card.yaml") as f:
        facilitator_data = yaml.safe_load(f)
    fac_tmpl = env.get_template("card-facilitator.html")
    pages.append(fac_tmpl.render(card=facilitator_data))

    return "\n".join(pages)


def render_script(env: Environment) -> str:
    with open("content/facilitation-script.md") as f:
        script_md = f.read()
    script_html = markdown_lib.markdown(
        script_md,
        extensions=["tables", "fenced_code"]
    )
    tmpl = env.get_template("facilitation-script.html")
    return tmpl.render(content=script_html)


# ── Main ───────────────────────────────────────────────

def main():
    import weasyprint  # lazy import — requires system gobject/pango libraries

    today = date.today().isoformat()
    os.makedirs("output", exist_ok=True)

    metrics_root = os.path.join("..", "framework", "metrics")
    registry = load_metrics(metrics_root)
    print(f"Loaded {len(registry)} metrics")

    env = Environment(loader=FileSystemLoader("templates"), comment_start_string="{#", comment_end_string="#}")

    # Cards PDF
    cards_html = render_cards(registry, env)
    weasyprint.HTML(string=cards_html, base_url=os.path.abspath("templates") + "/").write_pdf(
        f"output/flashcards-{today}.pdf"
    )
    print(f"✓ output/flashcards-{today}.pdf")

    # Script PDF
    script_html = render_script(env)
    weasyprint.HTML(string=script_html, base_url=os.path.abspath("templates") + "/").write_pdf(
        f"output/facilitation-script-{today}.pdf"
    )
    print(f"✓ output/facilitation-script-{today}.pdf")


if __name__ == "__main__":
    main()

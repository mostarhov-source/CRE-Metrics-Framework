import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from generate import (
    extract_definition,
    extract_why_it_matters,
    build_breadcrumb,
    get_chain_class,
    CHAIN_DISPLAY,
)


# ── extract_definition ─────────────────────────────────

def test_extract_definition_single_line():
    body = "**Definition:** Income after operating expenses, before financing and taxes."
    assert extract_definition(body) == "Income after operating expenses, before financing and taxes."

def test_extract_definition_missing_returns_empty():
    body = "# Some Metric\n\nNo definition here."
    assert extract_definition(body) == ""

def test_extract_definition_ignores_other_bold_lines():
    body = "**Category:** Financial\n**Definition:** The real one.\n**Formula:** x + y"
    assert extract_definition(body) == "The real one."


# ── extract_why_it_matters ─────────────────────────────

def test_extract_why_single_line():
    body = "**Why It Matters:** Core driver of valuations and investor returns."
    assert extract_why_it_matters(body) == "Core driver of valuations and investor returns."

def test_extract_why_bullet_list():
    body = "**Why It Matters:**\n- Tenant renewals stabilise cash flow.\n- Strong satisfaction drives reputation."
    assert extract_why_it_matters(body) == "Tenant renewals stabilise cash flow."

def test_extract_why_missing_returns_empty():
    body = "**Definition:** Something.\n\nNo why here."
    assert extract_why_it_matters(body) == ""


# ── build_breadcrumb ───────────────────────────────────

MOCK_REGISTRY = {
    "revenue-growth": {
        "id": "revenue-growth",
        "name": "Revenue Growth",
        "layer": "pvl",
        "chains": ["revenue-growth"],
    },
    "optimised-portfolio-returns": {
        "id": "optimised-portfolio-returns",
        "name": "Optimised Portfolio Returns",
        "layer": "abo",
        "chains": ["revenue-growth"],
        "pvl": ["revenue-growth"],
    },
    "noi": {
        "id": "noi",
        "name": "Net Operating Income (NOI)",
        "layer": "bodm",
        "chains": ["revenue-growth", "cost-savings"],
        "parent_abo": "optimised-portfolio-returns",
    },
    "proptech-investment-roi": {
        "id": "proptech-investment-roi",
        "name": "PropTech Investment ROI",
        "layer": "todm",
        "chains": ["revenue-growth", "cost-savings"],
        "enables_bodm": ["noi"],
    },
}

def test_breadcrumb_pvl():
    metric = MOCK_REGISTRY["revenue-growth"]
    assert build_breadcrumb(metric, MOCK_REGISTRY) == "Revenue Growth"

def test_breadcrumb_abo():
    metric = MOCK_REGISTRY["optimised-portfolio-returns"]
    assert build_breadcrumb(metric, MOCK_REGISTRY) == "Revenue Growth → Optimised Portfolio Returns"

def test_breadcrumb_bodm():
    metric = MOCK_REGISTRY["noi"]
    result = build_breadcrumb(metric, MOCK_REGISTRY)
    assert result == "Revenue Growth → Optimised Portfolio Returns → Net Operating Income (NOI)"

def test_breadcrumb_todm_with_enables_bodm():
    metric = MOCK_REGISTRY["proptech-investment-roi"]
    result = build_breadcrumb(metric, MOCK_REGISTRY)
    assert result == "Revenue Growth → Net Operating Income (NOI) → PropTech Investment ROI"


# ── get_chain_class ────────────────────────────────────

def test_chain_class_known_chain():
    metric = {"chains": ["revenue-growth"]}
    assert get_chain_class(metric) == "revenue-growth"

def test_chain_class_multi_chain_returns_first():
    metric = {"chains": ["cost-savings", "revenue-growth"]}
    assert get_chain_class(metric) == "cost-savings"

def test_chain_class_no_chains_returns_default():
    metric = {"chains": []}
    assert get_chain_class(metric) == "default"

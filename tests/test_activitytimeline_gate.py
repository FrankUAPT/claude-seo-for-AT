"""Tests for scripts/activitytimeline_gate.py, the ActivityTimeline gate and fact lint.

Every fact rule has one text that must raise it and one near miss that must
not: the confirmed figure, the correct spelling or the look-alike a careless
pattern would flag. Page-level gates run on inline HTML; URL mode runs with a
fake fetcher. No test touches the network.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import activitytimeline_gate as gate  # noqa: E402

PROFILE = gate.load_profile()
TODAY = dt.date(2026, 11, 19)
ORIGIN = "https://activitytimeline.com"

# rule id -> (text that must raise it, near miss that must not)
RULE_CASES = {
    "f15-old-team-count": ("Trusted by 5,000+ teams worldwide.", "Trusted by 10,000+ teams worldwide."),
    "f15-teams-not-customers": ("Join 10,000+ customers on Jira.", "Join 10,000+ teams on Jira."),
    "f10-server": ("Works with Jira Server and Cloud.", "Works with Jira Cloud and Data Center."),
    "f06-free-small-teams": ("It is free for up to 10 users.", "$10 a month for up to 10 users."),
    "f05-per-user-misquote": ("Advanced costs $15 per user per month.", "$10 a month, flat, for up to 10 users."),
    "f05-old-500-user-value": ("500 users: $8,250 a year.", "500 users: $8,450 a year."),
    "f07-old-advanced-quote": ("Advanced is $1,245 a month at 500 users.", "Advanced is $21,950 a year for 1,000 users."),
    "f14-install-count": ("Over 3,546 installs on the Marketplace.", "Installed from the Atlassian Marketplace."),
    "f13-review-count": ("4.7 from 122 reviews.", "4.7 from 125 reviews."),
    "f13-rating": ("Rated 4.5 out of 5 by users.", "Rated 4.7 out of 5 by users."),
    "f12-demo-length": ("Book a 30-minute demo.", "Book a 25-minute demo."),
    "f19-hosting": ("Data is hosted in Frankfurt.", "Data is hosted in the EU."),
    "f20-outlook-two-way": ("Outlook calendars sync two-way.", "Google and Outlook calendars are supported."),
    "f22-unconfirmed-integrations": ("Integrates with ScriptRunner.", "Integrates with Jira Plans and Tempo worklogs."),
    "f24-mcp": ("Use our MCP server with Claude.", "Use our REST API."),
    "f02-brand-spelling": ("Activity Timeline helps planners.", "ActivityTimeline helps planners on activitytimeline.com."),
    "f02-jira-caps": ("Plan work in JIRA.", "Plan work in Jira."),
    "f03-finances-data-center": ("Finances is available on Data Center too.",
                                 "Finances is part of the Advanced Edition on Cloud. Data Center has Planner."),
    "f09-data-center-new-customers": ("New customers can buy Data Center licences.",
                                      "Existing Data Center customers keep their pricing."),
    "f17-cloud-fortified": ("ActivityTimeline is Cloud Fortified.", "ActivityTimeline is Atlassian Enterprise Certified."),
    "f25-tempo-like-for-like": ("Pay 68% less than Tempo.",
                                "Pay 68% less than Tempo, like for like (Standard vs Timesheets + Capacity Planner)."),
    "f25-tempo-price-dated": ("Tempo Timesheets costs $17,280 a year.",
                              "Tempo Timesheets costs $17,280 a year (Marketplace list price, 1 Oct 2026)."),
}


def _ids(findings):
    return {f["id"] for f in findings}


def test_every_rule_is_well_formed_and_cited():
    seen = set()
    for rule in PROFILE["fact_rules"]:
        assert rule["id"] not in seen, rule["id"]
        seen.add(rule["id"])
        assert re.fullmatch(r"f\d\d", rule["fact"]), rule["id"]
        assert rule["kind"] in {"forbid", "number", "requires", "sentence"}, rule["id"]
        assert rule["severity"] in gate.SEVERITY_ORDER, rule["id"]
        assert rule["gate"] in {"G3", None}, rule["id"]
        assert rule["message"] and rule["source"], rule["id"]
        if rule["kind"] == "number":
            assert rule["expected_key"] in PROFILE["current"], rule["id"]
    dt.date.fromisoformat(PROFILE["facts_as_of"])


def test_every_rule_has_a_case():
    assert set(RULE_CASES) == {r["id"] for r in PROFILE["fact_rules"]}


@pytest.mark.parametrize("rule_id", sorted(RULE_CASES))
def test_rule_fires_on_positive_and_not_on_near_miss(rule_id):
    positive, near_miss = RULE_CASES[rule_id]
    assert rule_id in _ids(gate.lint_facts({"body": positive}, PROFILE, "en")), positive
    assert rule_id not in _ids(gate.lint_facts({"body": near_miss}, PROFILE, "en")), near_miss


def test_english_only_rules_skip_other_locales():
    findings = gate.lint_facts({"body": "Pague 68% menos que Tempo."}, PROFILE, "es")
    assert "f25-tempo-like-for-like" not in _ids(findings)


def test_localized_team_count_is_caught():
    findings = gate.lint_facts({"body": "Mais de 5.000 equipes confiam."}, PROFILE, "pt")
    assert "f15-old-team-count" in _ids(findings)


def test_fact_lint_reads_title_description_and_jsonld():
    findings = gate.lint_facts({"title": "Activity Timeline pricing", "description": "From $8,250 a year",
                                "jsonld": ['{"reviewCount": "122 reviews"}'], "body": ""}, PROFILE, "en")
    where = {f["id"]: f["evidence"].split(":")[0] for f in findings}
    assert where["f02-brand-spelling"] == "title"
    assert where["f05-old-500-user-value"] == "meta description"
    assert where["f13-review-count"] == "JSON-LD"


def _page(path="/pricing", *, canonicals=None, robots_meta=None, lang="en", title="Pricing | ActivityTimeline",
          body="ActivityTimeline pricing for Jira Cloud.", hreflang=("en", "es", "fr", "pt")):
    url = ORIGIN + path
    canonicals = [url] if canonicals is None else canonicals
    links = "".join(f'<link rel="canonical" href="{c}">' for c in canonicals)
    links += "".join(f'<link rel="alternate" hreflang="{h}" href="{ORIGIN}/{h}{path}">' for h in hreflang)
    robots = f'<meta content="{robots_meta}" name="robots">' if robots_meta else ""
    html = (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{title}</title>'
            f'<meta content="Plan capacity in Jira with ActivityTimeline." name="description">{robots}{links}'
            f'</head><body><h1>Pricing</h1><p>{body}</p><footer>Trusted by 10,000+ teams</footer></body></html>')
    return url, html


def _check(path="/pricing", site_files=None, commercial=True, **kw):
    url, html = _page(path, **kw)
    return gate.check_html(html, url, PROFILE, TODAY, site_files=site_files or {}, commercial=commercial)


def test_clean_commercial_page_passes_every_gate():
    result = _check()
    assert result["gates"]["G1"] == "pass"
    assert result["gates"]["G3"] == "pass"
    assert result["gates"]["G5"] == "pass"
    assert result["gates"]["G2"] == "not_checked"


def test_two_canonicals_fail_g1_and_list_both():
    url = ORIGIN + "/capacity-planning"
    result = _check("/capacity-planning", canonicals=[url, ORIGIN + "/how-to-do-capacity-planning-in-jira"])
    finding = next(f for f in result["findings"] if f["id"] == "canonical-multiple")
    assert finding["severity"] == "Critical"
    assert "how-to-do-capacity-planning-in-jira" in finding["evidence"]
    assert result["gates"]["G1"] == "fail"


def test_canonical_elsewhere_and_missing_fail_g1():
    assert "canonical-not-self" in _ids(_check(canonicals=[ORIGIN + "/"])["findings"])
    assert "canonical-missing" in _ids(_check(canonicals=[])["findings"])


def test_noindex_meta_with_content_first_fails_g1():
    result = _check(robots_meta="noindex, follow")
    assert "noindex" in _ids(result["findings"])
    assert result["gates"]["G1"] == "fail"


def test_noindex_header_fails_g1():
    url, html = _page()
    result = gate.check_html(html, url, PROFILE, TODAY, headers={"X-Robots-Tag": "noindex"})
    assert "noindex-header" in _ids(result["findings"])


def test_g5_flags_a_blocked_ai_crawler_only():
    blocked = {"robots_txt": {"content": "User-agent: OAI-SearchBot\nDisallow: /\n\nUser-agent: *\nAllow: /\n"}}
    finding = next(f for f in _check(site_files=blocked)["findings"] if f["id"] == "crawler-blocked")
    assert finding["evidence"] == "OAI-SearchBot"
    allowed = {"robots_txt": {"content": "User-agent: GPTBot\nDisallow: /\n\nUser-agent: *\nAllow: /\n"}}
    assert _check(site_files=allowed)["gates"]["G5"] == "pass"


@pytest.mark.parametrize("title,expected", [
    ("Jira Board Guide (2027) | ActivityTimeline", "title-future-year"),
    ("Time Tracking Plugins 2025 | ActivityTimeline", "title-past-year"),
])
def test_title_years(title, expected):
    assert expected in _ids(_check(title=title)["findings"])


def test_current_year_title_is_fine():
    ids = _ids(_check(title="Jira Board Guide (2026) | ActivityTimeline")["findings"])
    assert not ids & {"title-future-year", "title-past-year"}


def test_title_over_webflow_field_limit():
    assert "title-over-field-limit" in _ids(_check(title="x" * 81)["findings"])
    assert "title-over-field-limit" not in _ids(_check(title="x" * 80)["findings"])


def test_lang_mismatch_on_locale_path():
    assert "lang-mismatch" in _ids(_check("/es/pricing", lang="en")["findings"])
    assert "lang-mismatch" not in _ids(_check("/es/pricing", lang="es")["findings"])


def test_hreflang_gap_is_medium_on_commercial_and_info_elsewhere():
    commercial = next(f for f in _check(hreflang=("en", "es"))["findings"] if f["id"] == "hreflang-locales-missing")
    assert commercial["severity"] == "Medium" and "fr" in commercial["evidence"]
    post = next(f for f in _check("/blog/jira-board", hreflang=("en", "es"), commercial=False)["findings"]
                if f["id"] == "hreflang-locales-missing")
    assert post["severity"] == "Info"


def test_sitemap_and_llms_membership_for_commercial_pages():
    files = {"sitemap": {"content": f"<urlset><url><loc>{ORIGIN}/features</loc></url></urlset>"},
             "llms_txt": {"content": f"- [Pricing]({ORIGIN}/pricing)\n"}}
    ids = _ids(_check(site_files=files)["findings"])
    assert "not-in-sitemap" in ids and "not-in-llms-txt" not in ids


def test_is_commercial_and_locale_of():
    assert gate.is_commercial(ORIGIN + "/fr/pricing", PROFILE)
    assert gate.is_commercial(ORIGIN + "/es", PROFILE)
    assert not gate.is_commercial(ORIGIN + "/blog/jira-board", PROFILE)
    assert gate.locale_of(ORIGIN + "/pt/blog/x", PROFILE) == "pt"
    assert gate.locale_of(ORIGIN + "/pricing", PROFILE) == "en"


def test_check_url_with_fake_fetch_reports_redirect():
    url, html = _page("/how-it-works")

    def fake_fetch(requested, timeout=30):
        return {"url": url, "status_code": 200, "content": html, "headers": {}, "redirect_chain": [requested]}

    result = gate.check_url(ORIGIN + "/how-it-works/", PROFILE, TODAY, fake_fetch, {}, True)
    assert "redirected" in _ids(result["findings"])
    assert result["requested_url"].endswith("/how-it-works/")


def test_check_url_reports_fetch_errors_without_raising():
    result = gate.check_url(ORIGIN + "/", PROFILE, TODAY, lambda u, timeout=30: {"error": "blocked"}, {}, True)
    assert result["error"] == "blocked"


def test_facts_drift_against_memory(tmp_path):
    (tmp_path / "facts.md").write_text("| Date | Fact |\n|---|---|\n| 2026-12-01 | f07 changed |\n", encoding="utf-8")
    drift = gate.facts_drift(str(tmp_path), PROFILE)
    assert drift["stale"] is True and drift["memory_facts_newest"] == "2026-12-01"
    assert gate.facts_drift(None, PROFILE) is None
    assert "error" in gate.facts_drift(str(tmp_path / "missing"), PROFILE)


def _run(*args):
    proc = subprocess.run([sys.executable, str(SCRIPTS / "activitytimeline_gate.py"), *args],
                          capture_output=True, text=True, timeout=60)
    return proc.returncode, json.loads(proc.stdout)


def test_cli_text_draft(tmp_path):
    draft = tmp_path / "draft.md"
    draft.write_text("Trusted by 5,000 teams. Activity Timeline for Jira.", encoding="utf-8")
    code, out = _run("--file", str(draft), "--today", "2026-11-19")
    assert code == 0
    page = out["pages"][0]
    assert page["gates"]["G3"] == "fail"
    assert {"f15-old-team-count", "f02-brand-spelling"} <= _ids(page["findings"])
    clean = tmp_path / "clean.md"
    clean.write_text("Trusted by 10,000+ teams. ActivityTimeline for Jira.", encoding="utf-8")
    assert _run("--file", str(clean))[1]["pages"][0]["gates"]["G3"] == "pass"


def test_cli_html_file(tmp_path):
    url, html = _page("/pricing", canonicals=[ORIGIN + "/pricing", ORIGIN + "/"])
    saved = tmp_path / "pricing.html"
    saved.write_text(html, encoding="utf-8")
    code, out = _run("--file", str(saved), "--base-url", url, "--today", "2026-11-19")
    assert code == 0 and out["pages"][0]["gates"]["G1"] == "fail"
    assert {item["id"] for item in out["not_checked"]} >= {"G2", "G4"}


@pytest.mark.parametrize("args", [
    ("--file", "x.md", "--today", "19-11-2026"),
    ("--url", "https://activitytimeline.com/", "--base-url", "https://activitytimeline.com/"),
    ("--url", "https://activitytimeline.com/", "--locales"),
])
def test_cli_bad_arguments_exit_2(args):
    assert _run(*args)[0] == 2


def test_cli_missing_file_exits_1(tmp_path):
    assert _run("--file", str(tmp_path / "nope.md"))[0] == 1

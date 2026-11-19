"""Tests for scripts/lab_memory_status.py, the SEO Lab memory briefing.

A small memory checkout is written to a temporary directory in the same
shapes the real repository uses (changelog entries with Re-check lines, the
decisions tables, the initiatives table, the charter KPI table and the weekly
scorecard), and the briefing is checked against it. No network.
"""

from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import lab_memory_status as status  # noqa: E402

TODAY = dt.date(2026, 11, 19)

CHARTER = """# Charter

| KPI | Baseline | 12-month target |
| --- | --- | --- |
| Commercial pages indexed in Google | 3 of 12 (5 Nov 2026) | 12 of 12 within 4 weeks |
| Brand clicks, 28 days | 84 | 140-160 |
| Mention rate on cost and budget prompts | 7.9% | 40%+ |
"""

CHANGELOG = """# Change log

## 2026 Q4

### 2026-11-09 · Drafts (not live) · Title-tag years
- **Owner:** PM; Ostap publishes. **Not published.** Record the publish date here; re-check 4 weeks after.

### 2026-11-06 · Site · STB-3 shipped: one fact sheet
- **Why:** shipped 6 Nov after the 5 Nov audit.
- **Re-check:** 4 Dec 2026 and 1 Jan 2027: brand clicks, AI mention rate.

### 2026-10-30 · Site · /tempo-alternative went live
- **Result:** open. Change-set is idea 6 in the 9 Nov report; measure at 4 and 8 weeks (27 Nov, 25 Dec).
"""

DECISIONS = """# Decisions

## Decided

| Date | Decision | Ticket | File |
|---|---|---|---|
| 2026-11-09 | D6: freeze the alternatives posts; review 19 Nov and in February | STB-12 | x.md |
| 2026-11-06 | Blog post layout: option A | - | y.md |

## Deferred by Ostap (he will come back to these)

| Since | What | Revisit | Ticket | File |
|---|---|---|---|---|
| 2026-11-09 | Website structure: postponed | when Ostap brings it | - | a.md |
| 2026-11-05 | Portuguese list: two posts stay live | about 6 Nov 2026 (overdue) | STB-5 | b.md |

## Open (waiting on Ostap)

| Since | Question | Ticket | Stage | File |
|---|---|---|---|---|
| 2026-11-05 | D7 Who owns Bing Webmaster Tools? | STB-13 | stage-needs-ostap | c.md |
| 2026-11-10 | Titles list: second canonical on purpose? | not yet ticketed | - | d.md |

## Template for a decision file
"""

INITIATIVES = """# Initiatives

| Initiative | Ticket | Status (9 Nov 2026) | KPI |
|---|---|---|---|
| `fact-sheet.md` | STB-3 | Shipped 6 Nov; measuring; re-check 4 Dec | Brand clicks |
| `cost-hub.md` | WO6 | Not started (Dec-Feb) | Cost prompts |
"""

SCORECARD = """week_of,brand_clicks_28d,commercial_pages_indexed_google,notes
2026-10-26,94,,a
2026-11-02,97,3 (5 Nov),b
2026-11-09,84,,c
"""


@pytest.fixture()
def memory(tmp_path):
    files = {
        "charter.md": CHARTER,
        "changes/CHANGELOG.md": CHANGELOG,
        "decisions/README.md": DECISIONS,
        "initiatives/README.md": INITIATIVES,
        "scorecards/weekly.csv": SCORECARD,
        "trial-drought/weekly/2026-11-09.md": "# report\n",
    }
    for rel, text in files.items():
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return tmp_path


def _whats(items):
    return " || ".join(item["what"] for item in items)


def test_dates_without_a_year_take_the_anchor_year_or_the_next():
    assert status.dates_in("re-check 4 Dec", dt.date(2026, 11, 6)) == [dt.date(2026, 12, 4)]
    assert status.dates_in("review 10 Jan", dt.date(2026, 12, 20)) == [dt.date(2027, 1, 10)]
    assert status.dates_in("on 2026-11-05 and 31 Feb", TODAY) == [dt.date(2026, 11, 5)]


def test_action_dates_ignore_dates_before_the_action_word():
    assert status.action_dates("Shipped 6 Nov; measuring; re-check 4 Dec", dt.date(2026, 11, 1)) == [
        dt.date(2026, 12, 4)]
    assert status.action_dates("Shipped 6 Nov", dt.date(2026, 11, 1)) == []


def test_briefing_buckets(memory):
    out = status.build(str(memory), TODAY, 14)
    overdue, due, later = _whats(out["overdue"]), _whats(out["due_soon"]), _whats(out["later"])
    assert "Portuguese list" in overdue
    assert "D6" in due and "2026-11-19" in [i["date"] for i in out["due_soon"]]
    assert "tempo-alternative" in due
    assert "STB-3" in later and "fact-sheet.md" in later
    assert not [i for i in out["overdue"] if i["from"] == "initiatives/README.md"]
    assert "Blog post layout" not in overdue + due + later


def test_briefing_staged_and_open_decisions(memory):
    out = status.build(str(memory), TODAY, 14)
    assert [s["entry"].split(" · ")[-1] for s in out["staged_unpublished"]] == ["Title-tag years"]
    assert out["staged_unpublished"][0]["age_days"] == 10
    questions = {o["question"]: o for o in out["open_decisions"]}
    assert questions["D7 Who owns Bing Webmaster Tools?"]["age_days"] == 14
    assert "Deferred: Website structure: postponed" in questions
    assert out["open_decisions"][0]["age_days"] >= out["open_decisions"][-1]["age_days"]


def test_briefing_freshness_and_kpis(memory):
    out = status.build(str(memory), TODAY, 14)
    fresh = out["freshness"]
    assert fresh["changelog_newest"] == "2026-11-09"
    assert fresh["weekly_report_newest"] == "2026-11-09"
    assert fresh["expected_week_of"] == "2026-11-16"
    assert fresh["weekly_row_missing"] is True
    kpis = {k["kpi"]: k for k in out["kpis"]}
    brand = kpis["Brand clicks, 28 days"]
    assert brand["latest"] == {"week_of": "2026-11-09", "value": "84"}
    assert brand["previous"] == {"week_of": "2026-11-02", "value": "97"}
    indexed = kpis["Commercial pages indexed in Google"]
    assert indexed["latest"] == {"week_of": "2026-11-02", "value": "3 (5 Nov)"}
    assert kpis["Mention rate on cost and budget prompts"]["latest"] is None


def test_missing_files_become_warnings(tmp_path):
    (tmp_path / "charter.md").write_text(CHARTER, encoding="utf-8")
    out = status.build(str(tmp_path), TODAY, 14)
    assert "changes/CHANGELOG.md not found" in out["warnings"]
    assert out["overdue"] == [] and out["kpis"]


def _run(*args):
    proc = subprocess.run([sys.executable, str(SCRIPTS / "lab_memory_status.py"), *args],
                          capture_output=True, text=True, timeout=60)
    return proc.returncode, json.loads(proc.stdout)


def test_cli(memory, tmp_path):
    code, out = _run("--memory", str(memory), "--today", "2026-11-19", "--horizon", "7")
    assert code == 0 and out["horizon_days"] == 7
    assert _run("--memory", str(tmp_path / "none"))[0] == 1
    assert _run("--memory", str(memory), "--today", "tomorrow")[0] == 2
    assert _run("--memory", str(memory), "--horizon", "-1")[0] == 2

#!/usr/bin/env python3
# Build site/coded-alshaya-day-3-lab.html by cloning the Day 2 lab shell.
import json, re, pathlib

SITE = pathlib.Path(__file__).resolve().parent.parent / 'site'
src = (SITE / 'coded-alshaya-day-2-lab.html').read_text()

# ---------- scenario widget ----------
def sc(title, dept, situation, initiative, data, watch, wbfile):
    return (
        f'<details class="reveal"><summary>{title} · <span style="color:var(--ink-dim)">{dept}</span></summary>'
        f'<div style="padding:4px 2px 8px">'
        f'<p style="font-size:14px;line-height:1.6;margin:10px 0"><b>The situation.</b> {situation}</p>'
        f'<p style="font-size:14px;line-height:1.6;margin:10px 0"><b>Your initiative.</b> {initiative}</p>'
        f'<p style="font-size:14px;line-height:1.6;margin:10px 0"><b>Your data.</b> {data}</p>'
        f'<p style="font-size:14px;line-height:1.6;margin:10px 0;color:var(--gold-lt)"><b>Watch out.</b> {watch}</p>'
        f'<a class="dl" href="{wbfile}" download style="margin:6px 0 4px"><span class="ic">\u2b07</span>'
        f'<span>Download your workbook<small>{wbfile}</small></span></a>'
        f'</div></details>'
    )

scenarios = [
 sc('S1 · The Contractor Turnaround', 'Facilities',
    'The portfolio has 40 open maintenance tickets, 11 of them older than 30 days, against a 5-day service standard. Complaints have tripled in a quarter — and one contractor has quietly stopped closing tickets altogether.',
    'A contractor performance regime: response-time standards by priority, a weekly scorecard, and a clear escalation path — so the backlog cannot build up unseen again.',
    'Your workbook <b>alshaya-capstone-s1.xlsx</b> — the full 68-ticket maintenance log, per-ticket first-response times against SLA, the contracted service levels, and thirteen weeks of site attendance.',
    'Your briefing must name the stalled contractor from the log itself — worked out from the data, not from memory.', 'alshaya-capstone-s1.xlsx'),
 sc('S2 · The Cost Control Programme', 'Finance',
    'Q3 closed with maintenance KWD 7,300 over budget and utilities KWD 2,100 over, while marketing sat KWD 2,600 under. At the same time occupancy at [PROPERTY A] is sliding — income falling while costs rise.',
    'A Q4 cost-control programme: three concrete measures, each tied to a budget line, plus a monthly variance review so overruns surface in weeks, not quarters.',
    'Your workbook <b>alshaya-capstone-s2.xlsx</b> — the Q3 budget against actuals, twelve months of monthly cost by category, and six months of occupancy and income.',
    'Every saving you promise must trace to a line in your workbook. A saving with no line behind it is a wish, not a measure.', 'alshaya-capstone-s2.xlsx'),
 sc('S3 · The Upper-Floor Push', 'Leasing',
    'Retail occupancy at [PROPERTY A] has slid from 83.3% to 75% in six months. Twelve units sit vacant — five empty for nine months or more, concentrated on the upper floor. A new F&amp;B signing should lift footfall next quarter.',
    'An upper-floor leasing campaign: targeted incentives funded by the marketing underspend, a occupancy target, and a 90-day plan that rides the F&amp;B opening.',
    'Your workbook <b>alshaya-capstone-s3.xlsx</b> — six months of occupancy and income, the unit-by-unit schedule for all 48 units with use and lease expiry, and six months of leasing enquiries with outcomes.',
    'Occupancy numbers travel fast. Count the units yourself before any percentage reaches your briefing.', 'alshaya-capstone-s3.xlsx'),
 sc('S4 · The Hiring Sprint', 'HR',
    '[PROPERTY C] — a 14-unit tower — is approaching completion, and the facilities team that will run it does not exist yet. Twelve candidates across four roles are sitting in a sheet, unscreened.',
    'A 60-day structured hiring sprint: clear criteria per role, an AI-assisted screening workflow, and an interview plan — staffed and ready before the building opens.',
    'Your workbook <b>alshaya-capstone-s4.xlsx</b> — the agreed role requirements, the 40-candidate register, the agency’s long-list of the same pool, and eight weeks of application volume by source.',
    'AI screens, humans decide. Your package must say — explicitly — where the human decision sits in the workflow.', 'alshaya-capstone-s4.xlsx'),
 sc('S5 · The Engagement Turnaround', 'HR · People',
    'The staff survey is back: Maintenance and HR trail Leasing and Finance, and Growth Opportunities is the weakest score across every department. Twelve responses — small enough that every voice counts, small enough to overread.',
    'A 90-day engagement plan: two actions aimed at the weakest scores, an owner for each, and a follow-up pulse survey to prove movement.',
    'Your workbook <b>alshaya-capstone-s5.xlsx</b> — this year’s 12 scored responses with their free-text comments, last year’s survey for the trend, twelve months of exit interviews, and training hours by department.',
    'Twelve responses is a small sample. Your briefing should say what the data supports — and admit what it cannot.', 'alshaya-capstone-s5.xlsx'),
 sc('S6 · The Tenant Confidence Campaign', 'Communications',
    'Tenant complaints tripled from 9 to 23 in a month. The north lift keeps failing, three tenants have escalated in writing, and one is asking about a rent concession. Today, tenants hear nothing until something breaks.',
    'A proactive tenant communication programme: a monthly operations note, planned-works notices, a published service standard, and a complaint-response SLA.',
    'Your workbook <b>alshaya-capstone-s6.xlsx</b> — six months of tenant complaints (60 in all, ticket-linked from April), plus the full maintenance log for verifying every linked ticket.',
    'Honest without being alarming. Never promise a date or a fix the data cannot support — that is how confidence was lost in the first place.', 'alshaya-capstone-s6.xlsx'),
 sc('S7 · The Launch Readiness Plan', 'Operations',
    '[PROPERTY C] is a 14-unit tower in fit-out trouble: joinery arrived late, the contractor needs six weeks from delivery, the tenant is paying storage while they wait, and the Board wants a written position on the handover date.',
    'A launch-readiness plan: a realistic handover date you can defend, the top five risks with owners, and a week-by-week countdown to opening.',
    'Your workbook <b>alshaya-capstone-s7.xlsx</b> — the confirmed project facts, the contractor’s milestone schedule, the 28-item snag list, the fit-out cost tracker against contingency, and the portfolio occupancy context.',
    'Dates need the same checks as money. Run the arithmetic across every milestone yourself before you commit to a date.', 'alshaya-capstone-s7.xlsx'),
]
scenario_widget = ('<div class="step-card"><div class="sc-k">Your seven scenarios — one per team</div>'
                   + ''.join(scenarios)
                   + '<p style="font-size:13.5px;line-height:1.6;margin:14px 2px 2px;color:var(--gold-lt)">'
                     '<b>Every workbook contains exactly one planted inconsistency</b> — between its sheets, or '
                     'against its own totals. Your verifier\u2019s first job is to find it before it '
                     'reaches your briefing. Flag it in your pitch; do not silently pick a side.</p></div>')


TASKS = [
 {"app": "Team · Phase 0",
  "title": "T1 · Phase 0 — Choose your scenario &amp; plan",
  "scenario": "Ten minutes, no tools open. Find your team’s scenario below, read it twice, download your team\u2019s workbook, and agree who does what. Teams of two: for every deliverable one of you builds, the other verifies. (~10 min)",
  "widget": scenario_widget,
  "steps": [
    "Find your team’s scenario below (your instructor assigns S1–S7) and read it together.",
    "Open the data your scenario names and skim it — know what is in there before you prompt.",
    "Split the roles: for each deliverable, one builder, one verifier. Swap as you go.",
    "Agree the order of work and who presents what. Write it in the capture box."],
  "findings": [
    {"label": "Your scenario", "hint": "S1–S7 + its name"},
    {"label": "Who builds / who verifies, per deliverable", "hint": "initials are enough"}],
  "expect": "A scenario you both understand, the data open on one screen, and a role split written down. No deliverable started — that is the point of Phase 0.",
  "stretch": "Write the one-sentence version of your recommendation now, before any analysis. At the end, check: did the data change your mind?",
  "boss": "Name the single number in your data most likely to sink the initiative if it is wrong. That is the first thing your verifier checks."},

 {"app": "Claude · D1",
  "title": "T2 · Deliverable 1 — Executive briefing",
  "scenario": "One page that a director reads in ninety seconds: situation, key findings, recommendation, implementation, expected outcomes, next steps. You write the CTFT prompt from your scenario — Claude drafts, you verify and cut. (~35 min)",
  "steps": [
    "Attach your scenario’s data to a new Claude chat — keep this one conversation for the whole capstone.",
    "Write a full CTFT prompt for a one-page executive briefing with the six sections above.",
    "Verify every number in the draft against the sheet or the report — the verifier owns this pass.",
    "Cut it to one page. Recommendation near the top; nothing in it you cannot defend."],
  "findings": [
    {"label": "The number a sceptical director will challenge", "hint": "and where it comes from"},
    {"label": "One thing Claude got wrong or vague", "hint": "what you fixed"}],
  "expect": "A one-page briefing where the recommendation leads and every figure traces to your data. Ninety seconds to read, nothing wasted.",
  "stretch": "Ask Claude to attack it: “What would a sceptical CFO push back on in this briefing?” Fix the two best objections.",
  "boss": "Write the 60-word version — the summary for the executive who will not read even one page. Same recommendation, nothing lost that matters."},

 {"app": "Claude Design / Gamma · D2",
  "title": "T3 · Deliverable 2 — Stakeholder presentation",
  "scenario": "Five to six slides that carry your briefing into a room. You compared Claude Design and Gamma yesterday — now pick the one that fits this job and build. (~35 min)",
  "launches": [
    {"label": "Open Claude", "href": "https://claude.ai/new", "note": "Claude Design — build the deck in the same conversation as your briefing."},
    {"label": "Open Gamma", "href": "https://gamma.app", "note": "Or paste your prompt into Gamma and pick a theme."}],
  "steps": [
    "Choose your tool — you earned an opinion on this yesterday. One sentence on why.",
    "Build 5–6 slides from your briefing, in the same conversation, so Claude keeps the context.",
    "Check every figure on every slide against the source — a wrong number in a deck travels fastest.",
    "Fix at least one slide by hand: order, emphasis, or a chart that says it better."],
  "findings": [
    {"label": "Which tool, and why", "hint": "one honest sentence"},
    {"label": "A figure you verified on a slide", "hint": "number + source"}],
  "expect": "A 5–6 slide deck that tells the same story as the briefing — title, problem, evidence, recommendation, plan — with every number checked.",
  "stretch": "Regenerate your evidence slide for a different audience — the tenants, or the front-line team. Notice what has to change, and what must not.",
  "boss": "Run the same prompt in the other tool and keep whichever deck is honestly better. Be ready to say why in the Q&amp;A."},

 {"app": "Claude · D3",
  "title": "T4 · Deliverable 3 — Data analysis &amp; visualisations",
  "scenario": "Two to three charts that carry the argument, each with one written insight underneath. Not decoration — evidence. (~25 min)",
  "steps": [
    "Decide the two or three claims your initiative stands on. Each gets exactly one chart.",
    "Ask Claude to build each chart from your workbook, and to show the numbers behind it.",
    "Verify one number per chart by hand — the verifier recalculates it from the sheet.",
    "Write one insight sentence under each chart, then drop them into the deck."],
  "findings": [
    {"label": "Your charts", "hint": "e.g. “ticket ageing by contractor · occupancy trend”"},
    {"label": "The numbers you recalculated by hand", "hint": "one per chart"}],
  "expect": "Two or three charts, each defending one claim in your briefing, each with a verified number and a one-line insight. If a chart defends nothing, it goes.",
  "stretch": "Build the counter-chart — the one view of the data that argues against your initiative. Address it in your pitch before the room finds it.",
  "boss": "Ask Claude to list the exact sheet rows behind every chart. Spot-check two. That citation habit is the single most useful thing you take back to work."},

 {"app": "Claude · D4",
  "title": "T5 · Deliverable 4 — Communication package",
  "scenario": "The initiative is decided — now it has to land. Pick the two items that fit your scenario’s audience, then bank three reusable prompt templates. (~15 min)",
  "steps": [
    "Choose TWO of: an internal email to staff · a public tenant/customer FAQ · a one-page fact sheet.",
    "Generate both with full CTFT prompts. Same facts as the briefing — no new claims.",
    "Cross-check the two items against each other and the briefing. One story, three documents.",
    "Save three prompt templates with [PLACEHOLDERS] — the ones your department would reuse."],
  "findings": [
    {"label": "Which two items you chose, and for whom", "hint": "item + audience"},
    {"label": "Your three saved templates", "hint": "titles are enough"}],
  "expect": "Two finished communication items that agree with the briefing on every fact, plus three templates ready for the prompt library you started yesterday.",
  "stretch": "Take one item and produce it in three lengths — full email, lobby poster, SMS. Same facts, three formats: one more library entry.",
  "boss": "Draft the answer to the most hostile question your audience could ask — and put it in the FAQ before anyone has to ask it out loud."},

 {"app": "Team · Present",
  "title": "T6 · Assemble, rehearse, present",
  "scenario": "Assemble the package, run the pitch once out loud, cut what does not earn its place. Six minutes per team, then one question from the room. (~5 min prep · presentations from 11:45)",
  "steps": [
    "Assemble: briefing → deck (with charts in) → comms items. One package, one story.",
    "Run the pitch once, out loud, against the clock: title → problem → evidence → recommendation → implementation &amp; cost → next steps.",
    "Cut whatever broke the six minutes. Cutting is the last skill of the workshop.",
    "Decide who takes the Q&amp;A — and prepare your answer to “how do you know?” for your three biggest claims."],
  "findings": [
    {"label": "Who presents which section", "hint": "name → section"},
    {"label": "Your answer to “how do you know?”", "hint": "for your biggest claim"}],
  "expect": "A six-minute pitch you have actually run once, a package that tells one consistent story, and a ready answer for the obvious challenge.",
  "stretch": "Prepare the three-minute emergency version — if the schedule slips, the teams that can compress still land their recommendation.",
  "boss": "Trade packages with another team for two minutes and find one number in theirs to challenge in Q&amp;A. Expect them to do the same to you."},
]

# ---------- splice ----------
out = src
out = out.replace('<title>Day 2 Lab — Presentations, Data &amp; Prompt Libraries · CODED × Alshaya</title>',
                  '<title>Day 3 Lab — The Capstone Project · CODED × Alshaya</title>')
out = out.replace('<span class="day-chip">Day 2 · AI Lab</span>', '<span class="day-chip">Day 3 · Capstone</span>')
out = out.replace('Write every prompt yourself — the reveal is there if you get stuck. Stretch if you\'re early, Boss if you\'re fast.',
                  'One scenario, four deliverables, one pitch. Write every prompt yourselves — build in pairs, verify everything. Stretch if you\'re early, Boss if you\'re fast.')
out = out.replace('href="coded-alshaya-day-2.html"', 'href="coded-alshaya-day-3.html"')
out = out.replace("const KEY='alshaya_ai_day2';", "const KEY='alshaya_ai_day3';")
out = out.replace("Clear all your captured notes for Day 2?", "Clear all your captured notes for Day 3?")
out = out.replace("'Exercise '+(cur+1)", "'Task '+(cur+1)")
out = out.replace('Exercise ${cur+1} of ${TASKS.length}', 'Task ${cur+1} of ${TASKS.length}')
out = out.replace('Next exercise \\u203a', 'Next task \\u203a')
out = out.replace('<span class="crumb" id="crumb">Exercise 1</span>', '<span class="crumb" id="crumb">Task 1</span>')

# widget support: insert right after the scenario paragraph in render()
anchor = '      <p class="scn">${t.scenario}</p>\n'
assert anchor in out
out = out.replace(anchor, anchor + "      ${t.widget?t.widget:''}\n")

# swap TASKS
m = re.search(r'const TASKS = \[.*?\];\n', out, re.S)
assert m
out = out[:m.start()] + 'const TASKS = ' + json.dumps(TASKS, ensure_ascii=False) + ';\n' + out[m.end():]

(SITE / 'coded-alshaya-day-3-lab.html').write_text(out)
print('written', len(out), 'bytes')

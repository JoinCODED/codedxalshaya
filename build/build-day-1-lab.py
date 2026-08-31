# -*- coding: utf-8 -*-
"""Day 1 trainee lab — same format as the CODED x Burgan Copilot lab
   (rail + task runner + capture + localStorage), re-themed to CODED SPECIMEN
   crimson and rewritten for Alshaya / Al-Injaz on Claude."""
import json

LOGOF = "/Users/ayaalsaqaf/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/46c4e867-24f6-4e25-8db5-adecbebe4172/c097c4a3-d3ad-45b5-8472-60354fdb96eb/skills/workshop-builder/assets/coded-logo.txt"
OUT   = "/Users/ayaalsaqaf/codedxalshaya/site/coded-alshaya-day-1-lab.html"
LOGO  = open(LOGOF).read().strip()

CLAUDE = "https://claude.ai/new"

TASKS = [
{
 "app": "Claude",
 "title": "L1.1 · First Contact",
 "scenario": "Your first useful result out of Claude, on your own laptop. This is a confidence exercise, "
             "not a skills exercise — pick whichever starter appeals. (~8 min · Task Sheet 1)",
 "steps": [
   "Open Claude and start a new chat.",
   "Pick ONE starter below and tap it to copy, then run it.",
   "Read the result: would you actually use it? That is the bar.",
   "Turn to the person next to you and name one thing that surprised you."
 ],
 "starters": [
   "Explain [a term your department uses] in two sentences, like I am new here.",
   "Draft a three-line message telling my team the 10am site walk moved to 11am.",
   "Give me five ways to say \u201cthank you for your patience\u201d to a frustrated tenant.",
   "Turn these rough notes into three clear bullet points: [paste your notes].",
   "Rewrite this to sound more professional and polite: [paste your sentence].",
   "Summarise what this email is asking me to do, in one line: [paste the email].",
   "Suggest three subject lines for an email about [your topic].",
   "Give me a checklist for [a routine task you do], so I do not miss a step."
 ],
 "expect": "One result on screen you would actually consider sending, and one sentence on what was "
           "missing from it.",
 "stretch": "Steer it without rewriting your prompt: \u201cMake it shorter.\u201d \u2192 \u201cMake it warmer.\u201d "
            "\u2192 \u201cNow write it for a tenant who has already complained twice.\u201d That is iterative prompting, early.",
 "boss": "Break it on purpose. Ask for a specific figure, date or regulation, get Claude to be confidently "
         "wrong, and catch it. Bring what you found to the debrief \u2014 the hallucination lesson, discovered yourself."
},
{
 "app": "Claude",
 "title": "L1.2 · Build a CTFT Prompt",
 "scenario": "Pick one of two scenarios, both sample data. Read the stand-in document, then build a prompt "
             "using all four CTFT ingredients \u2014 Context, Task, Format, Tone. Assemble it, run it, and compare "
             "the result against the document: did it miss anything, or invent anything? (~12 min · Task Sheet 2)",
 "steps": [
   "Choose Scenario A (leasing) or Scenario B (maintenance) in the tool below.",
   "Read the stand-in document, then fill the four CTFT fields.",
   "Press Assemble, press Copy, and open Claude with Test in Claude.",
   "Paste Claude\u2019s answer into the capture box and flag anything missing or invented."
 ],
 "widget": """<div class="lw-tabs"><button class="lw-tab on" data-sc="a">Scenario A · Leasing</button><button class="lw-tab" data-sc="b">Scenario B · Maintenance</button></div>
<div class="lw-job"><span data-sc="a"><b>Your job:</b> using CTFT, get Claude to draft a one-page leasing update for the regional director with a clear recommendation.</span><span data-sc="b" hidden><b>Your job:</b> using CTFT, get Claude to draft a tenant-facing notice about the maintenance backlog \u2014 honest, calm, and specific.</span></div>
<div class="lw-doc"><pre class="lw-pre" data-sc="a">LEASING UPDATE \u2014 Stand-in document (sample data)

PROPERTY: [PROPERTY A] \u2014 retail centre, 48 units, opened 2019.
PERIOD: Quarter just closed.

KEY FACTS
- Occupancy: 75% (36 of 48 units let). Down from 83% same quarter last year.
- 12 units vacant. 5 have been vacant more than 9 months.
- 3 leases expiring within 90 days; 2 tenants have not responded to renewal outreach.
- Average rent achieved: KWD 11.40/sqm, against an KWD 13.00 asking rate.
- Footfall down 8% year on year; two anchor tenants report flat sales.
- One new signing this quarter: a food-and-beverage operator, 240 sqm, 5-year term.
- Marketing spend for the quarter came in 18% under budget.

MANAGEMENT NARRATIVE
"The vacancy is concentrated in the upper floor. We expect the F&amp;B signing to lift
footfall and support upper-floor leasing from next quarter."

LEASING MANAGER RECOMMENDATION
Hold the asking rate. Redirect unspent marketing budget to upper-floor incentives.</pre><pre class="lw-pre" data-sc="b" hidden>MAINTENANCE BACKLOG \u2014 Stand-in document (sample data)

SITE: [PROPERTY B] \u2014 mixed-use building, 14 floors, 62 tenancies.
PERIOD: Month just closed.

KEY FACTS
- 40 open maintenance tickets. 11 are older than 30 days.
- Breakdown: 17 HVAC, 9 plumbing, 7 lifts, 5 lighting, 2 other.
- The north lift has failed 4 times this month; parts are on 3-week lead time.
- Average time to close a ticket: 12 days, against a 5-day service standard.
- Two contractors are behind schedule; one has not been on site in 8 days.
- Tenant complaints logged this month: 23, up from 9 last month.
- Budget: 62% of the annual maintenance budget spent, with 5 months remaining.

TENANT SENTIMENT
Three tenants have escalated in writing. One has asked about a rent concession.

FACILITIES MANAGER NOTE
Lift parts ordered. Contractor performance meeting scheduled. Backlog plan needed
for the operations director by Thursday.</pre></div>
<div class="lw-fields">
<input id="lwC" placeholder="Context (C) — your role + the situation, using the document">
<input id="lwT" placeholder="Task (T) — the one thing Claude should produce">
<input id="lwF" placeholder="Format (F) — length, structure, sections">
<input id="lwTo" placeholder="Tone (T) — the voice + any guardrails">
<div class="lw-row"><button class="lw-btn" id="lwBuild">Assemble the prompt ↓</button><button class="lw-btn ghost" id="lwCopy">Copy</button><span class="lw-hint" id="lwCopyHint"></span></div>
<textarea class="lw-out" id="lwOut" readonly placeholder="Your assembled CTFT prompt appears here — Copy it, then Test in Claude."></textarea>
<div class="lw-row"><a class="lw-test" href="__CLAUDE__" target="_blank" rel="noopener">Test in Claude ↗</a><span class="lw-hint" style="color:var(--ink-faint)">Paste the result in the capture box below to compare.</span></div>
</div>""",
 "expect": "One assembled CTFT prompt, a result from Claude, and one sentence on how it matched \u2014 or "
           "missed \u2014 the source document. Sample data only; never paste real tenant or contract figures.",
 "stretch": "Switch to the other scenario and build a second prompt from scratch, all four ingredients, "
            "first try. Notice which ingredient changed the output most.",
 "boss": "Drop one ingredient on purpose. Run the same prompt with no Format, then with no Context. "
         "Write down which omission did the most damage \u2014 that is the ingredient you must never skip."
},
{
 "app": "Claude",
 "title": "L1.3 · Draft a Professional Document",
 "scenario": "Take a real-shaped brief and produce something you would be comfortable sending. Draft it with "
             "a full CTFT prompt, then edit it by hand. (~15 min · Task Sheet 3)",
 "steps": [
   "Pick one brief below and tap it to copy \u2014 or use your own real task.",
   "Write a full CTFT prompt for it. Do not skip Format or Tone.",
   "Generate the draft, then edit by hand: fix the tone, check every fact and number, cut anything repeated.",
   "Read your final version out loud once before you finish. If you stumble, so will the reader."
 ],
 "widget": """<div class="lw-tabs"><button class="lw-tab on" data-sc="a">Brief 1 · Staff memo</button><button class="lw-tab" data-sc="b">Brief 2 · Tenant notice</button><button class="lw-tab" data-sc="c">Brief 3 · Status update</button></div>
<div class="lw-briefs">
<pre class="lw-pre copyable" data-sc="a">BRIEF 1 — Staff memo (sample data)
Tap to copy, then build your CTFT prompt around it.

Starting the first of next month, the site office moves from Building 2 to
Building 5, floor 3. Parking moves to the east lot. The move happens over one
weekend; nobody should lose a working day. Staff need to pack their own desks by
the Thursday before. IT will move equipment. Anyone needing accessible parking
should contact facilities this week.

Audience: all 60 site staff. Nobody has been told yet.</pre>
<pre class="lw-pre copyable" data-sc="b" hidden>BRIEF 2 — Tenant notice (sample data)
Tap to copy, then build your CTFT prompt around it.

The north lift will be out of service Thursday, 9 AM to 12 PM, for a scheduled
parts replacement. The south lift stays running. The north lift has already
failed twice this month, so tenants are frustrated. Deliveries to floors 8–14
should be rescheduled or routed through the south lift.

Audience: all 62 tenancies. Tone matters — this is the third notice this month.</pre>
<pre class="lw-pre copyable" data-sc="c" hidden>BRIEF 3 — Status update (sample data)
Tap to copy, then build your CTFT prompt around it.

Fit-out on the ground-floor unit is 3 weeks behind. Cause: a late joinery
delivery, now on site. Revised handover is the end of next month. Cost impact is
within contingency. The tenant has been told verbally but not in writing. The
regional director wants a written position before the board pack goes out Friday.

Audience: regional director. Short on time, dislikes surprises.</pre>
</div>
<div class="lw-row"><a class="lw-test" href="__CLAUDE__" target="_blank" rel="noopener">Open Claude ↗</a><span class="lw-hint" style="color:var(--ink-faint)">Paste your finished document in the capture box below.</span></div>""",
 "expect": "A document you would actually be comfortable sending, with every fact checked by you \u2014 not by Claude.",
 "stretch": "Ask Claude to critique its own draft: \u201cWhat is weak about this? What would a sceptical reader "
            "push back on?\u201d Fix the two best points it raises.",
 "boss": "Write the version nobody wants to write: the same update, but the delay is now 8 weeks and it is "
         "our fault. Own it, give a plan, promise nothing you cannot deliver, stay under 150 words."
},
{
 "app": "Claude",
 "title": "L1.4 · Rewrite It — Tone and Length",
 "scenario": "You already have a draft. Now change it without starting over. This is the move you will use "
             "more than any other. (~10 min)",
 "steps": [
   "Copy the clunky paragraph below into Claude.",
   "Run each rewrite command in turn, in the SAME conversation. Do not start a new chat.",
   "Notice what survives every version \u2014 that is the actual message.",
   "Paste the version you would send into the capture box."
 ],
 "prompt": "Please be advised that with reference to the aforementioned maintenance matter previously "
           "raised, it has been determined following an internal review that the necessary remedial works "
           "will be undertaken in due course, and it is anticipated that the situation will be resolved "
           "within a reasonable timeframe, subject to contractor availability and the receipt of the "
           "required parts, and we thank you for your continued patience in this regard.",
 "widget": """<div class="lw-job"><b>Run these in order, same chat:</b></div>
<div class="lw-starters">
<div class="prompt st-prompt" data-p="Rewrite this in plain English. Same facts, half the length."><span class="copy-tag">tap to copy</span>Rewrite this in plain English. Same facts, half the length.</div>
<div class="prompt st-prompt" data-p="Now cut it to three bullet points."><span class="copy-tag">tap to copy</span>Now cut it to three bullet points.</div>
<div class="prompt st-prompt" data-p="Now make it warmer — this goes to a tenant who has already complained twice."><span class="copy-tag">tap to copy</span>Now make it warmer — this goes to a tenant who has already complained twice.</div>
<div class="prompt st-prompt" data-p="Now make it formal — this version goes in the file as the written record."><span class="copy-tag">tap to copy</span>Now make it formal — this version goes in the file as the written record.</div>
<div class="prompt st-prompt" data-p="Say the whole thing in one sentence."><span class="copy-tag">tap to copy</span>Say the whole thing in one sentence.</div>
<div class="prompt st-prompt" data-p="Give me a version I could send as an SMS, under 160 characters."><span class="copy-tag">tap to copy</span>Give me a version I could send as an SMS, under 160 characters.</div>
</div>
<div class="lw-row" style="margin-top:14px"><a class="lw-test" href="__CLAUDE__" target="_blank" rel="noopener">Open Claude ↗</a></div>""",
 "expect": "Six versions of one paragraph, and a clear view of which one you would actually send \u2014 and to whom.",
 "stretch": "Go too far on purpose: \u201cMake it half as long\u201d three times in a row. Find the point where it "
            "stops being useful. That edge is worth knowing.",
 "boss": "Reverse it. Take your one-sentence version and ask Claude to expand it back into a formal letter. "
         "Compare it to the original paragraph \u2014 what did it invent to fill the space?"
},
{
 "app": "Claude",
 "title": "L1.5 · Tame the Thread",
 "scenario": "A long email thread you have been copied into. Find out what it actually says, what you owe "
             "anyone, and draft the reply. (~10 min)",
 "steps": [
   "Tap the thread below to copy it.",
   "Ask Claude for a summary in the shape you need \u2014 decisions, open questions, and who owns what.",
   "Check the summary against the thread. Did it miss anything? Did it invent an owner?",
   "Draft your reply, then rewrite it once for tone."
 ],
 "widget": """<div class="lw-briefs"><pre class="lw-pre copyable">EMAIL THREAD — Stand-in (sample data). Tap to copy.

From: [FACILITIES], Mon 08:12
Subject: Ground-floor unit — handover
Joinery has landed on site. Fit-out team say they need 3 more weeks. I have not
told the tenant a revised date yet. Can someone confirm the contingency position
before I do?

From: [FINANCE], Mon 09:40
Re: Ground-floor unit — handover
Contingency covers it, roughly KWD 18k of a KWD 25k allowance. But if it slips
past the end of next month we are into the next budget period and I will need a
variation. Please do not commit to a date without checking with me.

From: [LEASING], Mon 11:05
Re: Ground-floor unit — handover
The tenant has already asked me twice. They have a fit-out crew booked and are
paying for storage in the meantime. If we slip again they will ask for rent-free
compensation — they hinted at two weeks' worth.

From: [REGIONAL DIRECTOR], Mon 16:22
Re: Ground-floor unit — handover
I need a written position before the board pack goes out Friday. One page. What
is the date, what does it cost, and who is accountable for the slip. Not a
discussion — a position.

From: [FACILITIES], Tue 07:55
Re: Ground-floor unit — handover
Contractor performance meeting is Wednesday. I will have a firm date after that.
Can we hold the written position until Wednesday afternoon?</pre></div>
<div class="lw-job" style="margin-top:14px"><b>Try this prompt:</b></div>
<div class="prompt st-prompt" data-p="Summarise this email thread in five bullet points. List every decision that was actually made, every question still open, and who owns each action. Then tell me what I personally need to do and by when."><span class="copy-tag">tap to copy</span>Summarise this email thread in five bullet points. List every decision that was actually made, every question still open, and who owns each action. Then tell me what I personally need to do and by when.</div>
<div class="lw-row"><a class="lw-test" href="__CLAUDE__" target="_blank" rel="noopener">Open Claude ↗</a></div>""",
 "expect": "A summary that correctly separates what was decided from what is still open \u2014 and a reply you "
           "would send to the regional director.",
 "stretch": "Ask for the same thread summarised three ways: for the regional director, for finance, and for "
            "the tenant. Same facts, three audiences. Notice what you would never say to the tenant.",
 "boss": "There is a trap in this thread \u2014 nobody has actually agreed a date, but it reads like they have. "
         "Get Claude to state the revised handover date as if it were settled, catch it doing so, then rewrite "
         "your prompt so it cannot make that mistake."
},
{
 "app": "Claude",
 "title": "L1.6 · Summarize and Verify",
 "scenario": "The last skill of the day, and the one that keeps you out of trouble. Summarise a five-page "
             "operations report, then check the summary against the source \u2014 by hand. The report has "
             "deliberate errors planted in it. (~12 min · Task Sheet 4)",
 "asset": {"href": "alshaya-quarterly-operations-report.pdf",
           "label": "Download the report (PDF, 5 pages, sample data)"},
 "steps": [
   "Download the Quarterly Property Operations Report above, then attach it to Claude. It is sample data \u2014 safe to upload.",
   "Write a CTFT prompt asking for a one-page summary with key points and open questions.",
   "Pick THREE facts or numbers from the summary and check each one against the report, by hand.",
   "The report has deliberate mistakes in it. Find at least one and note which section it is in.",
   "Note anything Claude got wrong, or quietly left out."
 ],
 "widget": """<div class="lw-job"><b>Two prompts to run, in order:</b></div>
<div class="lw-starters">
<div class="prompt st-prompt" data-p="Summarise this in one page: the position, the three biggest risks, and every open question. Use bullet points. Do not add anything that is not in the source."><span class="copy-tag">tap to copy</span>Summarise this in one page: the position, the three biggest risks, and every open question. Use bullet points. Do not add anything that is not in the source.</div>
<div class="prompt st-prompt" data-p="List every number you used in that summary, next to the exact line you took it from."><span class="copy-tag">tap to copy</span>List every number you used in that summary, next to the exact line you took it from.</div>
</div>
<div class="lw-row" style="margin-top:14px"><a class="lw-test" href="__CLAUDE__" target="_blank" rel="noopener">Open Claude ↗</a></div>""",
 "expect": "A one-page summary, plus a short list of what you checked and what you found. There are five "
           "planted faults in the report. Finding one is a pass. Finding three is very good.",
 "stretch": "That second prompt \u2014 asking it to cite the line for every number \u2014 is the single most useful "
            "verification habit of the day. Run it on the summary you made in L1.5 too.",
 "boss": "Find all five. Then work out which one Claude stated most confidently while being wrong \u2014 "
         "that is the one that would have reached the Board."
},
]

for t in TASKS:
    if "widget" in t: t["widget"] = t["widget"].replace("__CLAUDE__", CLAUDE)

CSS = """
:root{
  --base:#0A0507; --base2:#070406; --surf:#150A0D; --surf2:#1C0E12;
  --card:#130A0C; --card-2:#190E11; --raise:#241019; --panel:#120A0C;
  --maroon:#5D181A; --mid:#8B1E2A; --crimson:#C8324A; --rose:#E0566E; --rose-lt:#EC8B9C;
  --gold:#E9C46A; --gold-lt:#F5DFA8;
  --ink:#F5F0F1; --ink-dim:#AEA2A5; --ink-faint:#76696C;
  --w:#fff; --w8:rgba(255,255,255,.82); --w7:rgba(255,255,255,.7); --w6:rgba(255,255,255,.58);
  --w5:rgba(255,255,255,.46); --w4:rgba(255,255,255,.34); --w3:rgba(255,255,255,.3);
  --w2:rgba(255,255,255,.16); --w1:rgba(255,255,255,.09); --w06:rgba(255,255,255,.06);
  --line:rgba(255,255,255,.08); --line-2:rgba(255,255,255,.14);
  --green:#3DC873; --green-lt:#8FE6AE; --green-bg:rgba(61,200,115,.12); --green-bd:rgba(61,200,115,.4);
  --amber:#E9C46A; --ac-cyan:#6FCFE4;
  --f:'Manrope',system-ui,sans-serif; --mf:'Manrope',system-ui,sans-serif;
  --mono:'Space Mono',ui-monospace,monospace;
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{background:radial-gradient(1100px 640px at 85% -8%,rgba(200,50,74,.12),transparent 60%),var(--base);
  color:var(--ink);font-family:var(--f);-webkit-font-smoothing:antialiased;line-height:1.5;
  overflow-x:hidden;display:flex;min-height:100vh}
a{color:inherit;text-decoration:none}
a:focus-visible,button:focus-visible{outline:2px solid var(--rose);outline-offset:3px;border-radius:4px}

/* left rail */
#rail{width:290px;flex:none;border-right:1px solid var(--line);background:var(--base2);
  display:flex;flex-direction:column;height:100vh;position:sticky;top:0}
.rail-brand{padding:20px 22px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:11px}
.rail-brand .coded-logo{height:16px}
.rail-brand .x{color:var(--ink-faint);font-size:11px}
.rail-brand .partner{font-size:12px;font-weight:800;letter-spacing:.14em;color:var(--ink)}
.day-chip{margin:16px 22px 0;display:inline-flex;align-self:flex-start;font-family:var(--mono);font-size:11px;font-weight:700;
  letter-spacing:.12em;text-transform:uppercase;color:var(--rose-lt);background:rgba(200,50,74,.1);
  border:1px solid rgba(200,50,74,.3);border-radius:999px;padding:6px 12px}
.prog-wrap{margin:16px 22px 6px}
.prog-bar{height:6px;border-radius:3px;background:var(--w06);overflow:hidden}
.prog-fill{height:100%;width:0;background:linear-gradient(90deg,var(--rose),var(--crimson));transition:width .3s}
.prog-label{font-family:var(--mono);font-size:11px;color:var(--ink-faint);margin-top:7px}
#navList{flex:1;overflow-y:auto;padding:12px}
.nav-item{display:flex;align-items:center;gap:11px;padding:11px 12px;border-radius:10px;cursor:pointer;transition:background .15s;margin-bottom:3px}
.nav-item:hover{background:var(--w06)}
.nav-item.active{background:rgba(200,50,74,.12);border:1px solid rgba(200,50,74,.25)}
.nav-item .ni-n{flex:none;width:24px;height:24px;border-radius:7px;background:var(--w06);border:1px solid var(--w1);
  font-family:var(--mono);font-size:11px;font-weight:700;color:var(--rose-lt);display:flex;align-items:center;justify-content:center}
.nav-item.done .ni-n{background:var(--green-bg);border-color:var(--green-bd);color:var(--green-lt)}
.nav-item .ni-t{font-size:13px;font-weight:600;color:var(--ink);line-height:1.3}
.rail-foot{padding:14px 18px;border-top:1px solid var(--line);display:flex;gap:10px}
.rail-foot button{flex:1;font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
  padding:9px;border-radius:8px;border:1px solid var(--w1);background:var(--w06);color:var(--ink-dim);cursor:pointer}
.rail-foot button:hover{color:var(--ink)}
@media(max-width:820px){#rail{position:fixed;left:-300px;z-index:50;transition:left .2s}#rail.open{left:0}}

/* main */
#main{flex:1;min-width:0;display:flex;flex-direction:column}
#mtop{position:sticky;top:0;z-index:20;background:rgba(10,5,7,.9);backdrop-filter:blur(16px);
  border-bottom:1px solid var(--line);padding:14px 28px;display:flex;align-items:center;gap:14px}
#mtop .back{display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:700;color:var(--ink-dim);
  background:var(--w06);border:1px solid var(--w1);border-radius:8px;padding:7px 11px}
#mtop .back:hover{color:var(--ink)}
#mtop .ham{display:none}
@media(max-width:820px){#mtop .ham{display:inline-flex;background:var(--w06);border:1px solid var(--w1);border-radius:8px;padding:8px;cursor:pointer;color:var(--ink)}}
#mtop .crumb{font-family:var(--mono);font-size:12px;color:var(--ink-faint);flex:1}
#mtop .mnav{display:flex;gap:8px}
#mtop .mnav button{width:34px;height:34px;border-radius:8px;border:1px solid var(--w1);background:var(--w06);color:var(--ink-dim);cursor:pointer}
#mtop .mnav button:hover{color:var(--ink)}

#view{max-width:820px;margin:0 auto;padding:38px 28px 90px;width:100%}
.task-tag{display:inline-flex;align-items:center;gap:8px;font-family:var(--mono);font-size:11px;font-weight:700;
  letter-spacing:.1em;text-transform:uppercase;color:var(--rose-lt);margin-bottom:14px}
.task-tag .app{background:rgba(200,50,74,.14);border:1px solid rgba(200,50,74,.3);border-radius:6px;padding:3px 8px}
h1.task-h{font-size:26px;font-weight:800;letter-spacing:-.3px;margin-bottom:12px}
.scn{font-size:15px;line-height:1.65;color:var(--ink-dim);margin-bottom:24px}

.step-card{background:linear-gradient(180deg,var(--surf2),var(--surf));border:1px solid var(--w1);border-radius:14px;padding:22px 24px;margin-bottom:18px}
.step-card .sc-k{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--rose-lt);margin-bottom:12px}
.step-card ol{margin:0;padding-left:20px}
.step-card li{font-size:14.5px;color:var(--ink);line-height:1.55;margin-bottom:8px}
.prompt{font-family:var(--mono);font-size:13px;color:var(--ink);background:rgba(0,0,0,.28);border:1px solid var(--w1);
  border-radius:9px;padding:14px 16px;padding-right:74px;line-height:1.55;margin:14px 0;position:relative;cursor:pointer;transition:border-color .15s}
.prompt:hover{border-color:rgba(200,50,74,.4)}
.prompt .copy-tag{position:absolute;top:8px;right:10px;font-size:10px;color:var(--ink-faint);font-family:var(--mono)}
.prompt.copied{border-color:var(--green-bd)}
.prompt.copied .copy-tag{color:var(--green-lt)}

.expect{background:rgba(233,196,106,.06);border:1px solid rgba(233,196,106,.28);border-radius:12px;padding:18px 20px;margin-bottom:18px}
.expect .ex-k{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--amber);margin-bottom:8px}
.expect p{font-size:14px;color:var(--ink);line-height:1.55}

.capture{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 20px}
.capture label{display:block;font-size:13px;font-weight:700;color:var(--ink);margin-bottom:10px}
.capture textarea{width:100%;min-height:90px;background:var(--base);border:1px solid var(--w1);border-radius:9px;
  padding:12px 14px;color:var(--ink);font-family:var(--f);font-size:14px;line-height:1.5;resize:vertical}
.capture textarea:focus{outline:none;border-color:rgba(200,50,74,.5)}
.capture .cap-row{display:flex;align-items:center;gap:12px;margin-top:12px}
.cap-btn{padding:10px 18px;border-radius:9px;border:none;font-weight:700;font-size:13.5px;cursor:pointer;color:#fff;
  background:linear-gradient(135deg,var(--crimson),var(--maroon));box-shadow:0 6px 20px rgba(200,50,74,.3)}
.cap-btn:hover{transform:translateY(-1px)}
.cap-done{font-family:var(--mono);font-size:12px;color:var(--green-lt);display:none;align-items:center;gap:7px}
.cap-done.on{display:inline-flex}

.task-foot{display:flex;justify-content:space-between;margin-top:30px;gap:12px}
.tf-btn{padding:12px 20px;border-radius:10px;border:1px solid var(--w1);background:var(--w06);color:var(--ink);font-weight:700;font-size:14px;cursor:pointer}
.tf-btn.next{background:linear-gradient(135deg,var(--crimson),var(--maroon));border:none;color:#fff}
.tf-btn:disabled{opacity:.4;cursor:not-allowed}

/* widgets */
.lw-tabs{display:flex;gap:9px;flex-wrap:wrap;margin-bottom:14px}
.lw-tab{padding:8px 14px;border-radius:9px;font-size:12.5px;font-weight:700;cursor:pointer;
  border:1px solid var(--w1);background:var(--w06);color:var(--ink-dim);transition:.15s}
.lw-tab.on{border-color:rgba(200,50,74,.5);color:var(--ink);background:rgba(200,50,74,.13)}
.lw-job{font-size:13.5px;color:var(--ink);line-height:1.55;margin-bottom:14px}
.lw-job b{color:var(--rose-lt)}
.lw-doc{background:rgba(0,0,0,.3);border:1px solid var(--w1);border-radius:10px;padding:12px 15px;max-height:300px;overflow:auto;margin-bottom:16px}
.lw-pre{font-family:var(--mono);font-size:11px;line-height:1.55;color:var(--ink-dim);white-space:pre-wrap;margin:0}
.lw-fields{display:flex;flex-direction:column;gap:9px}
.lw-fields input{width:100%;background:var(--base);border:1px solid var(--w1);border-radius:9px;
  padding:11px 14px;color:var(--ink);font-family:var(--f);font-size:13.5px}
.lw-fields input:focus{outline:none;border-color:rgba(200,50,74,.5)}
.lw-row{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:4px}
.lw-btn{padding:9px 16px;border-radius:9px;border:none;font-weight:700;font-size:13px;cursor:pointer;color:#fff;
  background:linear-gradient(135deg,var(--crimson),var(--maroon))}
.lw-btn.ghost{background:var(--w06);border:1px solid var(--w1);color:var(--ink-dim)}
.lw-btn:hover{transform:translateY(-1px)}
.lw-hint{font-family:var(--mono);font-size:11px;color:var(--green-lt)}
.lw-out{width:100%;min-height:78px;margin-top:10px;background:rgba(0,0,0,.28);border:1px solid var(--w1);
  border-radius:9px;padding:12px 14px;color:var(--ink);font-family:var(--mono);font-size:12px;line-height:1.55;resize:vertical}
.lw-out:focus{outline:none;border-color:rgba(200,50,74,.5)}
.lw-test{display:inline-flex;align-items:center;gap:7px;font-size:13px;font-weight:700;color:var(--ink);
  background:var(--w06);border:1px solid var(--w1);border-radius:9px;padding:9px 15px}
.lw-test:hover{border-color:rgba(200,50,74,.45)}
.lw-starters{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.lw-starters .prompt{margin:0}
@media(max-width:640px){.lw-starters{grid-template-columns:1fr}}
.lw-briefs{margin-bottom:12px}
.lw-briefs .lw-pre{background:rgba(0,0,0,.3);border:1px solid var(--w1);border-radius:10px;padding:14px 16px;
  max-height:300px;overflow:auto;cursor:pointer;transition:border-color .15s;position:relative}
.lw-briefs .lw-pre:hover{border-color:rgba(200,50,74,.4)}
.lw-briefs .lw-pre.copied{border-color:var(--green-bd)}
"""

SCRIPT = """
  const TASKS = __TASKS__;
  const KEY='alshaya_ai_day1';
  let state=JSON.parse(localStorage.getItem(KEY)||'{}');
  let cur=0;

  const navList=document.getElementById('navList');
  function buildNav(){
    navList.innerHTML='';
    TASKS.forEach((t,i)=>{
      const el=document.createElement('div');
      el.className='nav-item'+(i===cur?' active':'')+((state[i]&&state[i].done)?' done':'');
      el.innerHTML='<span class="ni-n">'+((state[i]&&state[i].done)?'\\u2713':(i+1))+'</span><span class="ni-t">'+t.title+'</span>';
      el.onclick=()=>{cur=i;render()};
      navList.appendChild(el);
    });
  }
  function updateProg(){
    const done=Object.values(state).filter(x=>x&&x.done).length;
    document.getElementById('progFill').style.width=(done/TASKS.length*100)+'%';
    document.getElementById('progLabel').textContent=done+' of '+TASKS.length+' done';
  }
  function save(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}

  function render(){
    const t=TASKS[cur];const st=state[cur]||{};
    document.getElementById('crumb').textContent='Task '+(cur+1)+' \\u00b7 '+t.app;
    const v=document.getElementById('view');
    v.innerHTML=`
      <div class="task-tag"><span class="app">${t.app}</span> Task ${cur+1} of ${TASKS.length}</div>
      <h1 class="task-h">${t.title}</h1>
      <p class="scn">${t.scenario}</p>
      ${t.steps?`<div class="step-card"><div class="sc-k">Steps</div><ol>${t.steps.map(s=>'<li>'+s+'</li>').join('')}</ol>
        ${t.prompt?`<div class="prompt" id="promptBox" style="white-space:pre-wrap"><span class="copy-tag">tap to copy</span>${t.prompt}</div>`:''}
      </div>`:''}
      ${t.asset?`<a class="lw-test" href="${t.asset.href}" download style="margin:0 0 18px">\u2b07 ${t.asset.label}</a>`:''}
      ${t.starters?`<div class="step-card"><div class="sc-k">Starter menu \\u2014 tap any to copy</div><div class="lw-starters">${t.starters.map(x=>'<div class="prompt st-prompt" data-p="'+x.replace(/"/g,'&quot;')+'"><span class="copy-tag">tap to copy</span>'+x+'</div>').join('')}</div></div>`:''}
      ${t.widget?`<div class="step-card"><div class="sc-k">Build &amp; test</div>${t.widget}</div>`:''}
      <div class="expect"><div class="ex-k">Done looks like</div><p>${t.expect}</p></div>
      ${t.stretch?`<div class="step-card" style="border-left:3px solid var(--rose)"><div class="sc-k">Tier 2 \\u00b7 Stretch \\u2014 finished early?</div><p style="font-size:14px;color:var(--ink);line-height:1.55">${t.stretch}</p></div>`:''}
      ${t.boss?`<div class="step-card" style="border-left:3px solid var(--gold)"><div class="sc-k" style="color:var(--gold-lt)">Tier 3 \\u00b7 Boss Challenge</div><p style="font-size:14px;color:var(--ink);line-height:1.55">${t.boss}</p></div>`:''}
      <div class="capture">
        <label>Paste your Claude result (or a note on how it went)</label>
        <textarea id="note" placeholder="Optional \\u2014 saves to your browser so you can review later.">${st.note||''}</textarea>
        <div class="cap-row">
          <button class="cap-btn" id="markDone">${st.done?'Saved \\u2713':'Mark done'}</button>
          <span class="cap-done ${st.done?'on':''}" id="capDone">\\u2713 Captured</span>
        </div>
      </div>
      <div class="task-foot">
        <button class="tf-btn" id="tfPrev" ${cur===0?'disabled':''}>\\u2039 Previous</button>
        <button class="tf-btn next" id="tfNext" ${cur===TASKS.length-1?'disabled':''}>Next task \\u203a</button>
      </div>`;

    function flash(el,tagSel){const tag=el.querySelector(tagSel);el.classList.add('copied');
      if(tag){const old=tag.textContent;tag.textContent='copied \\u2713';
        setTimeout(()=>{el.classList.remove('copied');tag.textContent=old},1500);}
      else setTimeout(()=>el.classList.remove('copied'),1200);}
    function copy(text,el,tagSel){
      const done=()=>flash(el,tagSel);
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done).catch(()=>fallback(text,done));}
      else fallback(text,done);
    }
    function fallback(text,done){const ta=document.createElement('textarea');ta.value=text;
      ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();
      try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(ta);}

    const pb=document.getElementById('promptBox');
    if(pb)pb.onclick=()=>copy(t.prompt,pb,'.copy-tag');
    v.querySelectorAll('.st-prompt').forEach(sp=>sp.onclick=()=>copy(sp.dataset.p,sp,'.copy-tag'));
    v.querySelectorAll('.lw-pre.copyable').forEach(pre=>pre.onclick=()=>copy(pre.innerText,pre,'.nope'));

    if(v.querySelector('.lw-tabs')){
      const tabs=v.querySelectorAll('.lw-tab');
      tabs.forEach(tb=>tb.onclick=()=>{const sc=tb.dataset.sc;
        tabs.forEach(x=>x.classList.toggle('on',x===tb));
        v.querySelectorAll('.lw-doc [data-sc], .lw-job [data-sc], .lw-briefs [data-sc]').forEach(el=>{el.hidden=el.dataset.sc!==sc});
      });
    }
    if(document.getElementById('lwBuild')){
      const gg=id=>{const el=document.getElementById(id);return el?el.value.trim():''};
      document.getElementById('lwBuild').onclick=()=>{document.getElementById('lwOut').value=[gg('lwC'),gg('lwT'),gg('lwF'),gg('lwTo')].filter(Boolean).join(' ')};
      document.getElementById('lwCopy').onclick=()=>{const o=document.getElementById('lwOut').value.trim();if(!o)return;
        const h=document.getElementById('lwCopyHint');
        const ok=()=>{h.textContent='copied \\u2713';setTimeout(()=>h.textContent='',1500)};
        if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(o).then(ok).catch(()=>fallback(o,ok));
        else fallback(o,ok);};
    }
    document.getElementById('markDone').onclick=()=>{
      const note=document.getElementById('note').value;
      state[cur]={done:true,note};save();document.getElementById('capDone').classList.add('on');
      document.getElementById('markDone').textContent='Saved \\u2713';buildNav();updateProg();
    };
    document.getElementById('note').oninput=e=>{state[cur]=state[cur]||{};state[cur].note=e.target.value;save()};
    const p=document.getElementById('tfPrev'),n=document.getElementById('tfNext');
    if(p)p.onclick=()=>{if(cur>0){cur--;render();window.scrollTo(0,0)}};
    if(n)n.onclick=()=>{if(cur<TASKS.length-1){cur++;render();window.scrollTo(0,0)}};
    buildNav();updateProg();
  }
  document.getElementById('mPrev').onclick=()=>{if(cur>0){cur--;render();window.scrollTo(0,0)}};
  document.getElementById('mNext').onclick=()=>{if(cur<TASKS.length-1){cur++;render();window.scrollTo(0,0)}};
  document.getElementById('ham').onclick=()=>document.getElementById('rail').classList.toggle('open');
  document.getElementById('resetBtn').onclick=()=>{if(confirm('Clear all your captured notes for Day 1?')){state={};save();cur=0;render()}};
  render();
""".replace("__TASKS__", json.dumps(TASKS, ensure_ascii=False))

FAVICON = ("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2032%2032%22"
           "%3E%3Crect%20width%3D%2232%22%20height%3D%2232%22%20rx%3D%227%22%20fill%3D%22%230A0507%22%2F%3E%3Ccircle%20cx%3D"
           "%2216%22%20cy%3D%2216%22%20r%3D%227%22%20fill%3D%22%23C8324A%22%2F%3E%3C%2Fsvg%3E")

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>Day 1 Lab — AI in Workflow for Professionals · CODED × Alshaya</title>
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
  <aside id="rail">
    <div class="rail-brand"><img class="coded-logo" alt="CODED" src="{LOGO}"><span class="x">×</span><span class="partner">ALSHAYA</span></div>
    <span class="day-chip">Day 1 · AI Lab</span>
    <div class="prog-wrap">
      <div class="prog-bar"><div class="prog-fill" id="progFill"></div></div>
      <div class="prog-label" id="progLabel">0 of 6 done</div>
      <div class="prog-label" style="margin-top:9px;color:var(--gold-lt);line-height:1.5">Finish the core steps, then keep going — there's always more. Stretch if you're early, Boss if you're fast.</div>
    </div>
    <div id="navList"></div>
    <div class="rail-foot"><button id="resetBtn">↺ Reset</button></div>
  </aside>

  <div id="main">
    <div id="mtop">
      <button class="ham" id="ham" aria-label="Menu"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
      <a class="back" href="coded-alshaya-day-1.html">‹ Back</a>
      <span class="crumb" id="crumb">Task 1</span>
      <div class="mnav"><button id="mPrev">‹</button><button id="mNext">›</button></div>
    </div>
    <div id="view"></div>
  </div>

<script>{SCRIPT}</script>
</body>
</html>
"""
open(OUT, "w").write(page)
print("wrote", OUT, len(page), "bytes,", len(TASKS), "tasks")

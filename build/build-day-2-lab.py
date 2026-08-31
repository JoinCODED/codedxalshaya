# -*- coding: utf-8 -*-
"""Day 2 trainee lab — same format as the CODED x Burgan Copilot Day 2 lab
   (dataset blocks, goal + reveal-prompt + findings, multi-step exercises),
   re-themed to CODED SPECIMEN crimson and rewritten for Alshaya on Claude.
   Shares its base CSS with the Day 1 lab generator."""
import json, re, os

LOGOF = "/Users/ayaalsaqaf/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/46c4e867-24f6-4e25-8db5-adecbebe4172/c097c4a3-d3ad-45b5-8472-60354fdb96eb/skills/workshop-builder/assets/coded-logo.txt"
OUT   = "/Users/ayaalsaqaf/codedxalshaya/site/coded-alshaya-day-2-lab.html"
LOGO  = open(LOGOF).read().strip()
CLAUDE, GAMMA = "https://claude.ai/new", "https://gamma.app"

# base CSS comes verbatim from the validated Day 1 lab
_d1 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build-day-1-lab.py")).read()
CSS = _d1[_d1.index('CSS = """') + len('CSS = """') : ]
CSS = CSS[: CSS.index('"""')]

CSS += """
/* ===== Day 2 additions: dataset, findings, goal, reveal, launch ===== */
.dataset{background:var(--card);border:1px solid var(--line-2);border-radius:14px;padding:18px 20px;margin-bottom:18px}
.dataset .ds-k{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--rose-lt);margin-bottom:6px}
.dataset .ds-note{font-size:13.5px;color:var(--ink-dim);line-height:1.55;margin-bottom:12px}
.dl{display:inline-flex;align-items:center;gap:10px;padding:11px 16px;border-radius:10px;
  border:1px solid rgba(61,200,115,.3);background:rgba(61,200,115,.07);color:var(--ink);font-size:13.5px;font-weight:700}
.dl:hover{border-color:rgba(61,200,115,.6)}
.dl .ic{width:26px;height:26px;border-radius:7px;background:rgba(61,200,115,.16);display:flex;align-items:center;justify-content:center;font-size:13px}
.dl small{display:block;font-weight:600;font-size:11px;color:var(--ink-faint);margin-top:1px}
.ds-table-wrap{margin-top:14px;overflow-x:auto;border:1px solid var(--w1);border-radius:10px}
table.ds-table{border-collapse:collapse;width:100%;font-family:var(--mono);font-size:11.5px}
table.ds-table th{background:var(--surf2);color:var(--ink);text-align:left;padding:8px 10px;border-bottom:1px solid var(--w1);white-space:nowrap;font-weight:700}
table.ds-table td{padding:7px 10px;border-bottom:1px solid rgba(255,255,255,.05);color:var(--ink-dim);white-space:nowrap}
table.ds-table tr:last-child td{border-bottom:none}
.ds-more{font-family:var(--mono);font-size:11px;color:var(--ink-faint);padding:8px 10px}
.recap-card{background:var(--card);border:1px solid var(--line-2);border-radius:14px;padding:18px 20px;margin-bottom:18px}
.recap-pre{margin-top:10px;background:var(--surf);border:1px solid var(--w1);border-radius:10px;padding:14px 16px;
  font-family:var(--mono);font-size:11.5px;line-height:1.6;color:var(--ink-dim);white-space:pre-wrap;margin-bottom:0}
.launch-btn{display:flex;align-items:center;justify-content:space-between;gap:14px;margin-bottom:18px;padding:18px 22px;
  border-radius:14px;color:#fff;background:linear-gradient(135deg,var(--crimson),var(--maroon));
  box-shadow:0 8px 26px rgba(200,50,74,.3);transition:transform .16s}
.launch-btn:hover{transform:translateY(-1px)}
.launch-btn b{font-size:15.5px;display:block}
.launch-btn span.sub{font-size:13px;color:rgba(255,255,255,.82);display:block;margin-top:3px}
.launch-btn .ar{font-size:22px;flex:none}
.pstep{background:linear-gradient(180deg,var(--surf2),var(--surf));border:1px solid var(--w1);border-radius:14px;padding:18px 20px;margin-bottom:14px}
.pstep-h{display:flex;align-items:center;gap:11px;font-size:14.5px;font-weight:800;color:var(--ink);margin-bottom:12px}
.pstep-n{flex:none;width:26px;height:26px;border-radius:8px;background:rgba(200,50,74,.14);border:1px solid rgba(200,50,74,.35);
  display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:12px;font-weight:700;color:var(--rose-lt)}
.findings{margin-top:12px;display:grid;grid-template-columns:1fr 1fr;gap:10px}
@media(max-width:620px){.findings{grid-template-columns:1fr}}
.find{display:flex;flex-direction:column;gap:5px}
.find span{font-size:12px;font-weight:700;color:var(--ink-dim)}
.find-in{background:var(--base);border:1px solid var(--w1);border-radius:8px;padding:9px 11px;color:var(--ink);font-family:var(--f);font-size:13.5px}
.find-in:focus{outline:none;border-color:rgba(200,50,74,.5)}
.find-in.filled{border-color:var(--green-bd)}
.findings-k{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--amber);margin:2px 0 8px}
.ctft-note{margin-bottom:16px;border-left:3px solid var(--rose);background:rgba(200,50,74,.07);border-radius:0 12px 12px 0;
  padding:13px 17px;font-size:13.5px;color:var(--ink-dim);line-height:1.55}
.ctft-note b{color:var(--ink)}
.goal{background:rgba(233,196,106,.06);border:1px solid rgba(233,196,106,.28);border-radius:10px;padding:13px 16px;font-size:14.5px;color:var(--ink);line-height:1.55}
.goal .gk{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--amber);margin-bottom:6px}
details.reveal{margin-top:12px}
details.reveal>summary{cursor:pointer;font-family:var(--mono);font-size:12px;font-weight:700;color:var(--rose-lt);list-style:none}
details.reveal>summary::-webkit-details-marker{display:none}
details.reveal[open]>summary{color:var(--ink-dim);margin-bottom:10px}
details.reveal .prompt{margin:0}
"""

WB = {"label":"alshaya-day-2-dataset.xlsx", "href":"alshaya-day-2-dataset.xlsx",
      "note":"One workbook, six sheets — occupancy and income, the maintenance log, budget against actual, "
             "the employee survey, and the candidate sheet. Every figure is invented for the workshop, so it "
             "is safe to upload."}

DS_OCC = dict(WB, head=["Month","Property","Units","Units Let","Occupancy %","Monthly Rent (KWD)","Collection %"],
  rows=[["2026-01","[PROPERTY A]","48","40","83.3","179,640","98.1"],
        ["2026-01","[PROPERTY B]","62","57","91.9","221,388","98.4"],
        ["2026-06","[PROPERTY A]","48","36","75.0","161,676","96.2"],
        ["2026-06","[PROPERTY B]","62","56","90.3","217,504","96.8"]],
  more="… 18 rows on the Occupancy & Income sheet, plus four more sheets")

DS_MNT = dict(WB, head=["Ticket ID","Date Raised","Property","Category","Priority","Status","Days Open"],
  rows=[["MT-014","2026-04-20","[PROPERTY A]","HVAC","Medium","Open","71"],
        ["MT-021","2026-05-06","[PROPERTY B]","Lifts","High","Open","55"],
        ["MT-033","2026-05-18","[PROPERTY B]","Plumbing","Medium","Closed","8"],
        ["MT-052","2026-06-09","[PROPERTY A]","Lighting","Low","Open","21"]],
  more="… 68 tickets on the Maintenance Log sheet")

DS_CAND = dict(WB, head=["Candidate ID","Role Applied","Years Exp.","Key Skills","Certifications","Notice (wks)"],
  rows=[["C-01","Property Manager","9","Leasing, tenant relations, budgeting","RICS (part)","8"],
        ["C-05","Leasing Executive","6","Retail leasing, negotiation, CRM","Certified Leasing Prof.","6"],
        ["C-09","Facilities Technician","11","HVAC, lifts, contractor supervision","HVAC Level 3, IOSH","8"],
        ["C-12","Facilities Manager","14","Multi-site operations, capital projects","NEBOSH, PMP","12"]],
  more="… 12 candidates on the Candidates sheet. IDs only — deliberately no names.")

TASKS = [
{
 "app":"Claude Design · 1A", "title":"D2.1 · Report to deck",
 "scenario":"Yesterday's quarterly report, turned into a deck for the operations director. Same content, "
            "new format — and Claude already has the context if you keep it in one conversation. Write the "
            "prompt yourself. (~15 min · Task Sheet 1)",
 "files":[{"label":"alshaya-quarterly-operations-report.pdf",
           "href":"alshaya-quarterly-operations-report.pdf",
           "note":"Your source document — the Day 1 quarterly report. Attach it to Claude."}],
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Attach the PDF, then build the deck with Claude Design."}],
 "steps":["Attach the report to a new Claude conversation.",
          "Write your own CTFT prompt to hit the goal below, then ask Claude to design it.",
          "Open two slides and check every figure against the source PDF.",
          "Fix one slide by hand, so you feel where Claude stops and you start."],
 "goal":"Get Claude to turn the report into a six-slide management summary — position, occupancy and income, "
        "costs, construction, risks, and a closing 'so what' — with every figure traceable to the source.",
 "prompt":"[CONTEXT] I manage operations for a three-asset property portfolio. The attached quarterly report "
          "covers the quarter ended 30 June 2026. [TASK] Turn it into a six-slide management summary for the "
          "operations director. [FORMAT] Slides: position, occupancy and income, costs, construction, risks, "
          "and a closing 'so what'. Every figure must be traceable to the source. [TONE] Professional and direct.",
 "findings":[{"label":"A figure you verified against the PDF","hint":"the number + which section"},
             {"label":"Anything Claude got wrong or vague?","hint":"what you would fix"}],
 "expect":"A six-slide deck built from the report, with at least two figures you personally checked against "
          "the source. A deck that looks right but misquotes a number is worse than no deck.",
 "stretch":"Ask Claude to rewrite the same deck for a different audience — the tenants rather than the director. "
           "Notice what it drops, and what it should never have said out loud.",
 "boss":"The report has five deliberate errors in it. Ask Claude to fact-check the report against itself before "
        "it builds anything, and see how many it catches."
},
{
 "app":"Gamma · 1B", "title":"D2.2 · Same prompt, different tool",
 "scenario":"Take the prompt you just wrote and run it somewhere else. This is the whole point of learning the "
            "prompt rather than the product. (~10 min)",
 "launches":[{"label":"Open Gamma","href":GAMMA,"note":"Paste the same prompt and generate the deck."}],
 "steps":["Copy the prompt you wrote in D2.1 — the exact same one.",
          "Generate the deck in Gamma. Pick a theme.",
          "Put the two decks side by side and answer the questions below honestly.",
          "Export the Gamma deck to PowerPoint and see what shifts."],
 "goal":"Produce the same six-slide summary in Gamma, then decide which tool you would actually use for this "
        "job — and be able to say why in one sentence.",
 "findings":[{"label":"Which produced the better first draft?","hint":"Claude Design or Gamma"},
             {"label":"Which needed less fixing?","hint":"and roughly how much less"},
             {"label":"What broke in the PowerPoint export?","hint":"spacing, fonts, charts…"},
             {"label":"Which would you use on Sunday?","hint":"one sentence, honestly"}],
 "expect":"Two decks from one prompt, and a clear personal answer on which tool suits which job. There is no "
          "right answer here — there is only your answer, with a reason attached.",
 "stretch":"Change one word in the prompt — the audience — and regenerate in both. Which tool responds more to "
           "the change?",
 "boss":"Build the same deck a third way: ask Claude for the outline only, then paste that outline into Gamma. "
        "Does the hybrid beat either tool alone?"
},
{
 "app":"Claude · 2A", "title":"D2.3 · Finance — monthly performance",
 "scenario":"Use case 2. Finance compiles occupancy, rental income and maintenance cost by hand every month. "
            "Build the repeatable version: clean it, find the trend, draft the summary. Three passes, and you "
            "write every prompt. (~20 min · Task Sheet 2)",
 "dataset":DS_OCC,
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Upload the workbook, then work the three steps below."}],
 "steps":["Download the workbook and upload it to Claude.",
          "For each step below, write your own CTFT prompt, run it, verify against the sheet, then record what you found."],
 "promptSteps":[
   {"label":"Step 1 · Find the trend",
    "goal":"Get Claude to identify the occupancy and income trend for each property across the six months — "
           "with the numbers behind each claim, so you can check them.",
    "prompt":"Analyse the Occupancy & Income sheet. For each property, describe the trend in occupancy, rent "
             "and collection rate across the six months. Show the numbers behind each claim so I can check them.",
    "findings":[{"label":"Which property is declining?","hint":"property + how much"},
                {"label":"By how much did occupancy move?","hint":"from % to %"},
                {"label":"What is happening to collections?","hint":"the number"}]},
   {"label":"Step 2 · Cost overruns by property",
    "goal":"Get Claude to compare the Budget vs Actual sheet line by line, calculate every variance, and rank "
           "them from largest overspend to largest underspend.",
    "prompt":"From the Budget vs Actual sheet, calculate the variance for each category as actual minus planned. "
             "Rank them from largest overspend to largest underspend, and give me the total variance. Show your working.",
    "findings":[{"label":"Largest overspend","hint":"category + KWD"},
                {"label":"Largest underspend","hint":"category + KWD"},
                {"label":"Total variance — check it yourself","hint":"KWD, recalculated by hand"}]},
   {"label":"Step 3 · Draft the management summary",
    "goal":"Get Claude to write a management-ready summary — the position, the two biggest concerns, and one "
           "recommendation — with every claim backed by a number from the workbook.",
    "prompt":"Write a management summary of this portfolio for the operations director. Five bullets maximum: "
             "the overall position, the two biggest concerns, and one recommended action. Back every bullet with "
             "a number from the workbook. Professional and direct.",
    "findings":[{"label":"Biggest concern it surfaced","hint":"and the number behind it"},
                {"label":"Did every bullet carry a number?","hint":"yes / no — which one did not"}]}],
 "expect":"Every findings box filled from the sheet, one variance you recalculated by hand, and a summary you "
          "would actually send. If a bullet has no number behind it, it does not go in.",
 "stretch":"Ask Claude to build the same summary as a repeatable template with [PLACEHOLDERS] for next month's "
           "figures. That template is the real deliverable — the analysis was just this month.",
 "boss":"Ask Claude for the total annualised rent roll. Then add the two monthly figures yourself and multiply "
        "by twelve. The Day 1 report got this wrong — does Claude?"
},
{
 "app":"Claude · 2B", "title":"D2.4 · Facilities — logs to report",
 "scenario":"Use case 3. Raw maintenance tickets go in, a weekly management report and a tenant notice come "
            "out. This is draft, rewrite and summarize from Day 1, pointed at operational data. (~20 min)",
 "dataset":DS_MNT,
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Upload the workbook and work from the Maintenance Log sheet."}],
 "steps":["Upload the workbook and point Claude at the Maintenance Log sheet.",
          "Write your own CTFT prompt for each step. Verify the counts yourself before you trust the write-up."],
 "promptSteps":[
   {"label":"Step 1 · The weekly management report",
    "goal":"Get Claude to turn 68 raw tickets into a structured weekly report — volumes by category, what is "
           "ageing, which contractor is behind, and what needs a decision.",
    "prompt":"From the Maintenance Log sheet, write a weekly maintenance report for the operations director. "
             "Cover: open tickets by category, anything older than 30 days, average days to close by category, "
             "contractor performance, and what needs a decision this week. Use short headed sections.",
    "findings":[{"label":"How many tickets are open?","hint":"count them yourself"},
                {"label":"Worst category by close time","hint":"category + days"},
                {"label":"How many older than 30 days?","hint":"check against the sheet"}]},
   {"label":"Step 2 · The tenant notice",
    "goal":"Get Claude to draft a tenant-facing notice about the lift work — honest about the disruption, "
           "specific about timing, and short enough that people read it.",
    "prompt":"Using the lift tickets in this log, draft a notice to all tenants about the upcoming lift repair. "
             "Under 120 words. Say what is happening, when, what to do instead, and apologise once — not three "
             "times. Clear and calm, not corporate.",
    "findings":[{"label":"Word count of the draft","hint":"was it under 120?"},
                {"label":"What did you have to change?","hint":"tone, a fact, a promise it should not make"}]}],
 "expect":"A weekly report whose counts you verified against the sheet, and a tenant notice you would be "
          "comfortable putting on a noticeboard with your name on it.",
 "stretch":"Ask for the same notice in three lengths — a full email, a lobby poster, and an SMS. Same facts, "
           "three formats. That is one prompt library entry, not three.",
 "boss":"The log contains a contractor that has not attended site. Get Claude to find it without you naming it, "
        "then draft the escalation email to that contractor. Firm, factual, no threats."
},
{
 "app":"Claude · 3A", "title":"D2.5 · HR — screening support",
 "scenario":"Use case 1. High volumes of CVs for property, leasing and facilities roles. Build the screening "
            "scaffolding — a summary template, a criteria screen, and interview questions — while every hiring "
            "decision stays with the manager. (~20 min)",
 "dataset":DS_CAND,
 "launches":[{"label":"Open Claude","href":CLAUDE,"note":"Upload the workbook and work from the Candidates sheet."}],
 "steps":["Upload the workbook and point Claude at the Candidates sheet.",
          "Write your own CTFT prompt for each step below.",
          "Read the last step carefully — it is the one that matters most."],
 "promptSteps":[
   {"label":"Step 1 · A reusable candidate summary template",
    "goal":"Get Claude to design a structured summary template you could apply to any candidate for any role — "
           "the same fields every time, so two candidates can actually be compared.",
    "prompt":"Design a one-paragraph candidate summary template for property and facilities roles. It should "
             "capture experience, relevant skills, certifications, availability, and one open question for "
             "interview. Use [PLACEHOLDERS] so I can reuse it for any candidate.",
    "findings":[{"label":"How many fields does your template have?","hint":"fewer is usually better"},
                {"label":"What did you add that Claude missed?","hint":"something your process needs"}]},
   {"label":"Step 2 · Screen against role criteria",
    "goal":"Get Claude to sort the candidates for ONE role against criteria you define — and to show its "
           "reasoning for each, so a human can overrule it.",
    "prompt":"For the Facilities Manager role, screen the candidates on the Candidates sheet against these "
             "criteria: 5+ years experience, a safety certification, and 8 weeks notice or less. Group them "
             "into meets / partly meets / does not meet, and give one line of reasoning for each candidate.",
    "findings":[{"label":"Who met every criterion?","hint":"candidate IDs"},
                {"label":"Do you agree with its reasoning?","hint":"where would you overrule it?"},
                {"label":"Any candidate it judged unfairly?","hint":"and why"}]},
   {"label":"Step 3 · Interview questions",
    "goal":"Get Claude to draft a first-draft interview set for that role — questions that test the criteria "
           "rather than testing how well someone interviews.",
    "prompt":"Draft eight first-round interview questions for the Facilities Manager role. Four on technical "
             "and contractor management, two on safety and compliance, two behavioural. For each, tell me what "
             "a strong answer would contain.",
    "findings":[{"label":"Best question in the set","hint":"the one you would keep"},
                {"label":"Weakest question","hint":"and why you would cut it"}]}],
 "expect":"A reusable summary template, a screened shortlist you can defend line by line, and eight interview "
          "questions you would actually ask. The hiring decision never leaves the hiring manager.",
 "stretch":"Ask Claude to rewrite the criteria screen so it explicitly ignores location and notice period. "
           "Compare the two shortlists — did convenience quietly outrank capability the first time?",
 "boss":"Fairness check. Ask Claude what information in this sheet could lead to a biased screen, and what it "
        "would need to see instead to judge candidates on capability alone. Bring the answer to the debrief."
},
{
 "app":"Claude · 4A", "title":"D2.6 · Build your prompt library",
 "scenario":"Everything above was practice. This is the part you keep. Collect the prompts that actually worked "
            "today and turn them into something you will open again next week. (~15 min · Task Sheet 4)",
 "steps":["Scroll back through today's exercises and find the prompts that worked best.",
          "For each one, save four things: a title, the full CTFT prompt with [PLACEHOLDERS], which tool it "
          "worked best in, and what you had to fix afterwards.",
          "Add one prompt for a task in your own department that nobody else here would need.",
          "Save it somewhere you will actually find it — not your downloads folder."],
 "goal":"Leave today with at least five reusable prompts, written with placeholders, each labelled with the "
        "tool it worked in and the thing you had to fix.",
 "prompt":"Here are the prompts that worked for me today: [PASTE THEM]. Turn them into a clean prompt library. "
          "For each one give a short title, the prompt with [PLACEHOLDERS] where the details change, the tool "
          "it suits, and a one-line note on what to check in the output. Format it as a document I can save.",
 "findings":[{"label":"How many prompts did you save?","hint":"five is the target"},
             {"label":"The one from your own department","hint":"what task is it for?"},
             {"label":"Where did you save it?","hint":"be specific — you will need this next week"}],
 "expect":"A saved document with at least five ready-to-reuse prompts, one of them written for your own job, "
          "and a location you can name out loud.",
 "stretch":"Ask Claude to spot the pattern across your saved prompts — what do your best ones have in common "
           "that the weaker ones do not?",
 "boss":"Write the prompt you would give a colleague who was not here today, so they could get one of these "
        "results without the workshop. If it needs explaining, it is not finished."
},
]

FAVICON = ("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2032%2032%22"
           "%3E%3Crect%20width%3D%2232%22%20height%3D%2232%22%20rx%3D%227%22%20fill%3D%22%230A0507%22%2F%3E%3Ccircle%20cx%3D"
           "%2216%22%20cy%3D%2216%22%20r%3D%227%22%20fill%3D%22%23C8324A%22%2F%3E%3C%2Fsvg%3E")

SCRIPT = """
  const TASKS = __TASKS__;
  const KEY='alshaya_ai_day2';
  let state=JSON.parse(localStorage.getItem(KEY)||'{}');
  let cur=0;

  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
  const navList=document.getElementById('navList');
  function buildNav(){
    navList.innerHTML='';
    TASKS.forEach((t,i)=>{
      const el=document.createElement('div');
      el.className='nav-item'+(i===cur?' active':'')+((state[i]&&state[i].done)?' done':'');
      el.innerHTML='<span class="ni-n">'+((state[i]&&state[i].done)?'\\u2713':(i+1))+'</span><span class="ni-t">'+t.title+'</span>';
      el.onclick=()=>{cur=i;render();window.scrollTo(0,0)};
      navList.appendChild(el);
    });
  }
  function updateProg(){
    const done=Object.values(state).filter(x=>x&&x.done).length;
    document.getElementById('progFill').style.width=(done/TASKS.length*100)+'%';
    document.getElementById('progLabel').textContent=done+' of '+TASKS.length+' done';
  }
  function save(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}

  function datasetBlock(d){
    return `<div class="dataset"><div class="ds-k">Attached data</div>
      <div class="ds-note">${d.note}</div>
      <a class="dl" href="${d.href}" download><span class="ic">\\u2b07</span><span>Download workbook<small>${esc(d.label)}</small></span></a>
      <div class="ds-table-wrap"><table class="ds-table">
        <thead><tr>${d.head.map(h=>'<th>'+esc(h)+'</th>').join('')}</tr></thead>
        <tbody>${d.rows.map(r=>'<tr>'+r.map(c=>'<td>'+esc(c)+'</td>').join('')+'</tr>').join('')}</tbody>
      </table><div class="ds-more">${esc(d.more||'')}</div></div></div>`;
  }
  function filesBlock(files){
    return `<div class="dataset"><div class="ds-k">Attached file${files.length>1?'s':''}</div>${files.map(f=>
      `<div class="ds-note">${f.note||''}</div><a class="dl" href="${f.href}" download><span class="ic">\\u2b07</span><span>Download<small>${esc(f.label)}</small></span></a>`).join('')}</div>`;
  }
  function findVal(k){return (state[cur]&&state[cur].findings&&state[cur].findings[k])||''}
  function findInput(k,f){
    const v=findVal(k);
    return `<label class="find"><span>${esc(f.label)}</span><input class="find-in${v?' filled':''}" data-fk="${k}" placeholder="${esc(f.hint||'')}" value="${String(v).replace(/"/g,'&quot;')}"></label>`;
  }
  function findingsBlock(findings,prefix){
    return `<div class="findings-k">\\u270e Record what you found</div><div class="findings">${findings.map((f,i)=>findInput(prefix+'_'+i,f)).join('')}</div>`;
  }
  function goalBlock(g){return `<div class="goal"><div class="gk">Your goal \\u2014 build a CTFT prompt for this</div>${esc(g)}</div>`;}
  function revealStep(prompt,si){
    return `<details class="reveal"><summary>\\ud83d\\udd13 Stuck? Reveal a suggested prompt</summary><div class="prompt psbox" data-ps="${si}"><span class="copy-tag">tap to copy</span>${esc(prompt)}</div></details>`;
  }
  function promptStepsBlock(steps){
    return steps.map((ps,si)=>`<div class="pstep">
      <div class="pstep-h"><span class="pstep-n">${si+1}</span>${esc(ps.label)}</div>
      ${ps.goal?goalBlock(ps.goal):''}
      ${ps.prompt?revealStep(ps.prompt,si):''}
      ${ps.findings?findingsBlock(ps.findings,'s'+si):''}
    </div>`).join('');
  }

  function render(){
    const t=TASKS[cur];const st=state[cur]||{};
    document.getElementById('crumb').textContent='Exercise '+(cur+1)+' \\u00b7 '+t.app;
    const v=document.getElementById('view');
    v.innerHTML=`
      <div class="task-tag"><span class="app">${t.app}</span> Exercise ${cur+1} of ${TASKS.length}</div>
      <h1 class="task-h">${t.title}</h1>
      <p class="scn">${t.scenario}</p>
      ${t.dataset?datasetBlock(t.dataset):''}
      ${t.files?filesBlock(t.files):''}
      ${t.launches?t.launches.map(l=>`<a class="launch-btn" href="${l.href}" target="_blank" rel="noopener"><span><b>${esc(l.label)}</b><span class="sub">${esc(l.note||'')}</span></span><span class="ar">\\u2192</span></a>`).join(''):''}
      ${(t.prompt||t.promptSteps)?`<div class="ctft-note"><b>Write the prompt yourself.</b> Use <b>CTFT \\u2014 Context \\u00b7 Task \\u00b7 Format \\u00b7 Tone</b> to build a prompt that hits each goal below. Stuck? Hit \\u201cReveal a suggested prompt\\u201d.</div>`:''}
      <div class="step-card"><div class="sc-k">Steps</div><ol>${t.steps.map(s=>'<li>'+s+'</li>').join('')}</ol>
        ${t.goal?goalBlock(t.goal):''}
        ${t.prompt?`<details class="reveal"><summary>\\ud83d\\udd13 Stuck? Reveal a suggested prompt</summary><div class="prompt" id="promptBox"><span class="copy-tag">tap to copy</span>${esc(t.prompt)}</div></details>`:''}
        ${t.findings?findingsBlock(t.findings,'top'):''}
      </div>
      ${t.promptSteps?promptStepsBlock(t.promptSteps):''}
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
        <button class="tf-btn next" id="tfNext" ${cur===TASKS.length-1?'disabled':''}>Next exercise \\u203a</button>
      </div>`;

    function flash(el){const tag=el.querySelector('.copy-tag');el.classList.add('copied');
      if(tag){tag.textContent='copied \\u2713';setTimeout(()=>{el.classList.remove('copied');tag.textContent='tap to copy'},1500);}
      else setTimeout(()=>el.classList.remove('copied'),1200);}
    function fallback(text,done){const ta=document.createElement('textarea');ta.value=text;
      ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();
      try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(ta);}
    function copy(text,el){const done=()=>flash(el);
      if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(text).then(done).catch(()=>fallback(text,done));
      else fallback(text,done);}

    const pb=document.getElementById('promptBox');
    if(pb)pb.onclick=()=>copy(t.prompt,pb);
    v.querySelectorAll('.psbox').forEach(box=>box.onclick=()=>copy(t.promptSteps[+box.dataset.ps].prompt,box));
    v.querySelectorAll('.find-in').forEach(inp=>inp.oninput=e=>{
      state[cur]=state[cur]||{}; state[cur].findings=state[cur].findings||{};
      state[cur].findings[e.target.dataset.fk]=e.target.value; save();
      e.target.classList.toggle('filled', !!e.target.value);
    });
    document.getElementById('markDone').onclick=()=>{
      const note=document.getElementById('note').value;
      state[cur]=Object.assign(state[cur]||{},{done:true,note});save();
      document.getElementById('capDone').classList.add('on');
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
  document.getElementById('resetBtn').onclick=()=>{if(confirm('Clear all your captured notes for Day 2?')){state={};save();cur=0;render()}};
  render();
""".replace("__TASKS__", json.dumps(TASKS, ensure_ascii=False))

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>Day 2 Lab — Presentations, Data &amp; Prompt Libraries · CODED × Alshaya</title>
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
  <aside id="rail">
    <div class="rail-brand"><img class="coded-logo" alt="CODED" src="{LOGO}"><span class="x">×</span><span class="partner">ALSHAYA</span></div>
    <span class="day-chip">Day 2 · AI Lab</span>
    <div class="prog-wrap">
      <div class="prog-bar"><div class="prog-fill" id="progFill"></div></div>
      <div class="prog-label" id="progLabel">0 of 6 done</div>
      <div class="prog-label" style="margin-top:9px;color:var(--gold-lt);line-height:1.5">Write every prompt yourself — the reveal is there if you get stuck. Stretch if you're early, Boss if you're fast.</div>
    </div>
    <div id="navList"></div>
    <div class="rail-foot"><button id="resetBtn">↺ Reset</button></div>
  </aside>

  <div id="main">
    <div id="mtop">
      <button class="ham" id="ham" aria-label="Menu"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
      <a class="back" href="coded-alshaya-day-2.html">‹ Back</a>
      <span class="crumb" id="crumb">Exercise 1</span>
      <div class="mnav"><button id="mPrev">‹</button><button id="mNext">›</button></div>
    </div>
    <div id="view"></div>
  </div>

<script>{SCRIPT}</script>
</body>
</html>
"""
open(OUT, "w").write(page)
print("wrote", OUT, len(page), "bytes,", len(TASKS), "exercises")

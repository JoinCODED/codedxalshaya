#!/usr/bin/env python3
# Build site/coded-alshaya-day-3-deck.html from the Day 2 deck shell (head/CSS/JS identical).
import re, pathlib

SITE = pathlib.Path(__file__).resolve().parent.parent / 'site'
src = (SITE / 'coded-alshaya-day-2-deck.html').read_text()

head, rest = src.split('<body>', 1)
body_start = '<body>\n\n'
tail = rest[rest.index('<div id="prail-wrap">'):]

# grab the cover logos block verbatim (CODED logo + ALSHAYA mark)
logos = re.search(r'<div class="cv2-logos">.*?</div>\n', rest, re.S).group(0)

head = head.replace(
    '<title>Day 2 · Presentations, Data &amp; Prompt Libraries — CODED × Alshaya</title>',
    '<title>Day 3 · The Capstone Project — CODED × Alshaya</title>')

tail = tail.replace('<a class="deck-back" href="coded-alshaya-day-2.html">‹ Day 2</a>',
                    '<a class="deck-back" href="coded-alshaya-day-3.html">‹ Day 3</a>')

TITLES = ["Title", "Callback", "Cold-open", "The day at a glance", "01 · Assessment", "Final assessment",
          "02 · The Brief", "One initiative", "Four deliverables", "Teams & scenarios", "How the build runs",
          "03 · Build", "Lab T1 · Plan", "Lab T2 · Briefing", "Lab T3 · Deck", "Break",
          "Lab T4 · Data", "Lab T5 · Comms", "Lab T6 · Rehearse",
          "04 · Present", "Running order", "What good looks like",
          "05 · Certification", "Certificates", "Wrap", "End"]
m = re.search(r'var TITLES=\[[^\]]*\]', tail)
tail = tail[:m.start()] + 'var TITLES=' + str(TITLES).replace("'", '"') + tail[m.end():]

# ---------- slide helpers ----------
def pad(inner, sid, extra=''):
    return (f'<div class="slide" id="{sid}"{extra}>\n'
            '<div class="bg-grid"></div><div class="blob b1"></div><div class="blob b2"></div><div class="slide-pad ">\n'
            f'{inner}\n</div>\n</div>\n')

def sec(sid, num, name):
    return (f'<div class="slide" id="{sid}">\n'
            '<div class="bg-grid"></div><div class="blob b1"></div><div class="blob b2"></div><div class="secwrap">\n'
            f'  <div class="secnum b">{num}</div>\n  <div class="sech b">{name}</div>\n  <div class="secrule b"></div>\n'
            '</div>\n</div>\n')

def ritem(n, t, d):
    return (f'    <div class="ritem b"><div class="rn">{n}</div><div><div class="rt">{t}</div>'
            f'<div class="rd">{d}</div></div></div>')

def labslide(sid, mins, tag, title, lead, steps, secs, task):
    rows = '\n'.join(ritem(i + 1, t, d) for i, (t, d) in enumerate(steps))
    mm = f'{mins}:00'
    return pad(
        f'<div class="topic-tab b">{tag}</div>\n'
        f'<h2 class="demo-h sm b">{title}</h2>\n'
        f'<p class="lead b">{lead}</p>\n'
        f'<div class="road b">\n{rows}\n</div>\n'
        f'<div class="exrow b"><button class="ex-go" onclick="exStart({secs})">▶ Start {mm}</button>'
        f'<a class="tsnote ex-open" href="coded-alshaya-day-3-lab.html#t{task}" target="_blank" rel="noopener">Open lab task T{task} ↗</a></div>',
        sid, extra=f' data-exmin="{mins}"')

def ocitem(txt):
    return ('    <div class="oc-item b"><div class="oc-check"><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"></path></svg></div>'
            f'<div class="oc-txt">{txt}</div></div>')

S = []

# 1 · cover
S.append(f'''<div class="slide active" id="cover">
<div class="cv2-bg"><div class="cv2-r1"></div><div class="cv2-r2"></div><div class="cv2-r3"></div><div class="cv2-b1"></div><div class="cv2-wash"></div></div>
<div class="bg-grid"></div><div class="cv2-vig"></div>
<div class="cv2">
  <div class="cv2-pill"><span class="dot"></span> CODED × Alshaya · Kuwait</div>
  {logos.strip()}
  <h1 class="cv2-title"><span class="cv2-t1">Two Days of Skills.</span><br><span class="cv2-t2">One Real Package.</span></h1>
  <p class="cv2-sub">Day 3 — The final assessment, the capstone build, and the certificate you leave with.</p>
  <div class="cv2-meta">
    <span class="cv2-daybadge">DAY 3</span>
    <span class="cv2-mi"><svg viewBox="0 0 24 24"><rect x="3" y="4.5" width="18" height="17" rx="2.5"/><path d="M16 2.5v4M8 2.5v4M3 10h18"/></svg> Thursday 3 September 2026</span>
    <span class="cv2-mi"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7.5v5l3 2"/></svg> 09:00 – 13:00</span>
    <span class="cv2-mi"><svg viewBox="0 0 24 24"><path d="M21 10.5c0 6.5-9 12.5-9 12.5s-9-6-9-12.5a9 9 0 0118 0z"/><circle cx="12" cy="10.5" r="3"/></svg> CODED Campus</span>
  </div>
  <div class="cv2-standby"><span class="pdot"></span> Ali Taqi · Alshaya &amp; Al-Injaz</div>
  <div class="cv2-cue">press <kbd>→</kbd> to begin · <kbd>?</kbd> for controls</div>
</div>
</div>
''')

# 2 · callback
S.append(pad(
 '<h2 class="demo-h b">Callback: <span class="hl">two days of CTFT</span></h2>\n'
 '<div class="anchor b">You can prompt, produce, and verify. Today nothing new is taught — you put everything into one implementation package, as a team, against the clock.</div>\n'
 '<div class="keyline b">No new tools. <b>Just proof.</b></div>', 's1'))

# 3 · cold-open
S.append(pad(
 '<div class="topic-tab b">Day 3</div>\n'
 '<h2 class="demo-h b">A package like this used to take a team <span class="hl">a week.</span></h2>\n'
 '<p class="lead b">Your team of two builds it before lunch.</p>', 's2'))

# 4 · day at a glance
S.append(pad(
 '<h2 class="demo-h sm b">The day at a glance</h2>\n'
 '<div class="road b">\n'
 + ritem('①', 'Final assessment — 09:00', '30 minutes, Days 1 and 2. Worked alone — link shared in the room.') + '\n'
 + ritem('②', 'The capstone build — 09:30', 'Plan, then four deliverables. Timed blocks, one break.') + '\n'
 + ritem('③', 'Team presentations — 11:45', 'Six minutes a team, one question from the room.') + '\n'
 + ritem('④', 'Certificates — 12:30', 'Certificates, the group photo, and the send-off.') + '\n'
 + '</div>\n<div class="keyline b">Every block runs on a visible timer. <b>The deadline is part of the exercise.</b></div>', 'sched'))

# 5 · section 01
S.append(sec('sec1', '01', 'Final Assessment'))

# 6 · assessment slide
S.append(pad(
 '<div class="topic-tab b">Assessment</div>\n'
 '<h2 class="demo-h sm b">The Final Assessment</h2>\n'
 '<p class="lead b">30 minutes · everything from Days 1 and 2</p>\n'
 '<div class="road b">\n'
 + ritem(1, 'Open the assessment link and work alone', 'Ali shares the link in the room — it covers everything from Days 1 and 2.') + '\n'
 + ritem(2, 'Notes allowed. AI is not.', 'The point is what stayed with you — Claude sits this one out.') + '\n'
 + ritem(3, 'Watch the clock', '30 minutes is comfortable if you keep moving. Do not camp on one question.') + '\n'
 + ritem(4, 'Finished? Sit tight', 'Submit, then re-read your capstone scenario — the build starts at 09:30 sharp.') + '\n'
 + '</div>\n'
 '<div class="exrow b"><button class="ex-go" onclick="exStart(1800)">▶ Start 30:00</button>'
 '<span class="tsnote">Assessment link — shared on the day</span></div>',
 'assess', extra=' data-exmin="30"'))

# 7 · section 02
S.append(sec('sec2', '02', 'The Capstone Brief'))

# 8 · one initiative
S.append(pad(
 '<h2 class="demo-h b">One initiative. <span class="hl">One package.</span></h2>\n'
 '<div class="anchor b">Your team proposes a real organisational initiative for the portfolio you have worked with for two days — and backs it with a briefing, a presentation, verified analysis, and the communications to land it.</div>\n'
 '<div class="keyline b">The point is not a perfect deliverable. <b>It is proving the workflow holds up under a deadline.</b></div>', 'goal'))

# 9 · four deliverables
S.append(pad(
 '<h2 class="demo-h sm b">The four deliverables</h2>\n'
 '<div class="gcards">\n'
 '  <div class="gcard b"><div class="ge">📄</div><div class="gh">1 · Executive briefing</div><div class="gt">One page, six sections — situation, key findings, recommendation, implementation, expected outcomes, next steps.</div></div>\n'
 '  <div class="gcard b"><div class="ge">🖥️</div><div class="gh">2 · Stakeholder deck</div><div class="gt">5–6 slides in Claude Design or Gamma — your choice, you compared them yesterday.</div></div>\n'
 '  <div class="gcard b"><div class="ge">📊</div><div class="gh">3 · Data analysis</div><div class="gt">2–3 charts that carry the argument, each with a written insight and a hand-verified number.</div></div>\n'
 '  <div class="gcard b"><div class="ge">📣</div><div class="gh">4 · Comms package</div><div class="gt">Two of: internal email · public FAQ · fact sheet — plus three reusable prompt templates.</div></div>\n'
 '</div>\n'
 '<div class="keyline b">Every deliverable is <b>draft → verify → refine</b> — the loop from Days 1 and 2.</div>', 'deliv'))

# 10 · teams & scenarios
S.append(pad(
 '<h2 class="demo-h sm b">Seven teams, <span class="hl">seven scenarios</span></h2>\n'
 '<div class="anchor b">Teams of two. Each team draws a different scenario on the same fictional portfolio — the data you have been verifying all week.</div>\n'
 '<div class="oc-list">\n'
 + ocitem('<b>S1</b> · The Contractor Turnaround — <i>Facilities</i>') + '\n'
 + ocitem('<b>S2</b> · The Cost Control Programme — <i>Finance</i>') + '\n'
 + ocitem('<b>S3</b> · The Upper-Floor Push — <i>Leasing</i>') + '\n'
 + ocitem('<b>S4</b> · The Hiring Sprint — <i>HR</i>') + '\n'
 + ocitem('<b>S5</b> · The Engagement Turnaround — <i>HR · People</i>') + '\n'
 + ocitem('<b>S6</b> · The Tenant Confidence Campaign — <i>Communications</i>') + '\n'
 + ocitem('<b>S7</b> · The Launch Readiness Plan — <i>Operations</i>') + '\n'
 + '</div>\n<div class="keyline b">Full briefs, data pointers and checklists are in the <b>Day 3 lab</b>.</div>', 'teams'))

# 11 · how the build runs
S.append(pad(
 '<div class="topic-eyebrow b">The clock</div>\n'
 '<h2 class="demo-h sm b">How the build runs</h2>\n'
 '<div class="road b">\n'
 + ritem('T1', 'Phase 0 — plan · 10 min', 'Scenario, data, roles. No tools open yet.') + '\n'
 + ritem('T2', 'Executive briefing · 35 min', 'One page, six sections, every number verified.') + '\n'
 + ritem('T3', 'Stakeholder deck · 35 min', '5–6 slides — then the break, at 10:50.') + '\n'
 + ritem('T4', 'Data analysis · 25 min', '2–3 charts with insights, dropped into the deck.') + '\n'
 + ritem('T5', 'Comms package · 15 min', 'Two items plus three prompt templates.') + '\n'
 + ritem('T6', 'Assemble &amp; rehearse · 5 min', 'One run-through, out loud, against the clock.') + '\n'
 + '</div>\n<div class="keyline b">Builder and verifier on every deliverable. <b>Swap roles as you go.</b></div>', 'flow'))

# 12 · section 03
S.append(sec('sec3', '03', 'The Build'))

# 13–19 · lab slides + break
S.append(labslide('lt1', 10, 'Lab', 'Lab T1 — Phase 0: Choose &amp; Plan', '10 minutes · in the Day 3 lab', [
 ('Find your team’s scenario in the lab', 'S1–S7 — assigned by Ali. Read it together, twice.'),
 ('Download your team\u2019s scenario workbook', 'One file, everything you need — and one planted inconsistency hiding between its sheets.'),
 ('Split the roles', 'For every deliverable: one builder, one verifier. Swap as you go.'),
 ('Agree the order and who presents what', 'Write it in the capture box — that is your plan of record.')], 600, 1))

S.append(labslide('lt2', 35, 'Lab', 'Lab T2 — Deliverable 1: Executive Briefing', '35 minutes · in the Day 3 lab', [
 ('Attach your data to a new Claude chat', 'Keep this one conversation for the whole capstone — the context compounds.'),
 ('Write a full CTFT prompt for the one-pager', 'Six sections: situation, findings, recommendation, implementation, outcomes, next steps.'),
 ('Verify every number against the source', 'The verifier owns this pass. Totals get re-added by hand.'),
 ('Cut it to one page', 'Recommendation near the top. Ninety seconds to read.')], 2100, 2))

S.append(labslide('lt3', 35, 'Lab', 'Lab T3 — Deliverable 2: Stakeholder Deck', '35 minutes · in the Day 3 lab', [
 ('Pick your tool — Claude Design or Gamma', 'You compared them yesterday. One sentence on why.'),
 ('Build 5–6 slides from the briefing', 'Same conversation, so Claude keeps your context.'),
 ('Check every figure on every slide', 'A wrong number in a deck travels fastest.'),
 ('Fix at least one slide by hand', 'Order, emphasis, or a chart that says it better.')], 2100, 3))

S.append('<div class="slide" id="break1" data-min="10">\n'
 '<div class="bg-grid"></div><div class="blob b1"></div><div class="blob b2"></div><div class="brkslide">\n'
 '  <div class="bs-eye">Break</div>\n  <div class="bs-h">Stretch and Reset</div>\n'
 '  <div class="brk-clock">10:00</div>\n  <div class="bs-sub">10 minutes — back on time, please</div>\n'
 '</div>\n</div>\n')

S.append(labslide('lt4', 25, 'Lab', 'Lab T4 — Deliverable 3: Data &amp; Visualisations', '25 minutes · in the Day 3 lab', [
 ('Pick the 2–3 claims your initiative stands on', 'Each claim gets exactly one chart. No decoration.'),
 ('Build each chart, with the numbers shown', 'Ask Claude to show the working behind every chart.'),
 ('Verify one number per chart by hand', 'The verifier recalculates it straight from the sheet.'),
 ('One insight sentence per chart, into the deck', 'The chart shows it; the sentence says why it matters.')], 1500, 4))

S.append(labslide('lt5', 15, 'Lab', 'Lab T5 — Deliverable 4: Communication Package', '15 minutes · in the Day 3 lab', [
 ('Choose two items for your audience', 'Internal email · public FAQ · fact sheet — pick the two your scenario needs.'),
 ('Generate both with full CTFT prompts', 'Same facts as the briefing. No new claims.'),
 ('Cross-check the package', 'Briefing, deck and comms must tell one story.'),
 ('Bank three prompt templates', 'With [PLACEHOLDERS] — straight into yesterday’s library.')], 900, 5))

S.append(labslide('lt6', 5, 'Lab', 'Lab T6 — Assemble &amp; Rehearse', '5 minutes · then we present', [
 ('Assemble the package', 'Briefing → deck (charts in) → comms. One story.'),
 ('Run the pitch once, out loud', 'Against the clock. Six minutes, no restarts.'),
 ('Cut what broke the six minutes', 'Cutting is the last skill of the workshop.'),
 ('Prepare for “how do you know?”', 'Have the source ready for your three biggest claims.')], 300, 6))

# 20 · section 04
S.append(sec('sec4', '04', 'Present'))

# 21 · running order
S.append(pad(
 '<div class="topic-eyebrow b">The pitch</div>\n'
 '<h2 class="demo-h sm b">Six minutes, <span class="hl">one question</span></h2>\n'
 '<div class="oc-list">\n'
 + ocitem('<b>Title &amp; team</b> — who you are, which scenario (20 seconds)') + '\n'
 + ocitem('<b>The problem</b> — what the data says is wrong (1 minute)') + '\n'
 + ocitem('<b>The evidence</b> — your charts, your verified numbers (1½ minutes)') + '\n'
 + ocitem('<b>The recommendation</b> — the initiative, said plainly (1 minute)') + '\n'
 + ocitem('<b>Implementation &amp; cost</b> — how, who, what it takes (1½ minutes)') + '\n'
 + ocitem('<b>Next steps</b> — the first three moves (30 seconds)') + '\n'
 + '</div>\n'
 '<div class="exrow b"><button class="ex-go" onclick="exStart(360)">▶ Start 6:00</button><span class="tsnote">Per team · hard stop</span></div>',
 'order', extra=' data-exmin="6"'))

# 22 · rubric
S.append(pad(
 '<h2 class="demo-h sm b">What good looks like</h2>\n'
 '<div class="oc-list">\n'
 + ocitem('Every number is <b>traceable to the data</b> — and someone on the team re-checked it') + '\n'
 + ocitem('The <b>recommendation leads</b>; detail follows it, not the other way round') + '\n'
 + ocitem('The package is <b>consistent</b> — briefing, deck and comms tell one story') + '\n'
 + ocitem('You can answer <b>“how do you know?”</b> for any claim, without opening a laptop') + '\n'
 + '</div>\n<div class="keyline b">Notice what is not on the list: <b>polish.</b> Verified beats beautiful.</div>', 'rubric'))

# 23 · section 05
S.append(sec('sec5', '05', 'Certification'))

# 24 · certificates
S.append(pad(
 '<div class="rv-emoji b">🎓</div>\n'
 '<h2 class="demo-h b">Certificates <span class="hl">&amp; the photo</span></h2>\n'
 '<div class="anchor b">Certificates of completion for AI in Workflow for Professionals — three days, from first prompt to a full implementation package. Then the group photo.</div>\n'
 '<div class="keyline b">Prompt it. Produce it. <b>Prove it.</b></div>', 'cert'))

# 25 · wrap
S.append(pad(
 '<div class="topic-eyebrow b">You leave with:</div>\n'
 '<h2 class="demo-h sm b">Three things that <span class="hl">go back to work with you.</span></h2>\n'
 '<div class="oc-list">\n'
 + ocitem('A <b>tested workflow</b> — brief to finished package, under a deadline, verified throughout') + '\n'
 + ocitem('A <b>prompt library</b> built around your own department’s work') + '\n'
 + ocitem('A <b>team that has done it once</b> — the second time is Sunday morning at your desk') + '\n'
 + '</div>\n'
 '<div class="keyline b">The tool was already on your desk. <b>Now so is the skill.</b></div>', 'close'))

# 26 · end
S.append('''<div class="slide" id="end">
<div class="cv2-bg"><div class="cv2-r1"></div><div class="cv2-r3"></div><div class="cv2-wash"></div></div>
<div class="bg-grid"></div><div class="cv2-vig"></div>
<div class="cv2">
  <div class="cv2-pill"><span class="dot"></span> End of the programme</div>
  <h1 class="cv2-title" style="margin-top:26px"><span class="cv2-t1">Go build</span> <span class="cv2-t2">on Sunday.</span></h1>
  <p class="cv2-sub">AI in Workflow for Professionals — CODED × Alshaya · Kuwait</p>
  <div class="cv2-meta"><span class="cv2-mi"><svg viewBox="0 0 24 24"><path d="M4 12l5 5L20 6"/></svg> Three days · certificate in hand</span></div>
</div>
</div>
''')

out = head + body_start + '\n'.join(S) + '\n\n' + tail
(SITE / 'coded-alshaya-day-3-deck.html').write_text(out)

ids = re.findall(r'<div class="slide(?: active)?" id="([^"]+)"', out)
print('slides:', len(ids), '| titles:', len(TITLES), '| match:', len(ids) == len(TITLES))
print(ids)

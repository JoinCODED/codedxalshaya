# -*- coding: utf-8 -*-
"""Build the Alshaya Day 2 deck by splicing the gold-standard KIBS deck:
   CSS + presenter JS taken verbatim, Day-2-specific demo JS removed,
   content written from the supplied Day 1 markdown + instructor revisions."""
import re, json

EX    = "/Users/ayaalsaqaf/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/46c4e867-24f6-4e25-8db5-adecbebe4172/c097c4a3-d3ad-45b5-8472-60354fdb96eb/skills/workshop-builder/references/examples/deck.html"
LOGOF = "/Users/ayaalsaqaf/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/46c4e867-24f6-4e25-8db5-adecbebe4172/c097c4a3-d3ad-45b5-8472-60354fdb96eb/skills/workshop-builder/assets/coded-logo.txt"
OUT   = "/Users/ayaalsaqaf/codedxalshaya/site/coded-alshaya-day-2-deck.html"

src = open(EX).read()
_blocks = re.findall(r"<style>(.*?)</style>", src, re.S)
assert len(_blocks) == 2, f"expected 2 style blocks, got {len(_blocks)}"
CSS, CSS_BREAK = _blocks[0], _blocks[1]
LOGO = open(LOGOF).read().strip()

CSS_ADD = """
/* ===== Alshaya Day 1 additions — theme tokens only, no new colours ===== */
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:20px;max-width:1120px;}
@media(max-width:820px){.cmp{grid-template-columns:1fr;}}
.cmp-col{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012));
  border:1px solid var(--w1);border-radius:14px;padding:20px 22px;}
.cmp-col.good{border-color:rgba(200,50,74,.34);background:linear-gradient(180deg,rgba(200,50,74,.10),rgba(200,50,74,.02));}
.cmp-col .cl{font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;font-weight:700;color:var(--w5);margin-bottom:11px;}
.cmp-col.good .cl{color:var(--rose);}
.cmp-col .cr{font-size:clamp(15px,1.35vw,19px);line-height:1.5;color:var(--w8);}
.cmp-col .cr b{color:var(--w);font-weight:700;}
.cmp-foot{margin-top:16px;font-size:clamp(14px,1.2vw,17px);color:var(--w6);max-width:1060px;line-height:1.5;}
.cmp-foot b{color:var(--rose);}

.gcards{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:24px;max-width:1140px;}
.gcards.three{grid-template-columns:repeat(3,1fr);max-width:1080px;}
@media(max-width:900px){.gcards.three{grid-template-columns:1fr;}}
@media(max-width:900px){.gcards{grid-template-columns:repeat(2,1fr);}}
@media(max-width:560px){.gcards{grid-template-columns:1fr;}}
.gcard{background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012));
  border:1px solid var(--w1);border-radius:14px;padding:22px 18px;}
.gcard .ge{font-size:30px;line-height:1;margin-bottom:12px;}
.gcard .gh{font-size:17px;font-weight:800;letter-spacing:-.3px;color:#fff;margin-bottom:7px;}
.gcard .gt{font-size:13.5px;line-height:1.45;color:var(--w6);}

/* model cards */
.models{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:24px;max-width:1180px;}
@media(max-width:900px){.models{grid-template-columns:repeat(2,1fr);}}
@media(max-width:560px){.models{grid-template-columns:1fr;}}
.mcard{position:relative;background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012));
  border:1px solid var(--w1);border-radius:14px;padding:20px 18px;}
.mcard.pick{border-color:var(--rose);background:linear-gradient(180deg,rgba(200,50,74,.15),rgba(200,50,74,.03));
  box-shadow:0 0 0 1px rgba(200,50,74,.2);}
.mcard .mname{font-size:19px;font-weight:800;letter-spacing:-.3px;color:#fff;}
.mcard .mmaker{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--w4);margin-top:5px;}
.mcard .mdesc{font-size:13.5px;line-height:1.5;color:var(--w6);margin-top:12px;}
.mcard .mtag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:9.5px;font-weight:700;
  letter-spacing:.16em;text-transform:uppercase;color:#fff;background:var(--crimson);border-radius:20px;padding:5px 11px;}

/* bad / good example pairs */
.exs{margin-top:20px;display:flex;flex-direction:column;gap:10px;max-width:1080px;}
.exline{display:flex;gap:14px;align-items:flex-start;border-radius:12px;padding:14px 18px;
  font-size:clamp(14px,1.25vw,17.5px);line-height:1.48;}
.exline .xm{font-family:var(--mono);font-weight:700;font-size:15px;flex:none;line-height:1.4;}
.exline.bad{background:var(--w06);border:1px solid var(--w1);color:var(--w5);}
.exline.bad .xm{color:var(--w4);}
.exline.good{background:rgba(200,50,74,.10);border:1px solid rgba(200,50,74,.32);color:var(--w9);}
.exline.good .xm{color:var(--rose);}
.exline b{color:#fff;font-weight:700;}

/* live task capture */
.taskcap{position:relative;margin-top:30px;width:min(780px,92%);}
.taskrow{display:flex;gap:10px;}
.taskrow input{flex:1;min-width:0;background:var(--base);border:1.5px solid var(--w1);color:#fff;
  border-radius:12px;padding:15px 17px;font:600 16px/1.2 var(--mf);}
.taskrow input::placeholder{color:var(--w3);}
.taskrow input:focus{outline:none;border-color:var(--crimson);}
.taskrow button{flex:none;background:linear-gradient(180deg,var(--crimson),var(--mid));color:#fff;border:none;
  border-radius:12px;padding:0 24px;font:800 14px/1 var(--mf);cursor:pointer;transition:transform .14s;}
.taskrow button:hover{transform:translateY(-2px);}
.taskchips{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-top:22px;}
.taskchip{background:rgba(200,50,74,.13);border:1px solid rgba(200,50,74,.36);color:#fff;border-radius:999px;
  padding:11px 19px;font-size:clamp(15px,1.3vw,18px);font-weight:600;
  animation:taskPop .42s cubic-bezier(.2,.9,.3,1.4) both;}
@keyframes taskPop{from{opacity:0;transform:scale(.7) translateY(12px)}to{opacity:1;transform:none}}
.taskempty{margin-top:20px;font-family:var(--mono);font-size:11.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--w3);}
.taskclear{margin-top:18px;background:none;border:none;color:var(--w4);font:700 10.5px/1 var(--mono);
  letter-spacing:.18em;text-transform:uppercase;cursor:pointer;}
.taskclear:hover{color:var(--w7);}

/* describe-and-draw shape */
.shapestage{position:relative;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 5vw;z-index:2;}
.shapebox{position:relative;margin-top:22px;display:flex;flex-direction:column;align-items:center;}
.shapebtn{background:linear-gradient(180deg,var(--crimson),var(--mid));color:#fff;border:none;border-radius:12px;
  padding:14px 26px;font:800 14px/1 var(--mf);cursor:pointer;transition:transform .14s;}
.shapebtn:hover{transform:translateY(-2px);}
.shapewrap{max-height:0;overflow:hidden;opacity:0;transition:max-height .5s ease,opacity .4s ease;}
.shapewrap.on{max-height:72vh;opacity:1;margin-top:22px;}
.shapewrap svg{height:min(560px,58vh);width:auto;max-width:88vw;stroke:var(--w7);fill:none;
  stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;}
.shapewrap .acc{stroke:var(--rose);}
.shapenote{margin-top:14px;font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--w4);text-align:center;}

.secwrap{position:relative;height:100%;display:flex;flex-direction:column;align-items:center;
  justify-content:center;text-align:center;padding:0 6vw;z-index:2;}
.secnum{font-family:var(--mono);font-size:clamp(64px,11vw,150px);font-weight:700;line-height:1;
  color:transparent;-webkit-text-stroke:1.5px rgba(200,50,74,.42);margin-bottom:6px;}
.sech{font-size:clamp(32px,5vw,68px);font-weight:900;letter-spacing:-2px;line-height:1.04;color:#fff;}
.secrule{width:70px;height:2px;background:var(--crimson);margin:24px auto 0;}

.rv-emoji{font-size:clamp(38px,5vw,62px);line-height:1;margin-bottom:16px;}

.brkslide{position:relative;height:100%;display:flex;flex-direction:column;align-items:center;
  justify-content:center;text-align:center;z-index:2;}
.brkslide .bs-eye{font-family:var(--mono);font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--rose-lt);margin-bottom:16px;}
.brkslide .bs-h{font-size:clamp(30px,4.4vw,56px);font-weight:900;letter-spacing:-1.6px;color:#fff;}
.brkslide .brk-clock{font-family:var(--mono);font-size:clamp(48px,8vw,104px);font-weight:700;
  color:var(--rose);margin-top:22px;letter-spacing:-2px;font-variant-numeric:tabular-nums;}
.brkslide .bs-sub{margin-top:14px;font-size:15px;color:var(--w5);font-family:var(--mono);letter-spacing:.06em;}

.tsnote{margin-top:20px;display:inline-flex;align-items:center;gap:9px;font-family:var(--mono);
  font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--w5);
  background:var(--w06);border:1px solid var(--w1);border-radius:20px;padding:7px 15px;}
.caution{border-color:rgba(233,196,106,.42)!important;background:linear-gradient(135deg,rgba(233,196,106,.10),rgba(233,196,106,.02))!important;border-left:3px solid #E9C46A!important;}
.caution .al{color:#E9C46A!important;}
/* Decorative blur glows sit outside the slide box (b2 is bottom:-180px), which makes every
   slide 180px scrollable — a stray trackpad nudge shifts the slide mid-presentation.
   They are purely decorative and viewport-scale, so anchor them to the viewport instead:
   identical rendering, zero contribution to slide scroll height. */
.slide > .blob{position:fixed;}

/* pills are inline elements inside a flex column — stop them stretching full width */
.slide-pad > .bridge-tag,
.slide-pad > .topic-tab,
.slide-pad > .topic-eyebrow,
.slide-pad > .rv-emoji{align-self:flex-start;}
"""

# ------------------------------------------------------------------ helpers
def pad(inner, cls=""):
    return ('<div class="bg-grid"></div><div class="blob b1"></div><div class="blob b2"></div>'
            f'<div class="slide-pad {cls}">\n{inner}\n</div>')

def reveal(emoji, heading, body, footer, caution=False, extra=""):
    e  = f'<div class="rv-emoji b">{emoji}</div>' if emoji else ''
    cz = ' caution' if caution else ''
    f  = f'<div class="keyline b">{footer}</div>' if footer else ''
    return pad(f'{e}<h2 class="demo-h b">{heading}</h2>\n'
               f'<div class="anchor b{cz}">{body}</div>\n{extra}{f}')

def comparison(header, llab, lres, rlab, rres, footer=""):
    f = f'<div class="cmp-foot b">{footer}</div>' if footer else ''
    return pad(f'<div class="bridge-tag tech b">Compare</div>\n'
               f'<h2 class="demo-h sm b">{header}</h2>\n<div class="cmp">\n'
               f'  <div class="cmp-col b"><div class="cl">{llab}</div><div class="cr">{lres}</div></div>\n'
               f'  <div class="cmp-col good b"><div class="cl">{rlab}</div><div class="cr">{rres}</div></div>\n'
               f'</div>\n{f}')

def section(num, heading):
    return ('<div class="bg-grid"></div><div class="blob b1"></div><div class="blob b2"></div>'
            f'<div class="secwrap">\n  <div class="secnum b">{num}</div>\n'
            f'  <div class="sech b">{heading}</div>\n  <div class="secrule b"></div>\n</div>')

def question(eyebrow, text, extra=""):
    return ('<div class="bg-grid"></div><div class="ph-stage"><div class="ph-glow"></div>\n'
            f'  <div class="ph-eyebrow b">{eyebrow}</div>\n'
            f'  <div class="ph-q b">{text}</div>\n{extra}</div>')

def steps(pill, heading, sub, items, sheet=None):
    rows = "\n".join(
        f'    <div class="ritem b"><div class="rn">{i+1}</div><div>'
        f'<div class="rt">{t}</div><div class="rd">{d}</div></div></div>'
        for i, (t, d) in enumerate(items))
    s = f'<div><span class="tsnote b">{sheet}</span></div>' if sheet else ''
    return pad(f'<div class="topic-tab b">{pill}</div>\n<h2 class="demo-h sm b">{heading}</h2>\n'
               f'<p class="lead b">{sub}</p>\n<div class="road b">\n{rows}\n</div>\n{s}')

def framework(pill, heading, items):
    p = f'<div class="topic-eyebrow b">{pill}</div>\n' if pill else ''
    rows = "\n".join('    <div class="oc-item b"><div class="oc-check">'
                     '<svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"></path></svg></div>'
                     f'<div class="oc-txt">{t}</div></div>' for t in items)
    return pad(f'{p}<h2 class="demo-h sm b">{heading}</h2>\n<div class="oc-list">\n{rows}\n</div>')

def gridcards(heading, items, note="", lead=""):
    cards = "\n".join(f'  <div class="gcard b"><div class="ge">{e}</div>'
                      f'<div class="gh">{h}</div><div class="gt">{t}</div></div>'
                      for e, h, t in items)
    l = f'<p class="lead b">{lead}</p>\n' if lead else ''
    n = f'<div class="cmp-foot b">{note}</div>' if note else ''
    return pad(f'<h2 class="demo-h sm b">{heading}</h2>\n{l}<div class="gcards">\n{cards}\n</div>\n{n}')

def badgood(heading, why, pairs, footer):
    rows = "\n".join(
        f'  <div class="exline bad b"><span class="xm">✗</span><div>{b}</div></div>\n'
        f'  <div class="exline good b"><span class="xm">✓</span><div>{g}</div></div>'
        for b, g in pairs)
    return pad(f'<h2 class="demo-h b">{heading}</h2>\n<div class="anchor b">{why}</div>\n'
               f'<div class="exs">\n{rows}\n</div>\n<div class="keyline b">{footer}</div>')

def brk(heading, minutes):
    return ('<div class="bg-grid"></div><div class="blob b1"></div><div class="blob b2"></div>'
            '<div class="brkslide">\n  <div class="bs-eye">Break</div>\n'
            f'  <div class="bs-h">{heading}</div>\n  <div class="brk-clock">10:00</div>\n'
            f'  <div class="bs-sub">{minutes} minutes — back on time, please</div>\n</div>')

# ------------------------------------------------------------------ slides
S = []
def add(sid, label, html, attrs=""):
    S.append((sid, label, html, attrs))

def demo(emoji, heading, sub, watch):
    rows = "\n".join(f'  <div class="exline good b"><span class="xm">◆</span><div>{w}</div></div>'
                     for w in watch)
    return pad(f'<div class="rv-emoji b">{emoji}</div>\n'
               f'<div class="topic-tab b">Live demo</div>\n'
               f'<h2 class="demo-h sm b">{heading}</h2>\n'
               f'<p class="lead b">{sub}</p>\n'
               f'<div class="exs">\n{rows}\n</div>')

# --- S0 cover
add("cover", "Title",
 '<div class="cv2-bg"><div class="cv2-r1"></div><div class="cv2-r2"></div><div class="cv2-r3"></div>'
 '<div class="cv2-b1"></div><div class="cv2-wash"></div></div>\n'
 '<div class="bg-grid"></div><div class="cv2-vig"></div>\n<div class="cv2">\n'
 '  <div class="cv2-pill"><span class="dot"></span> CODED × Alshaya · Kuwait</div>\n'
 f'  <div class="cv2-logos"><img src="{LOGO}" alt="CODED"><span class="lx">×</span>'
 '<span style="font-size:19px;font-weight:800;letter-spacing:.15em;color:#fff">ALSHAYA</span></div>\n'
 '  <h1 class="cv2-title"><span class="cv2-t1">From Blank Page</span><br>'
 '<span class="cv2-t2">to Finished Deck</span></h1>\n'
 '  <p class="cv2-sub">Day 2 — Presentations, data analysis, and the prompt library you keep using '
 'after the workshop ends.</p>\n  <div class="cv2-meta">\n'
 '    <span class="cv2-daybadge">DAY 2</span>\n'
 '    <span class="cv2-mi"><svg viewBox="0 0 24 24"><rect x="3" y="4.5" width="18" height="17" rx="2.5"/>'
 '<path d="M16 2.5v4M8 2.5v4M3 10h18"/></svg> Wednesday 2 September 2026</span>\n'
 '    <span class="cv2-mi"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7.5v5l3 2"/>'
 '</svg> 09:00 – 13:00</span>\n'
 '    <span class="cv2-mi"><svg viewBox="0 0 24 24"><path d="M21 10.5c0 6.5-9 12.5-9 12.5s-9-6-9-12.5a9 9 0 0118 0z"/>'
 '<circle cx="12" cy="10.5" r="3"/></svg> CODED Campus</span>\n  </div>\n'
 '  <div class="cv2-standby"><span class="pdot"></span> Ali Taqi · Alshaya &amp; Al-Injaz</div>\n'
 '  <div class="cv2-cue">press <kbd>→</kbd> to begin · <kbd>?</kbd> for controls</div>\n</div>')

# --- S1 callback
add("s1", "Callback to Day 1", reveal("", 'Callback: yesterday\'s <span class="hl">CTFT prompt</span>',
 'You wrote Context, Task, Format and Tone for one real document. Today you reuse that exact structure '
 'twice more — once to build a presentation, once to question a set of data.',
 'Same framework. <b>Two new outputs.</b>'))

# --- S2 wow
add("s2", "Cold-open", pad(
 '<div class="topic-tab b">Day 2</div>\n'
 '<h2 class="demo-h b">A full presentation used to take <span class="hl">two to three hours.</span></h2>\n'
 '<p class="lead b">Today you\'ll build one before the first break.</p>'))

# --- S3 section 01
add("sec1", "01 · Presentations", section("01", "AI for Presentations"))

# --- S4
add("s4", "The problem", reveal("", "The presentation problem",
 'Blank slides, no structure, no design skill, and no time. Most people spend two to three hours '
 'building one deck — and most of that goes on layout, not on thinking.',
 'That time comes straight out of your real workday.'))

# --- S5 tools
add("s5", "The tools", pad(
 '<div class="bridge-tag tech b">The landscape</div>\n'
 '<h2 class="demo-h sm b">Four ways to let AI build the deck</h2>\n'
 '<p class="lead b">We will use the first two today, so you can feel the difference between them.</p>\n'
 '<div class="models">\n'
 '  <div class="mcard pick b"><div class="mname">Claude Design</div><div class="mmaker">Anthropic</div>'
 '<div class="mdesc">Describe the deck inside the chat you are already working in. You get an editable '
 'visual canvas — click any element, change it, export it. Your context is already there.</div>'
 '<span class="mtag">We use this</span></div>\n'
 '  <div class="mcard pick b"><div class="mname">Gamma</div><div class="mmaker">Gamma.app</div>'
 '<div class="mdesc">A tool built only for presentations. Type a prompt, pick a theme, get a designed '
 'deck — then export it to PowerPoint or PDF.</div><span class="mtag">We use this</span></div>\n'
 '  <div class="mcard b"><div class="mname">Beautiful.ai</div><div class="mmaker">Beautiful.ai</div>'
 '<div class="mdesc">Template-led. The layout adjusts itself as you add content, so slides stay tidy '
 'without you nudging boxes around.</div></div>\n'
 '  <div class="mcard b"><div class="mname">Canva AI</div><div class="mmaker">Canva</div>'
 '<div class="mdesc">Content and design in one place, with a very large library of images and brand '
 'assets behind it.</div></div>\n'
 '</div>\n'
 '<div class="keyline b">Different tools, one skill. <b>The prompt is what carries across.</b></div>'))

# --- S6 hybrid
add("s6", "The hybrid approach", reveal("", 'The <span class="hl">hybrid</span> approach',
 'Use AI to generate the outline and the first draft. Then add your own expertise, your own numbers, '
 'and your own judgment before anyone else sees it.',
 'AI drafts. <b>You own the version that gets presented.</b>'))

# --- S7 demo · Claude Design
add("s7", "Demo · Claude Design", demo("🎨", "Live demo — Claude Design",
 "Same chat, same context. Describe the deck and watch it become a canvas you can actually edit.",
 ["It already knows what we have been discussing — no re-explaining the situation",
  "Click any element to change it, rather than regenerating the whole slide",
  "Watch how a vague instruction produces a vague layout — the Day 1 lesson, again"]))

# --- S8 demo · Gamma
add("s8", "Demo · Gamma", demo("⚡", "Live demo — Gamma",
 "A tool that does one thing. Prompt in, themed deck out, ready to export.",
 ["One prompt produces a full deck with a theme applied, in well under a minute",
  "Swapping the theme restyles every slide at once",
  "Export to PowerPoint — and notice what needs fixing after the export"]))

# --- S9 framework
add("s9", "Prompt anatomy", framework("Framework", "What goes into a presentation prompt", [
 "<b>Type and length</b> — “a 5-slide presentation”",
 "<b>Topic and key points</b> — the specific ground it must cover",
 "<b>Audience and purpose</b> — who is in the room, and what you need from them",
 "<b>Tone</b> — professional, persuasive, plain",
]))

# --- S10 comparison
add("s10", "Weak vs strong", comparison("Weak prompt vs. strong prompt",
 "Weak", '“Make a presentation about maintenance.”',
 "Strong", '“Create a 5-slide presentation for property managers about the new maintenance request '
           'system. Cover the problem, the new process, staff responsibilities, and the launch date. '
           'Use a professional tone.”',
 "That is CTFT again, wearing a different hat. <b>Context, task, format, tone.</b>"))

# --- S11 exercise
add("s11", "Exercise 1", steps("Exercise", "Exercise: generate a presentation", "15 minutes", [
 ("Pick a real topic", "Something you would actually present at work this month."),
 ("Write a full prompt", "Type and length, topic and key points, audience and purpose, tone."),
 ("Build it in both tools", "Claude Design first, then the same prompt in Gamma."),
 ("Check every slide", "Look for anything wrong, missing, or out of order."),
], "Task Sheet 1"))

add("break1", "Break 1", brk("Stretch and Reset", 10), ' data-min="10"')

# --- S12 section 02
add("sec2", "02 · Review", section("02", "Presentation Review &amp; Advanced Features"))

# --- S13 question with live capture
add("s13", "Group discussion", question(
 "Group discussion",
 'What <span class="hl">surprised</span> you about the deck AI built for you?',
 extra='''  <div class="taskcap b">
    <div class="taskrow">
      <input id="taskInput" type="text" autocomplete="off" spellcheck="false"
             placeholder="Type what they say, then press Enter…">
      <button id="taskAdd" type="button">Add</button>
    </div>
    <div class="taskchips" id="taskList"></div>
    <div class="taskempty" id="taskEmpty">one strength and one limitation from each table</div>
    <button class="taskclear" id="taskClear" type="button">Clear all</button>
  </div>'''))

# --- S14 when to use what
add("s14", "When to use what", pad(
 '<div class="bridge-tag tech b">Choosing</div>\n'
 '<h2 class="demo-h sm b">Which one, when?</h2>\n'
 '<div class="gcards three">\n'
 '  <div class="gcard b"><div class="ge">🎨</div><div class="gh">Claude Design</div>'
 '<div class="gt">You are already deep in the content with Claude, and you want to shape the deck '
 'visually without leaving the conversation.</div></div>\n'
 '  <div class="gcard b"><div class="ge">⚡</div><div class="gh">Gamma</div>'
 '<div class="gt">You want a themed, presentable deck fast — and you need it out as PowerPoint or '
 'PDF at the end.</div></div>\n'
 '  <div class="gcard b"><div class="ge">📊</div><div class="gh">PowerPoint</div>'
 '<div class="gt">Company template, exact control over every element, or highly technical detail '
 'that must sit exactly where you put it.</div></div>\n'
 '</div>\n'
 '<div class="keyline b">The honest rule: <b>AI for the first draft, your own tool for the final one</b> — '
 'whenever the deck really matters.</div>'))

# --- S15 advanced features
add("s15", "Advanced features", pad(
 '<h2 class="demo-h sm b">Features worth knowing</h2>\n'
 '<div class="gcards">\n'
 '  <div class="gcard b"><div class="ge">📥</div><div class="gh">Import</div>'
 '<div class="gt">Paste in an existing outline or document and let it structure the slides for you.</div></div>\n'
 '  <div class="gcard b"><div class="ge">✏️</div><div class="gh">AI rewrite</div>'
 '<div class="gt">Select one slide and ask for shorter, simpler, or more detail — without touching the rest.</div></div>\n'
 '  <div class="gcard b"><div class="ge">🎭</div><div class="gh">Themes</div>'
 '<div class="gt">Restyle the whole deck with one click when the first look is not right.</div></div>\n'
 '  <div class="gcard b"><div class="ge">📤</div><div class="gh">Export</div>'
 '<div class="gt">Out to PowerPoint or PDF. Always check the export — spacing and fonts can shift.</div></div>\n'
 '</div>'))

# --- S16 privacy
add("s16", "Before real data", reveal("🔒", "Before you put real company data in a deck",
 '<span class="al">Caution</span>Do not paste tenant, financial or contract data into a public AI tool. '
 'Build the structure with sample data first, then add the real numbers yourself, afterwards, in your '
 'own file.',
 'Same rule as Day 1. <b>A new tool does not change it.</b>', caution=True))

add("break2", "Break 2", brk("Stretch and Reset", 10), ' data-min="10"')

# --- S17 section 03
add("sec3", "03 · Data", section("03", "Data Analysis With AI"))

# --- S18
add("s18", "The data problem", reveal("", "The data analysis problem",
 'A spreadsheet with 200 rows lands in your inbox. No time to clean it, chart it, or work out what it '
 'means before the meeting starts.',
 'Most people spend more time <b>preparing</b> data than <b>analysing</b> it.'))

# --- S19 can / cannot
add("s19", "Can and cannot", comparison("What AI can and cannot do with data",
 "AI cannot", "Know whether a result is good or bad <i>for your business</i>, understand your "
              "organisation's context, or fix data that was wrong before it arrived",
 "AI can", "Calculate statistics, clean and sort, spot patterns and outliers, build charts, and draft "
           "the explanation",
 "It will also do arithmetic confidently and occasionally get it wrong. <b>Spot-check every number that matters.</b>"))

# --- S20 best practice
add("s20", "Best practice", framework("Framework", "Three rules for analysing data with Claude", [
 "<b>One clear question at a time</b> — not five at once",
 "<b>Spot-check every calculation</b> — by hand, on the number that matters most",
 "<b>Ask it to show its working</b> — “list every figure you used and where it came from”",
]))

# --- S21 exercise survey
add("s21", "Exercise 2", steps("Exercise", "Exercise: employee satisfaction survey", "20 minutes", [
 ("Paste the sample survey into Claude", "12 responses across four departments. Sample data, not real records."),
 ("Ask three questions", "One CTFT prompt each — averages, gaps between scores, the biggest concern."),
 ("Recalculate one average by hand", "Pick one number Claude gave you and check it yourself."),
 ("Note whether it matched", "Write down what you checked and what you found."),
], "Task Sheet 2"))

add("break3", "Break 3", brk("Stretch and Reset", 10), ' data-min="10"')

# --- S22 section 04
add("sec4", "04 · Budget", section("04", "Budget Analysis &amp; the AI + Excel Hybrid"))

# --- S23 hybrid
add("s23", "Why hybrid", reveal("", 'Why <span class="hl">hybrid</span> beats either tool alone',
 'Claude explains what a pattern means and writes it up in plain language. Excel proves the number is '
 'actually correct. Use both, in that order.',
 'Trust, but verify. <b>Every time, no exceptions.</b>'))

# --- S24 exercise budget
add("s24", "Exercise 3", steps("Exercise", "Exercise: budget analysis", "20 minutes", [
 ("Paste the sample budget into Claude", "Five categories, planned against actual. Sample data."),
 ("Ask for the variances, ranked", "Actual minus planned, largest overspend to largest underspend."),
 ("Confirm the top variance yourself", "Recalculate it in Excel or on paper before you trust it."),
 ("Separate fact from guess", "Ask why it happened — then mark that answer as a guess until someone checks."),
], "Task Sheet 3"))

add("break4", "Break 4", brk("Stretch and Reset", 10), ' data-min="10"')

# --- S25 section 05
add("sec5", "05 · Libraries", section("05", "Prompt Libraries &amp; Your Department"))

# --- S26 why save
add("s26", "Why save prompts", reveal("", "Why save your best prompts?",
 'A prompt that worked once will work again. Save it, and next time you skip straight past the '
 'rewriting to the result.',
 'This is your <b>prompt library</b> — you started it on Day 1 without noticing.'))

# --- S27 what makes a good one
add("s27", "A good saved prompt", framework("Framework", "What makes a saved prompt worth keeping", [
 "<b>A title you will recognise later</b> — “monthly maintenance update”, not “prompt 3”",
 "<b>The full CTFT prompt</b>, with placeholders where the details change",
 "<b>A note on which tool it worked best in</b> — and what you had to fix afterwards",
]))

# --- S28 by department
add("s28", "By department", pad(
 '<h2 class="demo-h sm b">Where this lands in <span class="hl">your</span> job</h2>\n'
 '<div class="gcards">\n'
 '  <div class="gcard b"><div class="ge">👥</div><div class="gh">HR</div>'
 '<div class="gt">Onboarding letters, policy summaries, job description drafts, training announcements.</div></div>\n'
 '  <div class="gcard b"><div class="ge">💰</div><div class="gh">Finance</div>'
 '<div class="gt">Variance commentary, budget summaries, turning a table into a paragraph a board can read.</div></div>\n'
 '  <div class="gcard b"><div class="ge">🔧</div><div class="gh">Operations</div>'
 '<div class="gt">Maintenance updates, contractor briefs, schedules, incident write-ups.</div></div>\n'
 '  <div class="gcard b"><div class="ge">📣</div><div class="gh">Communications</div>'
 '<div class="gt">Tenant notices, announcements, FAQs, and the same message rewritten for three audiences.</div></div>\n'
 '</div>\n'
 '<div class="keyline b">Every one of these is <b>draft, rewrite, or summarize</b> — the three moves from yesterday.</div>'))

# --- S29 exercise library
add("s29", "Exercise 4", steps("Exercise", "Exercise: build your prompt library", "15 minutes", [
 ("Collect today's three best prompts", "The presentation, the survey analysis, the budget analysis."),
 ("Add one from your own department", "Something you will genuinely reuse next week."),
 ("Give each one a title and a note", "What it is for, and which tool it worked best in."),
 ("Save it where you will find it", "A document, a notes app, a shared drive — anywhere but your memory."),
], "Task Sheet 4"))

# --- close
add("close", "Wrap", pad(
 '<div class="topic-eyebrow b">Today you built:</div>\n'
 '<h2 class="demo-h sm b">Three things you can <span class="hl">use on Sunday.</span></h2>\n'
 '<div class="oc-list">\n'
 '    <div class="oc-item b"><div class="oc-check"><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"></path></svg></div>'
 '<div class="oc-txt">A <b>presentation</b> generated in two tools and reviewed properly</div></div>\n'
 '    <div class="oc-item b"><div class="oc-check"><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"></path></svg></div>'
 '<div class="oc-txt">Two <b>data analyses</b>, each with one number verified by hand</div></div>\n'
 '    <div class="oc-item b"><div class="oc-check"><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"></path></svg></div>'
 '<div class="oc-txt">The start of a <b>reusable prompt library</b>, built around your own job</div></div>\n'
 '</div>\n'
 '<div class="keyline b">Tomorrow: put all three days together into one implementation package.</div>'))

# --- end
add("end", "End",
 '<div class="cv2-bg"><div class="cv2-r1"></div><div class="cv2-r3"></div><div class="cv2-wash"></div></div>\n'
 '<div class="bg-grid"></div><div class="cv2-vig"></div>\n<div class="cv2">\n'
 '  <div class="cv2-pill"><span class="dot"></span> End of Day 2</div>\n'
 '  <h1 class="cv2-title" style="margin-top:26px"><span class="cv2-t1">See you</span> '
 '<span class="cv2-t2">tomorrow.</span></h1>\n'
 '  <p class="cv2-sub">Day 3 — The Implementation Capstone</p>\n'
 '  <div class="cv2-meta"><span class="cv2-mi"><svg viewBox="0 0 24 24">'
 '<rect x="3" y="4.5" width="18" height="17" rx="2.5"/><path d="M16 2.5v4M8 2.5v4M3 10h18"/></svg> '
 'Thursday 3 September 2026 · 09:00 – 13:00</span></div>\n</div>')

# ------------------------------------------------------------------ assemble
slides_html = [f'<div class="{"slide active" if i==0 else "slide"}" id="{sid}"{attrs}>\n{html}\n</div>'
               for i, (sid, _, html, attrs) in enumerate(S)]
SLIDES = "\n\n".join(slides_html)
LABELS = json.dumps([lbl for _, lbl, _, _ in S])

CHROME = """
<div id="prail-wrap"><div id="prail"></div></div>
<a class="deck-back" href="coded-alshaya-day-2.html">‹ Day 2</a>
<div id="extimer"><span class="ex-lbl">Exercise</span><span class="ex-time" id="ex-time">1:00</span></div>
<div class="nav-dots" id="nav-dots"></div>
<div class="deck-nav">
  <button class="nav-btn" onclick="prev()" aria-label="Previous">‹</button>
  <div class="nav-pos"><span class="cur" id="pos-cur">1</span><span class="tot"> / <span id="pos-tot">0</span></span></div>
  <button class="nav-btn" onclick="next()" aria-label="Next">›</button>
  <div class="nav-divider"></div>
  <button class="nav-btn fs" onclick="toggleFs()" aria-label="Fullscreen">⛶</button>
  <div class="nav-divider"></div>
  <button class="nav-btn brkbtn" onclick="openBreak()" aria-label="Break timer" title="Start a break timer">☕</button>
</div>
<div class="kbd-hint"><kbd>→</kbd> next <kbd>←</kbd> back <kbd>F</kbd> full <kbd>?</kbd> help</div>
<div class="laser" id="laser"></div>
<div class="blankscreen" id="blank"><div class="bk">screen blanked — press B to resume</div></div>
<div class="help-overlay" id="help"><div class="help-card">
  <h3>Presenter &amp; pointer controls</h3>
  <div class="help-row"><div class="keys"><kbd>→</kbd><kbd>Space</kbd><kbd>Pg Dn</kbd></div><div class="what">Next slide</div></div>
  <div class="help-row"><div class="keys"><kbd>←</kbd><kbd>Pg Up</kbd></div><div class="what">Back</div></div>
  <div class="help-row"><div class="keys"><kbd>L</kbd></div><div class="what">Laser pointer (follows the mouse)</div></div>
  <div class="help-row"><div class="keys"><kbd>B</kbd><kbd>.</kbd></div><div class="what">Blank the screen</div></div>
  <div class="help-row"><div class="keys"><kbd>F</kbd></div><div class="what">Fullscreen</div></div>
  <div class="help-row"><div class="keys"><kbd>S</kbd></div><div class="what">Sound on / off (starts off)</div></div>
  <div class="help-row"><div class="keys"><kbd>T</kbd></div><div class="what">Start 60-second exercise timer</div></div>
  <div class="help-row"><div class="keys"><kbd>?</kbd></div><div class="what">This panel</div></div>
  <div class="help-row"><div class="keys"><kbd>Esc</kbd></div><div class="what">Close / resume</div></div>
  <div class="hint">Most USB presenter remotes send Page&nbsp;Up / Page&nbsp;Down — they already drive this deck.</div>
</div></div>
<div class="break-pick" id="breakPick"><div class="bp-card">
  <div class="bp-h">☕ Start a break</div>
  <div class="bp-sub">Pick a length — the timer counts down and shows everyone the return time.</div>
  <div class="bp-chips">
    <button class="bp-chip" data-min="5">5 min</button>
    <button class="bp-chip" data-min="10">10 min</button>
    <button class="bp-chip" data-min="15">15 min</button>
    <button class="bp-chip" data-min="20">20 min</button>
    <button class="bp-chip" data-min="30">30 min</button>
  </div>
  <div class="bp-custom"><input id="bpCustom" type="number" min="1" max="180" placeholder="custom minutes"><button class="bp-go" id="bpGo">Start →</button></div>
  <button class="bp-cancel" id="bpCancel">Cancel</button>
</div></div>
<div class="break-ov" id="breakOv"><div class="bg-grid"></div><div class="blob b1"></div><div class="blob b2"></div>
  <div class="brk">
    <div class="brk-eyebrow" id="boEye">Break</div>
    <div class="brk-title">Break</div>
    <div class="brk-clock" id="boClock">10:00</div>
    <div class="brk-back" id="boBack">Back at <b>—</b></div>
    <div class="bo-cta"><button class="bo-btn" id="boAdd">+5 min</button><button class="bo-btn end" id="boEnd">End break →</button></div>
  </div>
</div>
<div class="pres-tag" id="prestag"></div>
"""

SCRIPT = r"""
var slides=[].slice.call(document.querySelectorAll('.slide'));
var total=slides.length,idx=0;
document.getElementById('pos-tot').textContent=total;
var TITLES=__LABELS__,SECS={};
for(var _i=0;_i<slides.length;_i++){if(/^sec\d+$/.test(slides[_i].id))SECS[_i]=1;}
var dc=document.getElementById('nav-dots');
for(var i=0;i<total;i++){var d=document.createElement('button');
  d.className='nav-dot'+(i===0?' active':'')+(SECS[i]?' sec':'');
  (function(n){d.onclick=function(){show(n);};})(i);
  var tip=document.createElement('span');tip.className='nav-tip';tip.textContent=(i+1)+'. '+TITLES[i];
  d.appendChild(tip);dc.appendChild(d);}
var dots=[].slice.call(dc.querySelectorAll('.nav-dot'));
function items(s){return [].slice.call(s.querySelectorAll('.b'));}
function show(n){slides[idx].classList.remove('active');if(dots[idx])dots[idx].classList.remove('active');
  idx=(n+total)%total;var s=slides[idx];s.classList.add('active');if(dots[idx])dots[idx].classList.add('active');s.scrollTop=0;
  document.getElementById('pos-cur').textContent=idx+1;
  document.body.classList.toggle('hide-brand', s.id==='cover'||s.id==='end');
  if(brkTimer){clearInterval(brkTimer);brkTimer=null;}
  if(s.id.indexOf('break')===0)startBreakCountdown(s);
  if(s.id==='drawshape')shapeHide();
  /* content shows on arrival — no extra clicks */
  [].slice.call(s.querySelectorAll('.b')).forEach(function(el){el.classList.add('shown');el.classList.add(el.classList.contains('step')?'on':'in');el.classList.remove('next-up');});
  mcReset(s);taskRender();
  var pr=document.getElementById('prail');if(pr)pr.style.width=(total>1?(idx/(total-1)*100):0)+'%';
}
function next(){if(idx<total-1)show(idx+1);}
function prev(){if(idx>0)show(idx-1);}
function toggleFs(){if(!document.fullscreenElement){document.documentElement.requestFullscreen().catch(function(){});}else{document.exitFullscreen();}}
var laserEl=document.getElementById('laser');
document.addEventListener('mousemove',function(e){if(document.body.classList.contains('laser-on')&&laserEl){laserEl.style.left=e.clientX+'px';laserEl.style.top=e.clientY+'px';}});
var tagT=null;function flashTag(t){var el=document.getElementById('prestag');if(!el)return;el.textContent=t;el.classList.add('show');if(tagT)clearTimeout(tagT);tagT=setTimeout(function(){el.classList.remove('show');},1700);}
function toggleLaser(){document.body.classList.toggle('laser-on');flashTag(document.body.classList.contains('laser-on')?'Laser ON':'Laser off');}
function toggleBlank(){var b=document.getElementById('blank');if(b)b.classList.toggle('on');}
function toggleHelp(){var h=document.getElementById('help');if(h)h.classList.toggle('on');}
function closeOverlays(){var h=document.getElementById('help');if(h)h.classList.remove('on');var b=document.getElementById('blank');if(b)b.classList.remove('on');document.body.classList.remove('laser-on');closeBreakPick();exHide();}
(function(){var h=document.getElementById('help');if(h)h.addEventListener('click',closeOverlays);var b=document.getElementById('blank');if(b)b.addEventListener('click',function(){toggleBlank();});})();
document.addEventListener('keydown',function(e){
  if(e.target.tagName==='INPUT')return;
  if(e.key==='s'||e.key==='S'){toggleSound();e.preventDefault();return;}
  if(e.key==='t'||e.key==='T'){exStart(120);e.preventDefault();return;}
  if(e.key==='l'||e.key==='L'){toggleLaser();e.preventDefault();return;}
  if(e.key==='b'||e.key==='B'||e.key==='.'){toggleBlank();e.preventDefault();return;}
  if(e.key==='?'||(e.shiftKey&&e.key==='/')){toggleHelp();e.preventDefault();return;}
  if(e.key==='Escape'){closeOverlays();e.preventDefault();return;}
  if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown'){next();e.preventDefault();}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){prev();e.preventDefault();}
  else if(e.key==='Home'){show(0);e.preventDefault();}
  else if(e.key==='End'){show(total-1);e.preventDefault();}
  else if(e.key==='f'||e.key==='F'){toggleFs();e.preventDefault();}
});
slides.forEach(function(s){s.addEventListener('click',function(e){
  if(e.target.closest('button,input,a,.mc-opt,.taskcap,.shapebox'))return;next();});});
/* ===== MC test-yourself ===== */
function mcReset(s){[].slice.call(s.querySelectorAll('.mc-opts')).forEach(function(o){o.classList.remove('done');
  [].slice.call(o.querySelectorAll('.mc-opt')).forEach(function(b){b.classList.remove('correct','wrong');});});
  [].slice.call(s.querySelectorAll('.mc-fb')).forEach(function(f){f.classList.remove('show');f.innerHTML='';});}
document.addEventListener('click',function(e){var opt=e.target.closest('.mc-opt');if(!opt)return;
  var box=opt.closest('.mc-opts');if(!box||box.classList.contains('done'))return;e.stopPropagation();
  box.classList.add('done');
  var correctBtn=box.querySelector('.mc-opt[data-k="1"]');
  if(opt.dataset.k==='1')opt.classList.add('correct');else{opt.classList.add('wrong');if(correctBtn)correctBtn.classList.add('correct');}sfx(opt.dataset.k==='1'?'correct':'wrong');
  var fb=box.parentNode.querySelector('.mc-fb');
  if(fb){fb.innerHTML='<div class="fbh">'+(opt.dataset.k==='1'?'Correct':'Not quite')+'</div><div class="fbt">'+(opt.dataset.fb||'')+'</div>';fb.classList.add('show');}
});
/* ===== live task capture (slide 3 -> echoed on slide 14) ===== */
var TASKS=[];
function esc(t){return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function taskRender(){
  var html=TASKS.map(function(t){return '<span class="taskchip">'+esc(t)+'</span>';}).join('');
  ['taskList','taskEcho'].forEach(function(id){var el=document.getElementById(id);if(el)el.innerHTML=html;});
  ['taskEmpty','taskEmpty2'].forEach(function(id){var el=document.getElementById(id);if(el)el.style.display=TASKS.length?'none':'block';});
  var c=document.getElementById('taskClear');if(c)c.style.display=TASKS.length?'inline-block':'none';
}
function taskAdd(){var i=document.getElementById('taskInput');if(!i)return;
  var v=(i.value||'').trim();if(!v)return;TASKS.push(v);i.value='';taskRender();i.focus();}
function taskClear(){TASKS=[];taskRender();}
(function(){
  var b=document.getElementById('taskAdd');if(b)b.addEventListener('click',function(e){e.stopPropagation();taskAdd();});
  var c=document.getElementById('taskClear');if(c)c.addEventListener('click',function(e){e.stopPropagation();taskClear();});
  var i=document.getElementById('taskInput');
  if(i){i.addEventListener('click',function(e){e.stopPropagation();});
        i.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();e.stopPropagation();taskAdd();}});}
})();
/* ===== describe-and-draw shape reveal ===== */
function shapeToggle(){var w=document.getElementById('shapeWrap');if(!w)return;
  w.classList.toggle('on');
  var b=document.getElementById('shapeBtn');
  if(b)b.textContent=w.classList.contains('on')?'Hide the shape':'Show the shape';}
function shapeHide(){var w=document.getElementById('shapeWrap');if(w)w.classList.remove('on');
  var b=document.getElementById('shapeBtn');if(b)b.textContent='Show the shape';}
(function(){var b=document.getElementById('shapeBtn');
  if(b)b.addEventListener('click',function(e){e.stopPropagation();shapeToggle();});})();
/* ===== sound (default off), exercise timer, break countdown ===== */
var SND={on:false,ctx:null};
function sndCtx(){if(!SND.ctx){try{SND.ctx=new (window.AudioContext||window.webkitAudioContext)();}catch(e){SND.ctx=null;}}return SND.ctx;}
function tone(freq,start,dur,type,vol){var c=sndCtx();if(!c)return;try{var o=c.createOscillator(),g=c.createGain();o.type=type||'sine';o.frequency.value=freq;o.connect(g);g.connect(c.destination);var t=c.currentTime+start;g.gain.setValueAtTime(0.0001,t);g.gain.linearRampToValueAtTime(vol||0.2,t+0.012);g.gain.exponentialRampToValueAtTime(0.0001,t+dur);o.start(t);o.stop(t+dur+0.03);}catch(e){}}
function sfx(name){if(!SND.on)return;var c=sndCtx();if(!c)return;if(c.state==='suspended'){try{c.resume();}catch(e){}}
  if(name==='correct'){tone(660,0,.12,'sine',.18);tone(990,.09,.16,'sine',.15);}
  else if(name==='wrong'){tone(170,0,.2,'sawtooth',.13);}
  else if(name==='times-up'){tone(880,0,.14,'square',.18);tone(880,.2,.14,'square',.18);tone(620,.4,.32,'square',.18);}}
function toggleSound(){SND.on=!SND.on;if(SND.on){var c=sndCtx();if(c&&c.state==='suspended'){try{c.resume();}catch(e){}}sfx('correct');}flashTag(SND.on?'Sound ON':'Sound OFF');}
var exTimer=null,exLeft=0;
function exRender(){var t=document.getElementById('ex-time');if(!t)return;var m=Math.floor(exLeft/60),s=exLeft%60;t.textContent=m+':'+(s<10?'0':'')+s;}
function exStart(sec){if(exTimer)clearInterval(exTimer);exLeft=sec;var box=document.getElementById('extimer');if(box){box.classList.add('show');box.classList.remove('warn');}var t=document.getElementById('ex-time');if(t)t.classList.remove('warn');exRender();
  exTimer=setInterval(function(){exLeft--;exRender();if(exLeft<=10){if(box)box.classList.add('warn');if(t)t.classList.add('warn');}if(exLeft<=0){clearInterval(exTimer);exTimer=null;sfx('times-up');setTimeout(function(){if(box)box.classList.remove('show','warn');},2600);}},1000);}
function exHide(){if(exTimer){clearInterval(exTimer);exTimer=null;}var box=document.getElementById('extimer');if(box)box.classList.remove('show','warn');}
var brkTimer=null;
function startBreakCountdown(s){if(brkTimer){clearInterval(brkTimer);brkTimer=null;}var clock=s.querySelector('.brk-clock');if(!clock)return;var total=(+(s.dataset.min||10))*60;
  function r(){var m=Math.floor(total/60),sec=total%60;clock.textContent=m+':'+(sec<10?'0':'')+sec;}r();
  brkTimer=setInterval(function(){total--;if(total<=0){total=0;r();clearInterval(brkTimer);brkTimer=null;}else r();},1000);}
taskRender();show(0);
/* ===== on-demand BREAK timer ===== */
var boTimer=null,boLeft=0;
function _pad2(n){return (n<10?'0':'')+n;}
function _boFmt(s){return Math.floor(s/60)+':'+_pad2(s%60);}
function boRender(){var cl=document.getElementById('boClock');if(cl){cl.textContent=_boFmt(Math.max(0,boLeft));cl.classList.toggle('over',boLeft<=0);}var end=new Date(Date.now()+Math.max(0,boLeft)*1000);var bk=document.getElementById('boBack');if(bk)bk.innerHTML=(boLeft<=0?'Time is up — ':'Back at ')+'<b>'+_pad2(end.getHours())+':'+_pad2(end.getMinutes())+'</b>';}
function _boTick(){boLeft--;if(boLeft<=0){boLeft=0;boRender();var eye=document.getElementById('boEye');if(eye)eye.textContent='Break is over';if(boTimer){clearInterval(boTimer);boTimer=null;}return;}boRender();}
function _boRun(){if(boTimer)clearInterval(boTimer);boTimer=setInterval(_boTick,1000);}
function openBreak(){var p=document.getElementById('breakPick');if(p)p.classList.add('on');var c=document.getElementById('bpCustom');if(c)c.value='';}
function closeBreakPick(){var p=document.getElementById('breakPick');if(p)p.classList.remove('on');}
function startBreak(min){min=Math.round(min);if(!min||min<1)return;if(min>180)min=180;closeBreakPick();boLeft=min*60;var eye=document.getElementById('boEye');if(eye)eye.textContent=min+(min===1?' minute':' minutes');boRender();var o=document.getElementById('breakOv');if(o)o.classList.add('on');_boRun();}
function addBreak(){boLeft=Math.max(0,boLeft)+300;var eye=document.getElementById('boEye');if(eye)eye.textContent='Break extended';boRender();_boRun();}
function endBreak(){if(boTimer){clearInterval(boTimer);boTimer=null;}var o=document.getElementById('breakOv');if(o)o.classList.remove('on');}
(function(){
  [].slice.call(document.querySelectorAll('.bp-chip')).forEach(function(b){b.onclick=function(){startBreak(+b.dataset.min);};});
  var go=document.getElementById('bpGo');if(go)go.onclick=function(){startBreak(+(document.getElementById('bpCustom').value));};
  var cx=document.getElementById('bpCancel');if(cx)cx.onclick=closeBreakPick;
  var bc=document.getElementById('bpCustom');if(bc)bc.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();startBreak(+bc.value);}});
  var ad=document.getElementById('boAdd');if(ad)ad.onclick=addBreak;
  var en=document.getElementById('boEnd');if(en)en.onclick=endBreak;
  var pk=document.getElementById('breakPick');if(pk)pk.addEventListener('click',function(e){if(e.target===pk)closeBreakPick();});
})();
""".replace("__LABELS__", LABELS)

FAVICON = ("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2032%2032%22"
           "%3E%3Crect%20width%3D%2232%22%20height%3D%2232%22%20rx%3D%227%22%20fill%3D%22%230A0507%22%2F%3E%3Ccircle%20cx%3D"
           "%2216%22%20cy%3D%2216%22%20r%3D%227%22%20fill%3D%22%23C8324A%22%2F%3E%3C%2Fsvg%3E")

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Day 2 · Presentations, Data &amp; Prompt Libraries — CODED × Alshaya</title>
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800;900&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>{CSS}
{CSS_BREAK}
{CSS_ADD}</style>
</head>
<body>

{SLIDES}

{CHROME}
<script>{SCRIPT}</script>
</body>
</html>
"""
page = (page.replace("/* ===== professional cover (CODED × KIBS, ref-matched) ===== */",
                     "/* ===== professional cover (CODED × Alshaya, ref-matched) ===== */")
            .replace("/* ===== cover BG v2: crimson-dominant (KIBS) + CODED blue accent ===== */",
                     "/* ===== cover BG v2: crimson-dominant + CODED blue accent ===== */"))
open(OUT, "w").write(page)
print("wrote", OUT, len(page), "bytes,", len(S), "slides")

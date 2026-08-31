# -*- coding: utf-8 -*-
"""Build the Alshaya Day 1 deck by splicing the gold-standard KIBS deck:
   CSS + presenter JS taken verbatim, Day-2-specific demo JS removed,
   content written from the supplied Day 1 markdown + instructor revisions."""
import re, json

EX    = "/Users/ayaalsaqaf/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/46c4e867-24f6-4e25-8db5-adecbebe4172/c097c4a3-d3ad-45b5-8472-60354fdb96eb/skills/workshop-builder/references/examples/deck.html"
LOGOF = "/Users/ayaalsaqaf/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/46c4e867-24f6-4e25-8db5-adecbebe4172/c097c4a3-d3ad-45b5-8472-60354fdb96eb/skills/workshop-builder/assets/coded-logo.txt"
OUT   = "/Users/ayaalsaqaf/codedxalshaya/site/coded-alshaya-day-1-deck.html"

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

# the describe-and-draw shape: a robot cat on a unicycle holding a balloon
SHAPE_SVG = """<svg viewBox="0 0 560 470" xmlns="http://www.w3.org/2000/svg">
  <circle class="acc" cx="215" cy="20" r="8"/><line class="acc" x1="215" y1="28" x2="215" y2="58"/>
  <path d="M152 72 L196 72 L170 32 Z"/><path d="M234 72 L278 72 L260 32 Z"/>
  <rect x="148" y="70" width="134" height="104" rx="16"/>
  <line class="acc" x1="172" y1="100" x2="192" y2="120"/><line class="acc" x1="192" y1="100" x2="172" y2="120"/>
  <circle cx="248" cy="110" r="14"/><circle cx="248" cy="113" r="5" fill="currentColor" stroke="none"/>
  <path d="M186 146 L200 136 L214 146 L228 136 L242 146"/>
  <line x1="120" y1="120" x2="146" y2="126"/><line x1="118" y1="136" x2="146" y2="136"/>
  <line x1="310" y1="120" x2="284" y2="126"/><line x1="312" y1="136" x2="284" y2="136"/>
  <line x1="215" y1="174" x2="215" y2="196"/>
  <rect x="160" y="196" width="110" height="96" rx="18"/>
  <rect x="182" y="216" width="66" height="40" rx="6"/>
  <circle cx="196" cy="236" r="4"/><circle cx="215" cy="236" r="4"/><circle cx="234" cy="236" r="4"/>
  <path d="M160 220 L112 250 L98 284"/>
  <path d="M270 214 L330 172 L384 152"/>
  <ellipse class="acc" cx="432" cy="70" rx="38" ry="46"/>
  <path class="acc" d="M424 114 L440 114 L432 126 Z"/>
  <path class="acc" d="M432 126 Q412 146 386 150"/>
  <path d="M270 268 C 322 268 332 226 300 218 C 278 213 276 240 296 246"/>
  <line x1="215" y1="292" x2="215" y2="330"/>
  <circle cx="215" cy="386" r="56"/><circle cx="215" cy="386" r="8"/>
  <line x1="215" y1="330" x2="215" y2="378"/><line x1="215" y1="394" x2="215" y2="442"/>
  <line x1="167" y1="358" x2="263" y2="414"/><line x1="167" y1="414" x2="263" y2="358"/>
  <rect x="152" y="396" width="26" height="10" rx="3"/><rect x="252" y="358" width="26" height="10" rx="3"/>
  <path d="M196 292 L172 396"/><path d="M240 292 L258 360"/>
</svg>"""

# ------------------------------------------------------------------ slides
S = []
def add(sid, label, html, attrs=""):
    S.append((sid, label, html, attrs))

add("cover", "Title",
 '<div class="cv2-bg"><div class="cv2-r1"></div><div class="cv2-r2"></div><div class="cv2-r3"></div>'
 '<div class="cv2-b1"></div><div class="cv2-wash"></div></div>\n'
 '<div class="bg-grid"></div><div class="cv2-vig"></div>\n<div class="cv2">\n'
 '  <div class="cv2-pill"><span class="dot"></span> CODED × Alshaya · Kuwait</div>\n'
 f'  <div class="cv2-logos"><img src="{LOGO}" alt="CODED"><span class="lx">×</span>'
 '<span style="font-size:19px;font-weight:800;letter-spacing:.15em;color:#fff">ALSHAYA</span></div>\n'
 '  <h1 class="cv2-title"><span class="cv2-t1">The Tool Is Already</span><br>'
 '<span class="cv2-t2">on Your Desk</span></h1>\n'
 '  <p class="cv2-sub">Day 1 — Foundations, responsible use, and the framework that turns a vague '
 'request into a draft you can send.</p>\n  <div class="cv2-meta">\n'
 '    <span class="cv2-daybadge">DAY 1</span>\n'
 '    <span class="cv2-mi"><svg viewBox="0 0 24 24"><rect x="3" y="4.5" width="18" height="17" rx="2.5"/>'
 '<path d="M16 2.5v4M8 2.5v4M3 10h18"/></svg> Tuesday 1 September 2026</span>\n'
 '    <span class="cv2-mi"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7.5v5l3 2"/>'
 '</svg> 09:00 – 13:00</span>\n'
 '    <span class="cv2-mi"><svg viewBox="0 0 24 24"><path d="M21 10.5c0 6.5-9 12.5-9 12.5s-9-6-9-12.5a9 9 0 0118 0z"/>'
 '<circle cx="12" cy="10.5" r="3"/></svg> CODED Campus</span>\n  </div>\n'
 '  <div class="cv2-standby"><span class="pdot"></span> Ali Taqi · Alshaya &amp; Al-Injaz</div>\n'
 '  <div class="cv2-cue">press <kbd>→</kbd> to begin · <kbd>?</kbd> for controls</div>\n</div>')

add("s1", "Cold-open", pad(
 '<div class="topic-tab b">Day 1</div>\n'
 '<h2 class="demo-h b">Yesterday\'s memo took you <span class="hl">45 minutes.</span></h2>\n'
 '<p class="lead b">By the end of today, you\'ll draft one in under 10.</p>'))

# S2 — question + LIVE capture field
add("s2", "Your dreaded tasks", question(
 "Before we begin",
 'What is one task on your desk this week that you <span class="hl">dread</span> the most?',
 extra='''  <div class="taskcap b">
    <div class="taskrow">
      <input id="taskInput" type="text" autocomplete="off" spellcheck="false"
             placeholder="Type what they say, then press Enter…">
      <button id="taskAdd" type="button">Add</button>
    </div>
    <div class="taskchips" id="taskList"></div>
    <div class="taskempty" id="taskEmpty">answers appear here</div>
    <button class="taskclear" id="taskClear" type="button">Clear all</button>
  </div>'''))

add("sec1", "01 · Foundations", section("01", "AI &amp; LLM Foundations"))

# S4 — what is AI, with the capability list
add("s4", "What is AI", reveal("🤖", "What is AI, really?",
 'Software that can <b>understand</b>, <b>learn</b>, and <b>generate</b> content that used to need a person to do it.',
 'Think of it as a fast assistant, not a replacement for your judgment.',
 extra='<div class="exs b">\n'
       '  <div class="exline good"><span class="xm">📖</span><div><b>Reads and understands text</b> — a contract, a report, an email thread</div></div>\n'
       '  <div class="exline good"><span class="xm">✍️</span><div><b>Writes content</b> — memos, notices, summaries, replies</div></div>\n'
       '  <div class="exline good"><span class="xm">💬</span><div><b>Answers questions</b> — about anything you paste into it</div></div>\n'
       '  <div class="exline good"><span class="xm">🧩</span><div><b>Helps solve problems</b> — options, trade-offs, next steps</div></div>\n'
       '  <div class="exline good"><span class="xm">🔋</span><div><b>Never gets tired and never forgets</b> — at 8 AM or 8 PM, same quality</div></div>\n'
       '</div>\n'))

# S5 — how an LLM works
add("s5", "What is an LLM", reveal("🧠", "What is an <span class=\"hl\">LLM</span>?",
 '<span class="al">Large Language Model</span>It read an enormous amount of text, learned the '
 '<b>patterns</b> in language, and now predicts what word should come next — one word at a time, '
 'until it has written a full answer.',
 'It is not looking anything up. It is <b>predicting the pattern</b> — which is why it can be fluent and wrong at the same time.'))

# S6 — what makes it "large"
add("s6", "What makes it large", pad(
 '<div class="bridge-tag tech b">The name</div>\n'
 '<h2 class="demo-h b">What makes an LLM <span class="hl">large</span>?</h2>\n'
 '<div class="gcards">\n'
 '  <div class="gcard b"><div class="ge">📚</div><div class="gh">Massive training data</div>'
 '<div class="gt">Billions of pages of text — books, articles, code, conversation.</div></div>\n'
 '  <div class="gcard b"><div class="ge">🔗</div><div class="gh">Billions of parameters</div>'
 '<div class="gt">The internal settings it tuned while learning those patterns.</div></div>\n'
 '  <div class="gcard b"><div class="ge">🏗️</div><div class="gh">Complex tasks</div>'
 '<div class="gt">Enough scale to hold a long document in mind and reason across it.</div></div>\n'
 '  <div class="gcard b"><div class="ge">🎯</div><div class="gh">One job</div>'
 '<div class="gt">Predict the next word. Everything else is that, repeated.</div></div>\n'
 '</div>\n'
 '<div class="keyline b">Large is about <b>scale</b>, not intelligence. It is a very good pattern-predictor.</div>'))

# S7 — the models (replaces "Which tool for which job")
add("s7", "The models", pad(
 '<div class="bridge-tag tech b">The landscape</div>\n'
 '<h2 class="demo-h sm b">Four names you\'ll hear</h2>\n'
 '<p class="lead b">They all work the same way. What differs is who built them, and what each is strongest at.</p>\n'
 '<div class="models">\n'
 '  <div class="mcard b"><div class="mname">ChatGPT</div><div class="mmaker">OpenAI</div>'
 '<div class="mdesc">The best known. Strong all-rounder for writing and everyday questions, with a large '
 'add-on ecosystem.</div></div>\n'
 '  <div class="mcard pick b"><div class="mname">Claude</div><div class="mmaker">Anthropic</div>'
 '<div class="mdesc">Strongest on long documents, careful analysis, and natural professional writing. '
 'Built with a heavy focus on safety.</div><span class="mtag">We use this</span></div>\n'
 '  <div class="mcard b"><div class="mname">Gemini</div><div class="mmaker">Google</div>'
 '<div class="mdesc">Built into Google Workspace. Convenient if your documents already live in Docs, '
 'Sheets, and Gmail.</div></div>\n'
 '  <div class="mcard b"><div class="mname">DeepSeek</div><div class="mmaker">DeepSeek AI</div>'
 '<div class="mdesc">An open, low-cost option from China. Capable, and popular where budget or '
 'self-hosting matters.</div></div>\n'
 '</div>\n'
 '<div class="keyline b">Learn the skill once and it moves with you. <b>The prompt is the skill — not the logo.</b></div>'))

# S8 — why should you care
add("s8", "Why you should care", gridcards(
 'Why should <span class="hl">you</span> care?',
 [("⏱️", "Save time", "Automate repetitive writing. Summarise long documents. Get a first draft in minutes instead of an hour."),
  ("✅", "Improve quality", "Catch errors and inconsistencies, tighten unclear writing, and sound consistently professional."),
  ("💡", "Think better", "Brainstorm options, organise messy information, and see a problem from angles you had not considered."),
  ("📈", "Work smarter", "Read data faster, prepare for meetings quicker, and spend your hours on judgment instead of typing.")],
 note="None of this replaces you. It removes the part of the job that was never the point.",
 lead="Not because it is new — because of what it gives back to your week."))

add("s9", "Strong vs weak", comparison("What AI Does Well vs. Where It Fails",
 "Weak at", "Facts it cannot check, your company's private context, and final judgment calls",
 "Strong at", "Drafting, summarizing, brainstorming, and finding patterns in data",
 "AI can state a wrong fact with full confidence. This is called a <b>hallucination</b> — always verify anything that matters."))

add("s10", "What is safe to type", reveal("🔒", "What Can You Safely Type Into AI?",
 '<span class="al">Caution</span>Do not paste tenant records, financial data, or contract terms into a '
 'public AI tool. Use only information that is already public or approved for outside tools.',
 'When you are not sure, ask your manager before you paste it.', caution=True))

add("s11", "Example · memo", comparison("Real Example — Writing a Memo",
 "Before AI", "45 minutes: blank page, first draft, two rewrites, final check",
 "After AI", "10 minutes: describe the memo, get a draft, edit, done",
 "Same memo. <b>One-quarter of the time.</b>"))

add("s12", "Example · report", comparison("Real Example — Reading a Long Report",
 "Before AI", "60 minutes: read the whole report and write notes",
 "After AI", "5 minutes: upload the report and ask for the key points",
 "You still read the summary. <b>AI reads the report.</b>"))

# S13 — call-back question, echoes the captured tasks
add("s13", "Call-back question", question(
 "Back to your list",
 'Which one of these would save you the <span class="hl">most time</span> this month?',
 extra='  <div class="taskchips b" id="taskEcho"></div>\n'
       '  <div class="taskempty" id="taskEmpty2">nothing captured yet — go back to slide 3</div>\n'))

add("break1", "Break 1", brk("Stretch and Reset", 10), ' data-min="10"')

# --- describe-and-draw exercise (segue into prompting)
add("draw", "Describe &amp; draw", pad(
 '<div class="topic-tab b">Two volunteers</div>\n'
 '<h2 class="demo-h sm b">Describe It, Draw It</h2>\n'
 '<p class="lead b">One person sees the shape. One person draws it. '
 'The drawer faces the whiteboard, <b>back to the screen</b> — no peeking.</p>\n'
 '<div class="road b">\n'
 '    <div class="ritem b"><div class="rn">1</div><div><div class="rt">Pick two volunteers</div>'
 '<div class="rd">One at the whiteboard with a marker. One facing the screen.</div></div></div>\n'
 '    <div class="ritem b"><div class="rn">2</div><div><div class="rt">Describe it in words only</div>'
 '<div class="rd">No gestures, no drawing in the air. The drawer may not ask questions — yet.</div></div></div>\n'
 '    <div class="ritem b"><div class="rn">3</div><div><div class="rt">Two minutes on the clock</div>'
 '<div class="rd">The shape is on the next slide. Press T for the timer, then compare the drawing to the original.</div></div></div>\n'
 '    <div class="ritem b"><div class="rn">4</div><div><div class="rt">Run it again — questions allowed</div>'
 '<div class="rd">Same shape, new pair. Watch how much faster it goes.</div></div></div>\n'
 '</div>'))

add("drawshape", "The shape",
 '<div class="bg-grid"></div><div class="blob b1"></div>'
 '<div class="shapestage">\n'
 '  <div class="ph-eyebrow b">Describer only — drawer, eyes on the board</div>\n'
 '  <div class="shapebox b">\n'
 '    <button class="shapebtn" id="shapeBtn" type="button">Show the shape</button>\n'
 f'    <div class="shapewrap" id="shapeWrap">{SHAPE_SVG}</div>\n'
 '  </div>\n</div>')

add("drawpoint", "The segue", pad(
 '<div class="bridge-tag tech b">What just happened</div>\n'
 '<h2 class="demo-h b">Vague words in.<br><span class="hl">Vague drawing out.</span></h2>\n'
 '<div class="exs">\n'
 '  <div class="exline bad b"><span class="xm">✗</span><div>“Draw a cat on a wheel with a balloon.” '
 '— technically true, and the drawing looks nothing like it.</div></div>\n'
 '  <div class="exline good b"><span class="xm">✓</span><div>“A square robot cat head with two triangle ears '
 'and an antenna, one X eye and one round eye, on a rectangular body, riding a single large wheel, '
 'holding a balloon in its raised right arm.”</div></div>\n'
 '</div>\n'
 '<div class="keyline b">The drawer is the AI. It can only draw what you actually described — '
 '<b>it cannot see what is in your head.</b></div>'))

add("sec2", "02 · First prompts", section("02", "Your First Prompts"))

add("s14", "Exercise 1", steps("Exercise", "Exercise: Your First Prompt", "8 minutes", [
 ("Open Claude", "This is the tool we're using for the whole program."),
 ("Ask one real question", "Pick something from your actual to-do list today."),
 ("Read the answer closely", "Decide: is it correct? Is it useful as it is?"),
], "Task Sheet 1"))

add("s15", "Good prompt", framework("Framework", "What Makes a Good Prompt?", [
 "<b>Specific</b> — say exactly what you want",
 "<b>Clear purpose</b> — say why you need it",
 "<b>Give details</b> — background, numbers, names",
 "<b>Set the tone</b> — formal, friendly, or technical",
]))

add("s16", "Weak vs strong", comparison("Weak Prompt vs. Strong Prompt",
 "Weak", '“Write something about the new parking policy.”',
 "Strong", '“Write a 100-word notice for tenants about the new parking policy starting Sunday. '
           'Use a friendly, clear tone.”'))

add("break2", "Break 2", brk("Stretch and Reset", 10), ' data-min="10"')

add("sec3", "03 · CTFT", section("03", "The CTFT Framework"))

add("s19", "CTFT", framework("Framework", "CTFT: Four Parts of a Great Prompt", [
 "<b>C</b>ontext — the background",
 "<b>T</b>ask — the exact request",
 "<b>F</b>ormat — how you want it structured",
 "<b>T</b>one — the style and voice",
]))

add("s20", "C = Context", badgood(
 'C = <span class="hl">Context</span>',
 'Tell the AI your role, the situation, and who will read the result. AI does not know your building, '
 'your team, or your project unless you say so.',
 [('“Write about the policy.”<br><i>Which policy? Whose? For whom?</i>',
   '“I manage leasing for a retail property with 12 vacant units. Our tenant parking policy changes on Sunday.”')],
 'No context, no relevance. <b>Start with who you are and what is going on.</b>'))

add("s21", "T = Task", badgood(
 'T = <span class="hl">Task</span>',
 'State the one action you want, written as a clear command. Ask for one thing, not five things at once.',
 [('“Help me with this.”<br><i>Help how — write it, shorten it, check it?</i>',
   '“Write a one-page leasing update for the regional director.”')],
 'One clear verb, one clear deliverable. <b>Write, summarise, compare, list — pick one.</b>'))

add("s22", "F = Format", badgood(
 'F = <span class="hl">Format</span>',
 'Say how long the result should be, how it should be structured, and what type of document it is.',
 [('“Write a document.”<br><i>How long? Bullets or prose? What sections?</i>',
   '“One page. Opening summary, three bullet points, then a closing recommendation.”')],
 'If you do not choose the shape, <b>the AI chooses it for you</b> — and you rewrite it.'))

add("s23", "T = Tone", badgood(
 'T = <span class="hl">Tone</span>',
 'Say the style you want: formal, friendly, technical, or persuasive. The same facts land very differently.',
 [('“Write an email.”<br><i>To a regulator, or to your team?</i>',
   '“Professional and direct — this goes to the regional director, who is short on time.”')],
 'Tone is not decoration. <b>It is how the reader decides whether to act.</b>'))

add("s24", "Role &amp; constraints", reveal("", "Two Extra Tools: Role and Constraints",
 '<b>Role</b> tells the AI who to act as — “act as a facilities manager.” <b>Constraints</b> set a '
 'limit — “do not mention the budget number.” Add these to CTFT when you need more control.',
 'Optional extensions — use them only when plain CTFT is not specific enough.'))

add("s25", "Zero vs few-shot", comparison("One Task, Two Ways to Ask",
 "Zero-shot", 'Ask directly, with no example: “Write a reply to a tenant complaint about noise.”',
 "Few-shot", 'Give AI one sample reply first, then ask it to match that same style.',
 "Use <b>few-shot</b> prompting when tone and format matter more than usual."))

add("s26", "CTFT in action", comparison("CTFT in Action",
 "Poor prompt", '“Write about the maintenance backlog.”',
 "Excellent CTFT prompt",
 '<b>[CONTEXT]</b> I manage facilities at a retail property with 40 open maintenance tickets. '
 '<b>[TASK]</b> Write a one-page update for the operations director. '
 '<b>[FORMAT]</b> Opening summary, three bullet points, closing recommendation. '
 '<b>[TONE]</b> Professional and direct.'))

add("s27", "Practice · CTFT", steps("Practice", "Practice: Build Your Own CTFT Prompt", "10 minutes", [
 ("Pick a real task", "Something due this week."),
 ("Write all four parts", "Context, Task, Format, Tone."),
 ("Run it in Claude and check", "Does the result match all four parts you asked for?"),
], "Task Sheet 2"))

add("break3", "Break 3", brk("Stretch and Reset", 10), ' data-min="10"')

add("sec4", "04 · Writing", section("04", "Writing &amp; Communication With AI"))

add("wmoves", "Three moves", framework("Framework", "Three moves you'll use every day", [
 "<b>Draft</b> — turn a prompt into a first version",
 "<b>Rewrite</b> — change the tone or the length of something that already exists",
 "<b>Summarize</b> — pull the key points out of a thread or a document",
]))

add("wdraft", "1 · Draft", badgood(
 '1 — <span class="hl">Draft</span> from a prompt',
 'You give Claude a CTFT prompt. It gives you a first version. That first version is never the '
 'final version — it is the thing you react to.',
 [('“Write an email about the lift.”<br><i>Which lift, when, to whom, how long?</i>',
   '<b>[CONTEXT]</b> I am the facilities lead at a retail property. The north lift is out Thursday, '
   '9 AM to 12 PM. <b>[TASK]</b> Write a notice email to all tenants. <b>[FORMAT]</b> Subject line '
   'plus three short paragraphs, under 120 words. <b>[TONE]</b> Clear and apologetic, but brief.')],
 'A blank page costs you 45 minutes. <b>A draft you can argue with costs 30 seconds.</b>'))

add("wtone", "2 · Rewrite tone", comparison("2 — Rewrite: change the <span class=\"hl\">tone</span>",
 "Formal", '“We wish to inform tenants that the north elevator will be out of service from 9 AM to 12 PM on Thursday.”',
 "Conversational", '“Quick note — the north elevator will be down for repairs Thursday morning, 9 to 12.”',
 "Same facts, same length. <b>Two different readers.</b>"))

add("wlength", "2 · Rewrite length", pad(
 '<div class="bridge-tag tech b">Rewrite</div>\n'
 '<h2 class="demo-h b">2 — Rewrite: change the <span class="hl">length</span></h2>\n'
 '<div class="anchor b">You do not need a new prompt to fix a draft. Say what to change, in plain '
 'words, in the same conversation.</div>\n'
 '<div class="exs">\n'
 '  <div class="exline good b"><span class="xm">↓</span><div>“Make it half as long.”</div></div>\n'
 '  <div class="exline good b"><span class="xm">↓</span><div>“Cut this to three bullet points.”</div></div>\n'
 '  <div class="exline good b"><span class="xm">↑</span><div>“Expand the second paragraph — add the reason for the delay.”</div></div>\n'
 '  <div class="exline good b"><span class="xm">→</span><div>“Say the same thing in one sentence.”</div></div>\n'
 '</div>\n'
 '<div class="keyline b">Shorter is almost always better. <b>Ask for half, then read it again.</b></div>'))

add("s31", "Iterative prompting", reveal("", 'Refine, <span class="hl">Don\'t Restart</span>',
 'When a draft is close but not right, tell Claude exactly what to change. “Make it shorter.” '
 '“Make it warmer.” Do not start a new prompt from zero.',
 'This is called <b>iterative prompting</b> — small corrections, same conversation.'))

add("wsummary", "3 · Summarize", badgood(
 '3 — <span class="hl">Summarize</span> the key points',
 'Paste in a long email thread or a set of meeting notes. Then ask for the shape of summary you '
 'actually need — not just “summarize”.',
 [('“Summarize this.”<br><i>You get a paragraph. You still do not know what you owe anyone.</i>',
   '“Summarize this thread in five bullet points. List every decision made, every question still '
   'open, and who owns each action.”')],
 'Ask for the shape you need. <b>Then check it against the original.</b>'))

add("wemail", "Email with Claude", reveal("✉️", "Email, end to end",
 'Three things Claude handles well on email — and all three are just Draft, Rewrite and Summarize '
 'pointed at your inbox.',
 'Right now this is copy and paste. <b>The next slide removes the copy and paste.</b>',
 extra='<div class="exs b">\n'
       '  <div class="exline good"><span class="xm">📥</span><div><b>Summarize a thread</b> — “What was '
       'decided, what is still open, and what do I owe anyone?”</div></div>\n'
       '  <div class="exline good"><span class="xm">✍️</span><div><b>Draft a message</b> — “Reply to the '
       'tenant below. Apologise for the delay, give Thursday as the new date, under 100 words.”</div></div>\n'
       '  <div class="exline good"><span class="xm">↩️</span><div><b>Match your own voice</b> — “Reply in '
       'the same tone I used earlier in this thread.”</div></div>\n'
       '</div>\n'))

add("wmcp", "Connect your inbox", pad(
 '<div class="bridge-tag tech b">One step further</div>\n'
 '<h2 class="demo-h sm b">Connect it straight to your inbox</h2>\n'
 '<div class="anchor b"><span class="al">MCP · Model Context Protocol</span>An open standard that lets '
 'an AI assistant plug into the tools you already use — mail, calendar, files. Once it is connected, '
 'Claude reads the thread and drafts the reply <b>in place</b>. No copying, no pasting.</div>\n'
 '<div class="exs">\n'
 '  <div class="exline good b"><span class="xm">◆</span><div><b>Claude</b> — connects to mail, calendar '
 'and files through MCP connectors</div></div>\n'
 '  <div class="exline good b"><span class="xm">◆</span><div><b>ChatGPT</b> — its own connectors for '
 'mail and documents</div></div>\n'
 '  <div class="exline good b"><span class="xm">◆</span><div><b>Microsoft Copilot</b> — built directly '
 'into Outlook, already inside Microsoft 365</div></div>\n'
 '</div>\n'
 '<div class="keyline caution b">This points an AI tool at <b>real company mail</b>. Nobody connects '
 'anything until IT and your manager have approved it.</div>'))

add("s33", "Exercise 2", steps("Exercise", "Exercise: Draft a Professional Document", "15 minutes", [
 ("Choose your scenario", "A memo, a tenant notice, or an update email."),
 ("Write a full CTFT prompt", "Use today's framework."),
 ("Draft, then rewrite it", "Fix the tone, cut the length, check every fact."),
], "Task Sheet 3"))

add("break4", "Break 4", brk("Stretch and Reset", 10), ' data-min="10"')

add("sec5", "05 · Review", section("05", "Reviewing AI Output &amp; Using AI for Research"))

add("s36", "Pre-send check", framework("", "Before You Send Any AI Draft, Check:", [
 "<b>Accuracy</b> — are the facts correct?",
 "<b>Tone</b> — does it match the reader?",
 "<b>Structure</b> — is it easy to follow?",
 "<b>Numbers</b> — did you verify every calculation by hand?",
]))

add("s37", "Research assistant", reveal("", "AI as a Research Assistant",
 'Paste in a long document and ask for a summary, the key points, or the open questions it raises.',
 'You still read the summary. <b>AI reads the document.</b>'))

add("s38", "Example · 20 pages", comparison("Real Example — A 20-Page Report",
 "Before AI", "60 minutes: read the full report, take notes, write a summary",
 "After AI", "5 minutes: upload the report, ask for a summary, verify the key numbers"))

add("s39", "Exercise 3", steps("Exercise", "Exercise: Summarize a Real Document", "12 minutes", [
 ("Download the quarterly report", "Five pages of sample data — safe to upload. It's in the lab."),
 ("Ask for a one-page summary", "Use a full CTFT prompt. Say what shape you need."),
 ("Check three numbers by hand", "Against the report, not against the summary."),
 ("Find a planted mistake", "There are five in there. One is enough."),
], "Task Sheet 4"))

add("close", "Wrap", pad(
 '<div class="topic-eyebrow b">Today you built:</div>\n'
 '<h2 class="demo-h sm b">Three things that are <span class="hl">already yours.</span></h2>\n'
 '<div class="oc-list">\n'
 '    <div class="oc-item b"><div class="oc-check"><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"></path></svg></div>'
 '<div class="oc-txt">A <b>CTFT prompt</b> for a real work task</div></div>\n'
 '    <div class="oc-item b"><div class="oc-check"><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"></path></svg></div>'
 '<div class="oc-txt">A <b>professional document</b>, drafted and edited with Claude</div></div>\n'
 '    <div class="oc-item b"><div class="oc-check"><svg viewBox="0 0 24 24"><path d="M5 12l5 5L20 7"></path></svg></div>'
 '<div class="oc-txt">A <b>document summary</b>, verified against the source</div></div>\n'
 '</div>\n'
 '<div class="keyline b">Tomorrow: turn today\'s skills into presentations and data insights.</div>'))

add("end", "End",
 '<div class="cv2-bg"><div class="cv2-r1"></div><div class="cv2-r3"></div><div class="cv2-wash"></div></div>\n'
 '<div class="bg-grid"></div><div class="cv2-vig"></div>\n<div class="cv2">\n'
 '  <div class="cv2-pill"><span class="dot"></span> End of Day 1</div>\n'
 '  <h1 class="cv2-title" style="margin-top:26px"><span class="cv2-t1">See you</span> '
 '<span class="cv2-t2">tomorrow.</span></h1>\n'
 '  <p class="cv2-sub">Day 2 — Presentations, Data Analysis &amp; Reusable Workflows</p>\n'
 '  <div class="cv2-meta"><span class="cv2-mi"><svg viewBox="0 0 24 24">'
 '<rect x="3" y="4.5" width="18" height="17" rx="2.5"/><path d="M16 2.5v4M8 2.5v4M3 10h18"/></svg> '
 'Wednesday 2 September 2026 · 09:00 – 13:00</span></div>\n</div>')

# ------------------------------------------------------------------ assemble
slides_html = [f'<div class="{"slide active" if i==0 else "slide"}" id="{sid}"{attrs}>\n{html}\n</div>'
               for i, (sid, _, html, attrs) in enumerate(S)]
SLIDES = "\n\n".join(slides_html)
LABELS = json.dumps([lbl for _, lbl, _, _ in S])

CHROME = """
<div id="prail-wrap"><div id="prail"></div></div>
<a class="deck-back" href="coded-alshaya-day-1.html">‹ Day 1</a>
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
<title>Day 1 · AI Quickstart &amp; the Art of Prompting — CODED × Alshaya</title>
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

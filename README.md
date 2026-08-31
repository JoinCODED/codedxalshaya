# CODED × Alshaya — AI in Workflow for Professionals

Workshop site for **Alshaya Property Development Co.** and **Al-Injaz Contracting Company**.

| | |
|---|---|
| **Dates** | Tuesday 1 – Thursday 3 September 2026 |
| **Timing** | 09:00 – 13:00 daily · 12 hours total |
| **Location** | CODED Campus, Kuwait |
| **Instructor** | Ali Taqi |
| **Trainees** | 14, mixed departments — teams of two on Day 3 |
| **Tool** | Claude (plus Gamma for presentation variety on Day 2) |
| **Level** | Beginner-friendly · no coding |

## Deploying

Static site, no build step. Everything served from `site/`.

`vercel.json` sets `outputDirectory: site` and `cleanUrls: true`, so pages resolve at
`/coded-alshaya-day-1` as well as `/coded-alshaya-day-1.html`.

If Vercel asks during import: **Framework preset** = Other, **Output Directory** = `site`,
**Build Command** = none.

## What's in `site/`

| File | What it is |
|---|---|
| `index.html` | Landing page — hero and the three programme cards |
| `coded-alshaya-day-1.html` | Day 1 plan — brief, run of show, resources |
| `coded-alshaya-day-1-deck.html` | Day 1 deck · 52 slides |
| `coded-alshaya-day-1-lab.html` | Day 1 trainee lab · 6 tasks |
| `alshaya-quarterly-operations-report.pdf` | Day 1 exercise document · 5 pages, sample data |
| `coded-alshaya-day-2.html` | Day 2 plan |
| `coded-alshaya-day-2-deck.html` | Day 2 deck · 36 slides |
| `coded-alshaya-day-2-lab.html` | Day 2 trainee lab · 6 exercises |
| `alshaya-day-2-dataset.xlsx` | Day 2 dataset · 6 sheets, sample data |
| `coded-alshaya-day-3.html` | Day 3 plan — assessment, capstone, certificates |
| `coded-alshaya-day-3-deck.html` | Day 3 deck · 26 slides |
| `coded-alshaya-day-3-lab.html` | Day 3 capstone lab · 6 tasks, 7 team scenarios |
| `alshaya-capstone-s1.xlsx` … `s7.xlsx` | Day 3 scenario workbooks · one self-contained file per team |

Every page is a single self-contained HTML file — CSS and JS inline, logo as a data URI,
fonts from Google. No bundler, no dependencies.

## Sample data

All figures across the PDF and the workbook describe one **fictional** three-property
portfolio, and they reconcile with each other by design. Nothing here is an Alshaya or
Al-Injaz record.

The quarterly report contains **five deliberate factual faults** for the Day 1 verification
exercise, and each Day 3 scenario workbook carries **one planted inconsistency**, catchable
inside the team's own file (trainees are told one exists, not what it is). Both sets are
documented in `instructor/` — `coded-alshaya-day-1-answer-key.html` and
`coded-alshaya-capstone-data-key.html` — kept **outside `site/`** on purpose, so they
never deploy and trainees cannot stumble on them. Open them locally for the debriefs.

## MAP test

`instructor/coded-alshaya-map-test-key.html` is the answer key for the pre/post knowledge test —
20 questions, 30 minutes, sat twice: Day 1 before teaching starts, and Day 3 before the capstone.
The test itself lives in the CODED portal as the draft survey
**Alshaya MAP Test — AI in Workflow (Pre & Post)** (`alshaya-map-test-ai-in-workflow-pre-post`).
The key stays outside `site/` with the other instructor material, so it never deploys.

## Rebuilding

The generators in `build/` produce the decks, labs and data files. They splice from the
CODED workshop-builder skill's reference build, so paths inside them are local to the
authoring machine.

```bash
python3 build/build-day-1-deck.py
python3 build/build-day-1-lab.py
python3 build/build-day-2-deck.py
python3 build/build-day-2-lab.py
python3 build/build-day-2-dataset.py   # needs openpyxl
python3 build/build-ops-report.py      # needs reportlab
python3 build/build-day-3-deck.py      # clones the Day 2 deck shell
python3 build/build-day-3-lab.py       # clones the Day 2 lab shell
python3 build/build-capstone-data.py   # needs openpyxl; reads the Day 2 dataset
```

## Day 3 shape

09:00 final assessment (30 min) → 09:30 capstone build (7 teams of two, scenarios S1–S7,
four deliverables on timed blocks) → 11:45 six-minute team presentations → 12:30
certificates and close. Each team gets its own self-contained scenario workbook
(`alshaya-capstone-s1.xlsx` … `s7.xlsx`) — same fictional portfolio, but every team
uploads one file with everything its scenario needs.

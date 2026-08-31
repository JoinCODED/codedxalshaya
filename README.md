# CODED × Alshaya — AI in Workflow for Professionals

Workshop site for **Alshaya Property Development Co.** and **Al-Injaz Contracting Company**.

| | |
|---|---|
| **Dates** | Tuesday 1 – Thursday 3 September 2026 |
| **Timing** | 09:00 – 13:00 daily · 12 hours total |
| **Location** | CODED Campus, Kuwait |
| **Instructor** | Ali Taqi |
| **Trainees** | Up to 10, mixed departments |
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
| `coded-alshaya-day-3.html` | Day 3 plan (capstone deck and lab still to come) |

Every page is a single self-contained HTML file — CSS and JS inline, logo as a data URI,
fonts from Google. No bundler, no dependencies.

## Sample data

All figures across the PDF and the workbook describe one **fictional** three-property
portfolio, and they reconcile with each other by design. Nothing here is an Alshaya or
Al-Injaz record.

The quarterly report contains **five deliberate factual faults** for the Day 1 verification
exercise. They are documented in `instructor/coded-alshaya-day-1-answer-key.html` — kept
**outside `site/`** on purpose, so it never deploys and trainees cannot stumble on it.
Open it locally when running the L1.6 debrief.

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
```

## Still to come

- Day 3 capstone deck and brief
- Practice quiz and exam (not yet decided)

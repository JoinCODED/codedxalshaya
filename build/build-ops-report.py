# -*- coding: utf-8 -*-
"""Quarterly Property Operations Report — synthetic training document.
   Contains FIVE deliberately planted faults for the Day 1 verification exercise.
   See build-ops-report-answer-key.md for the list."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                KeepTogether)

OUT = "/Users/ayaalsaqaf/codedxalshaya/site/alshaya-quarterly-operations-report.pdf"

INK   = colors.HexColor("#1A1A1A")
MUTED = colors.HexColor("#5A5A5A")
RULE  = colors.HexColor("#C9C9C9")
BAND  = colors.HexColor("#F0F0F0")
ACC   = colors.HexColor("#8B1E2A")

ss = getSampleStyleSheet()
def S(name, **kw):
    base = kw.pop("parent", ss["Normal"])
    return ParagraphStyle(name, parent=base, **kw)

TITLE = S("t", fontName="Helvetica-Bold", fontSize=19, leading=23, textColor=INK, spaceAfter=2)
SUB   = S("s", fontName="Helvetica", fontSize=11, leading=15, textColor=MUTED, spaceAfter=14)
H1    = S("h1", fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=INK,
          spaceBefore=16, spaceAfter=7)
BODY  = S("b", fontName="Helvetica", fontSize=9.6, leading=14.4, textColor=INK,
          alignment=TA_JUSTIFY, spaceAfter=7)
BULL  = S("bu", parent=BODY, leftIndent=12, bulletIndent=2, spaceAfter=3.5, alignment=0)
NOTE  = S("n", fontName="Helvetica-Oblique", fontSize=9, leading=13, textColor=MUTED, spaceAfter=6)
CELL  = S("c", fontName="Helvetica", fontSize=8.8, leading=12, textColor=INK)
CELLB = S("cb", fontName="Helvetica-Bold", fontSize=8.8, leading=12, textColor=INK)
CAP   = S("cap", fontName="Helvetica", fontSize=8, leading=11, textColor=MUTED, spaceBefore=4)

def rule(space_before=2, space_after=8):
    t = Table([[""]], colWidths=[170*mm], rowHeights=[0.6])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),RULE),
                           ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    return [Spacer(1, space_before), t, Spacer(1, space_after)]

def table(data, widths, align_right=(), header=True, band_rows=()):
    rows = []
    for r_i, row in enumerate(data):
        out = []
        for c_i, cell in enumerate(row):
            st = CELLB if (header and r_i == 0) or r_i in band_rows else CELL
            out.append(Paragraph(str(cell), st))
        rows.append(out)
    t = Table(rows, colWidths=widths, repeatRows=1 if header else 0)
    style = [
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 7),
        ("RIGHTPADDING", (0,0), (-1,-1), 7),
        ("LINEBELOW", (0,0), (-1,-2), 0.4, RULE),
        ("LINEABOVE", (0,0), (-1,0), 0.8, INK),
        ("LINEBELOW", (0,-1), (-1,-1), 0.8, INK),
    ]
    if header:
        style.append(("BACKGROUND", (0,0), (-1,0), BAND))
    for br in band_rows:
        style.append(("BACKGROUND", (0,br), (-1,br), BAND))
    for c in align_right:
        style.append(("ALIGN", (c,0), (c,-1), "RIGHT"))
    t.setStyle(TableStyle(style))
    return t

def chrome(canvas, doc):
    canvas.saveState()
    w, h = A4
    # header
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.setFillColor(ACC)
    canvas.drawString(20*mm, h - 13*mm, "SAMPLE DATA — TRAINING USE ONLY")
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawRightString(w - 20*mm, h - 13*mm,
                           "Quarterly Property Operations Report  ·  Q2 2026")
    canvas.setStrokeColor(RULE); canvas.setLineWidth(0.5)
    canvas.line(20*mm, h - 15.5*mm, w - 20*mm, h - 15.5*mm)
    # footer
    canvas.line(20*mm, 15*mm, w - 20*mm, 15*mm)
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(MUTED)
    canvas.drawString(20*mm, 11*mm,
        "Fictional portfolio. All entities, figures and dates are invented for training purposes.")
    canvas.drawRightString(w - 20*mm, 11*mm, "Page %d" % doc.page)
    canvas.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=22*mm, bottomMargin=20*mm,
                        title="Quarterly Property Operations Report — Q2 2026 (Sample Data)",
                        author="CODED — AI in Workflow for Professionals",
                        subject="Training document. Sample data only.")
E = []

# ───────────────────────── cover block
E.append(Paragraph("Quarterly Property Operations Report", TITLE))
E.append(Paragraph("Portfolio review for the quarter ended 30 June 2026", SUB))
E.append(table([
    ["Prepared for",  "[OPERATIONS DIRECTOR] — Regional Operations"],
    ["Prepared by",   "[FACILITIES LEAD], with input from Leasing and Finance"],
    ["Report date",   "15 July 2026"],
    ["Period covered","1 April – 30 June 2026"],
    ["Portfolio",     "[PROPERTY A], [PROPERTY B], [PROPERTY C]"],
    ["Classification","Sample data. Training use only. Not a real portfolio."],
], [38*mm, 132*mm], header=False))
E += rule(10, 4)

# ───────────────────────── 1. executive summary
E.append(Paragraph("1.  Executive summary", H1))
E.append(Paragraph(
 "The portfolio closed the quarter broadly stable, with a combined annualised rent roll of "
 "<b>KWD 4.72 million</b> across the two income-producing assets. Occupancy across the retail asset "
 "held at <b>78%</b> for the quarter, while the mixed-use tower remained close to full. Collections "
 "softened slightly but remain within tolerance.", BODY))
E.append(Paragraph(
 "Costs are the principal concern. Maintenance spend is running ahead of plan and the open-ticket "
 "backlog has grown for a third consecutive month, with tenant complaints more than doubling. "
 "Utilities are up year on year, driven by HVAC runtime at [PROPERTY B].", BODY))
E.append(Paragraph(
 "On construction, [PROPERTY C] slipped three weeks against programme following a late joinery "
 "delivery, now resolved. Cost impact is contained within contingency, and <b>the Board approved the "
 "revised handover date</b> at its June sitting. The tenant has been kept informed.", BODY))
E.append(Paragraph(
 "Tenant sentiment has deteriorated. Three tenants escalated in writing during the quarter, and "
 "logged complaints more than doubled month on month. Two of the three escalations relate to lift "
 "availability at [PROPERTY B].", BODY))
E.append(Paragraph(
 "Three matters require a decision this quarter: the upper-floor leasing incentive at [PROPERTY A], "
 "the maintenance budget position, and the portfolio-wide collateral revaluation, which is now "
 "materially out of date.", BODY))

# ───────────────────────── 2. portfolio overview
E.append(Paragraph("2.  Portfolio overview", H1))
E.append(table([
    ["Asset", "Type", "Status", "Opened / due"],
    ["[PROPERTY A]", "Retail centre",     "Operating",          "Opened 2019"],
    ["[PROPERTY B]", "Mixed-use tower",   "Operating",          "Opened 2016"],
    ["[PROPERTY C]", "Ground-floor unit", "Under construction", "Handover 2026"],
], [38*mm, 44*mm, 44*mm, 44*mm]))

# ───────────────────────── 3. occupancy & income
E.append(Paragraph("3.  Occupancy and income", H1))
E.append(table([
    ["Asset", "Units", "Let", "Occupancy", "Annualised rent roll (KWD)"],
    ["[PROPERTY A]", "48", "36", "75.0%", "1,940,000"],
    ["[PROPERTY B]", "62", "56", "90.3%", "2,610,000"],
    ["[PROPERTY C]", "14", "0",  "—", "—"],
    ["<b>Portfolio total</b>", "<b>124</b>", "<b>92</b>", "<b>74.2%</b>", "<b>4,720,000</b>"],
], [38*mm, 22*mm, 22*mm, 30*mm, 58*mm], align_right=(1,2,3,4), band_rows=(4,)))
E.append(Paragraph("Table 3.1 — Occupancy and annualised rent roll at 30 June 2026.", CAP))
E.append(Spacer(1, 8))
for b in [
 "[PROPERTY A] occupancy fell from 83% in the same quarter last year. Twelve units are vacant; "
 "five have now been vacant for more than nine months, all on the upper floor.",
 "Three leases at [PROPERTY A] expire within 90 days. Two of those tenants have not responded to "
 "renewal outreach.",
 "Average rent achieved at [PROPERTY A] is KWD 11.40 per sqm against an asking rate of KWD 13.00.",
 "One new signing this quarter: a food-and-beverage operator, 240 sqm, five-year term.",
 "Footfall at [PROPERTY A] is down 8% year on year. Both anchor tenants report flat sales.",
 "Blended collection rate for the quarter was 96.2%, down from 98.1%. Two tenants are on payment plans.",
]:
    E.append(Paragraph(b, BULL, bulletText="–"))

# ───────────────────────── 4. cost position
E.append(Paragraph("4.  Cost position", H1))
E.append(table([
    ["Cost line", "Position at 30 June", "Comment"],
    ["Maintenance", "62% of annual budget spent",
     "Six months of the financial year remain. Overrun risk flagged."],
    ["Utilities", "Up 14% year on year", "Driven by HVAC runtime at [PROPERTY B]."],
    ["Marketing", "18% under budget at [PROPERTY A]",
     "KWD 47,000 unspent. Not yet reallocated."],
    ["Contract labour", "In line with budget", "No variances to report."],
], [32*mm, 48*mm, 90*mm]))
E.append(Spacer(1, 6))
E.append(Paragraph(
 "The maintenance position is the item most likely to require a budget variation before year end. "
 "The overrun is concentrated in reactive callouts rather than planned works, which is itself a "
 "signal: the planned-maintenance programme is not preventing the failures it exists to prevent.", BODY))

# ───────────────────────── 5. construction
E.append(Paragraph("5.  Construction — [PROPERTY C]", H1))
E.append(table([
    ["Item", "Position"],
    ["Programme status", "Three weeks behind programme."],
    ["Cause", "Late joinery delivery. Joinery delivered to site 2 June 2026."],
    ["Fit-out duration", "Contractor requires six weeks from joinery delivery to practical completion."],
    ["Revised handover date", "10 July 2026"],
    ["Cost impact", "KWD 18,000 against a KWD 25,000 contingency allowance."],
    ["Contractor", "[CONTRACTOR B] — performance review outstanding."],
], [42*mm, 128*mm]))
E.append(Spacer(1, 6))
E.append(Paragraph(
 "The revised date has been <b>proposed</b> to the Board and communicated to the tenant verbally. It "
 "has not been ratified by the Board, and it has not been confirmed to the tenant in writing. Leasing "
 "advise that the tenant has a fit-out crew booked and is paying storage costs in the interim; if the "
 "date slips again, a request for rent-free compensation is expected.", BODY))

# ───────────────────────── 6. risk register
E.append(Paragraph("6.  Maintenance detail", H1))
E.append(table([
    ["Category", "Open tickets", "Older than 30 days", "Average days to close"],
    ["HVAC", "17", "5", "14"],
    ["Plumbing", "9", "2", "9"],
    ["Lifts", "7", "3", "21"],
    ["Lighting", "5", "1", "6"],
    ["Other", "2", "0", "4"],
    ["<b>Total</b>", "<b>40</b>", "<b>11</b>", "<b>12 (blended)</b>"],
], [46*mm, 34*mm, 44*mm, 46*mm], align_right=(1,2,3), band_rows=(6,)))
E.append(Paragraph("Table 6.1 — Open maintenance tickets at 30 June 2026. Service standard is five days to close.", CAP))
E.append(Spacer(1, 8))
E.append(Paragraph(
 "The blended average of twelve days is more than double the five-day service standard, and the lift "
 "category is the worst performer at twenty-one days. Tenant complaints logged this month reached 23, "
 "against 9 the previous month. Two contractors are behind schedule; one has not attended site for "
 "eight days and has not responded to two written requests.", BODY))

E.append(Paragraph("7.  Tenant matters and escalations", H1))
E.append(table([
    ["Ref", "Tenant", "Asset", "Matter", "Position"],
    ["E-01", "[TENANT 1]", "[PROPERTY B]", "Lift reliability", "Requesting a service credit."],
    ["E-02", "[TENANT 2]", "[PROPERTY A]", "Upper-floor footfall", "Seeking a rent review at renewal."],
    ["E-03", "[TENANT 3]", "[PROPERTY C]", "Handover delay", "Storage costs accruing; expects compensation."],
], [15*mm, 28*mm, 30*mm, 38*mm, 59*mm]))
E.append(Spacer(1, 6))
E.append(Paragraph(
 "None of the three escalations has yet received a written response. Leasing consider E-02 the most "
 "commercially significant, as the tenant occupies 620 sqm across two upper-floor units and its lease "
 "is one of the three expiring within 90 days.", BODY))

E.append(Paragraph("8.  Health, safety and compliance", H1))
for b in [
 "Annual fire system inspection completed 12 May 2026 at both operating assets. No major findings. "
 "Two minor observations raised and closed within the quarter.",
 "Statutory lift inspection at [PROPERTY B] falls due 30 September 2026. Not yet scheduled.",
 "Two contractor site inductions are overdue at [PROPERTY C].",
 "No reportable safety incidents during the quarter.",
 "Insurance renewal documentation submitted on time. No change to premium indicated.",
]:
    E.append(Paragraph(b, BULL, bulletText="\u2013"))

E.append(Paragraph("9.  Risk register", H1))
E.append(table([
    ["Ref", "Risk", "Impact", "Likelihood"],
    ["R-01", "Maintenance backlog: 11 tickets older than 30 days.", "Medium", "High"],
    ["R-02", "North lift at [PROPERTY B] failed four times this month. Parts on three-week lead time.",
     "High", "High"],
    ["R-03", "Five units at [PROPERTY A] vacant more than nine months.", "Medium", "Certain"],
    ["R-04", "Tenant at [PROPERTY C] may request two weeks rent-free if handover slips again.",
     "Medium", "Medium"],
    ["R-05", "Portfolio collateral valuations are 27 months old.", "High", "Certain"],
    ["R-06", "Two contractors behind schedule; one absent from site for eight days.", "Medium", "High"],
], [16*mm, 106*mm, 24*mm, 24*mm]))

# ───────────────────────── 7. action log
E.append(Paragraph("10.  Action log", H1))
E.append(table([
    ["Ref", "Action", "Owner", "Due", "Status"],
    ["A-01", "Confirm revised handover date to tenant in writing", "[PROJECT MANAGER]", "18 Jul 2026", "Open"],
    ["A-02", "Contractor performance review with [CONTRACTOR B]", "[FACILITIES LEAD]", "22 Jul 2026", "Open"],
    ["A-03", "Order replacement lift parts", "[FACILITIES LEAD]", "8 Jun 2026", "Closed"],
    ["A-04", "Commission portfolio collateral revaluation", "[FINANCE MANAGER]", "30 Sep 2026", "Open"],
    ["A-05", "Upper-floor leasing incentive proposal", "[LEASING MANAGER]", "31 Jul 2026", "Open"],
    ["A-06", "Review payment plans for two tenants", "[FINANCE MANAGER]", "15 Aug 2026", "Open"],
    ["A-07", "Reallocate unspent marketing budget", "TBC", "30 Jun 2026", "Open"],
], [15*mm, 68*mm, 37*mm, 26*mm, 24*mm]))

# ───────────────────────── 8. narrative
E.append(Paragraph("11.  Management narrative and outlook", H1))
E.append(Paragraph(
 "“The quarter reflects sector-wide conditions rather than asset-specific weakness. Vacancy at "
 "[PROPERTY A] is concentrated on the upper floor, and the new food-and-beverage signing is expected "
 "to lift footfall and support upper-floor leasing from next quarter. Collections remain healthy and "
 "the two payment plans are performing.”", BODY))
E.append(Paragraph(
 "“On costs, the maintenance position is understood and a contractor performance meeting is "
 "scheduled. We do not currently anticipate requesting a budget variation. On [PROPERTY C], the "
 "programme is recovered and handover is secured within contingency.”", BODY))
E.append(Spacer(1, 4))
E.append(Paragraph(
 "Recommendation from [FACILITIES LEAD]: hold the asking rate at [PROPERTY A], redirect the unspent "
 "marketing budget to upper-floor incentives, and bring the collateral revaluation forward into this "
 "quarter rather than next.", BODY))

E.append(Paragraph("12.  Priorities for next quarter", H1))
for b in [
 "Resolve the maintenance backlog to under five tickets older than 30 days.",
 "Secure and confirm the [PROPERTY C] handover date in writing.",
 "Bring the collateral revaluation forward from Q4 into Q3.",
 "Respond in writing to all three tenant escalations.",
 "Decide the upper-floor incentive position at [PROPERTY A] before the three expiring leases lapse.",
]:
    E.append(Paragraph(b, BULL, bulletText="\u2013"))

E += rule(12, 4)
E.append(Paragraph(
 "This document was written for training. Every entity, figure, date and quotation in it is invented. "
 "It is not a real portfolio, and it should not be treated as a model of correct reporting — it "
 "contains deliberate errors.", NOTE))

doc.build(E, onFirstPage=chrome, onLaterPages=chrome)
print("wrote", OUT)

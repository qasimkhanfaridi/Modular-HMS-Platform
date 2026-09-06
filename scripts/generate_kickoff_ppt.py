"""Generate PulseCore HMS team kickoff PowerPoint."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
import os

OUTPUT = r"C:\Users\Faridi\Project\AAQSOLS\Modular-HMS-Platform\PulseCore-HMS-Team-Kickoff.pptx"
OUTPUT_ALT = r"C:\Users\Faridi\Project\AAQSOLS\Modular-HMS-Platform\PulseCore-HMS-Team-Kickoff-NEW.pptx"

# Colors
DARK_BLUE = RGBColor(0x1B, 0x3A, 0x5C)
ACCENT_RED = RGBColor(0xC0, 0x39, 0x2B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xF5, 0xF5, 0xF5)
DARK_GRAY = RGBColor(0x33, 0x33, 0x33)
TEAL = RGBColor(0x1A, 0xBC, 0x9C)


def set_slide_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_title_slide(prs, title, subtitle):
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    set_slide_bg(slide, DARK_BLUE)
    box = slide.shapes.add_textbox(Inches(0.8), Inches(2.2), Inches(8.4), Inches(1.5))
    tf = box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER
    box2 = slide.shapes.add_textbox(Inches(0.8), Inches(3.8), Inches(8.4), Inches(1.2))
    tf2 = box2.text_frame
    p2 = tf2.paragraphs[0]
    p2.text = subtitle
    p2.font.size = Pt(20)
    p2.font.color.rgb = RGBColor(0xBB, 0xCC, 0xDD)
    p2.alignment = PP_ALIGN.CENTER


def add_section_slide(prs, title):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, ACCENT_RED)
    box = slide.shapes.add_textbox(Inches(0.8), Inches(2.8), Inches(8.4), Inches(1.2))
    tf = box.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER


def add_content_slide(prs, title, bullets, sub=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, WHITE)
    # Title bar
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(1.1))
    bar.fill.solid()
    bar.fill.fore_color.rgb = DARK_BLUE
    bar.line.fill.background()
    tb = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(9), Inches(0.8))
    tp = tb.text_frame.paragraphs[0]
    tp.text = title
    tp.font.size = Pt(28)
    tp.font.bold = True
    tp.font.color.rgb = WHITE

    body = slide.shapes.add_textbox(Inches(0.6), Inches(1.4), Inches(8.8), Inches(5.5))
    tf = body.text_frame
    tf.word_wrap = True
    for i, b in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = b
        p.font.size = Pt(18)
        p.font.color.rgb = DARK_GRAY
        p.space_after = Pt(10)
        p.level = 0
        if b.startswith("  "):
            p.level = 1
            p.font.size = Pt(16)

    if sub:
        sb = slide.shapes.add_textbox(Inches(0.6), Inches(6.5), Inches(8.8), Inches(0.6))
        sp = sb.text_frame.paragraphs[0]
        sp.text = sub
        sp.font.size = Pt(14)
        sp.font.italic = True
        sp.font.color.rgb = ACCENT_RED


def add_table_slide(prs, title, headers, rows):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, WHITE)
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(10), Inches(1.1))
    bar.fill.solid()
    bar.fill.fore_color.rgb = DARK_BLUE
    bar.line.fill.background()
    tb = slide.shapes.add_textbox(Inches(0.5), Inches(0.2), Inches(9), Inches(0.8))
    tp = tb.text_frame.paragraphs[0]
    tp.text = title
    tp.font.size = Pt(26)
    tp.font.bold = True
    tp.font.color.rgb = WHITE

    cols = len(headers)
    table = slide.shapes.add_table(len(rows) + 1, cols, Inches(0.4), Inches(1.3), Inches(9.2), Inches(0.4 * (len(rows) + 2))).table
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = DARK_BLUE
        for p in cell.text_frame.paragraphs:
            p.font.bold = True
            p.font.size = Pt(13)
            p.font.color.rgb = WHITE
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = table.cell(ri + 1, ci)
            cell.text = str(val)
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(12)
                p.font.color.rgb = DARK_GRAY
            if ri % 2 == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT_GRAY


def build():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # 1 Title
    add_title_slide(prs,
        "PulseCore HMS",
        "Modular Hospital Management System\nTeam Kickoff | AAQSOLS | August 2026")

    # 2 Agenda
    add_content_slide(prs, "Today's Agenda", [
        "What is PulseCore HMS?",
        "Why modular? Why clinic-first?",
        "Packages we sell (PKG-A to PKG-F)",
        "22 modules — how they connect",
        "Pricing overview",
        "Clinic → RIC roadmap",
        "Team roles & next steps",
    ])

    # 3 Problem
    add_section_slide(prs, "The Problem")

    add_content_slide(prs, "Why We Built This", [
        "Small heart clinics use paper records — no digital MR, no reports",
        "Full HMS systems are too expensive (PKR 10M+) for small clinics",
        "Existing HMS = all-or-nothing — pay for everything even if you need OPD only",
        "RIC needs 60+ departments but can't risk untested software",
        "General hospitals don't need Cath Lab — but vendors force them to buy it",
        "",
        "Our answer: Modular HMS — buy what you need, add later, same platform",
    ])

    # 4 Solution
    add_section_slide(prs, "The Solution")

    add_content_slide(prs, "One Platform — Every Size", [
        "PulseCore HMS = modular microservices platform",
        "22 separate modules — each works independently",
        "M00 Core is mandatory — everything connects through it",
        "Enable new module = license key — NO reinstall, NO migration",
        "Same code runs at:",
        "  → Small 2-room heart clinic (PKG-A)",
        "  → 50-bed general hospital (PKG-C)",
        "  → RIC enterprise — 60 departments (PKG-F)",
    ], sub="Folder: C:\\Users\\Faridi\\Project\\AAQSOLS\\Modular-HMS-Platform\\")

    # 5 One diagram slide
    add_content_slide(prs, "Growth Path — Same Software", [
        "STEP 1:  PKG-A  →  Small Heart Clinic     (PKR 25K/month)",
        "STEP 2:  PKG-B  →  Clinic + Lab + Pharmacy (PKR 55K/month)",
        "STEP 3:  PKG-C  →  Small Hospital 20-50 beds (PKR 120K/month)",
        "STEP 4:  PKG-D  →  General Hospital 50-150 beds (PKR 250K/month)",
        "STEP 5:  PKG-E  →  Cardiac Hospital 100-250 beds (PKR 450K/month)",
        "STEP 6:  PKG-F  →  RIC Enterprise 60+ depts (PKR 1.2M/month)",
        "",
        "Customer never changes system — only adds modules",
    ])

    # 6 Packages table
    add_section_slide(prs, "What We Sell")

    add_table_slide(prs, "Deployment Packages",
        ["Package", "Customer", "Modules", "Monthly"],
        [
            ["PKG-A ⭐ START", "Heart clinic 1-3 doctors", "5", "PKR 25,000"],
            ["PKG-B", "Heart clinic + echo/lab", "11", "PKR 55,000"],
            ["PKG-C", "Small hospital 20-50 beds", "12", "PKR 120,000"],
            ["PKG-D", "General hospital", "16", "PKR 250,000"],
            ["PKG-E", "Cardiac hospital", "18", "PKR 450,000"],
            ["PKG-F", "RIC / Enterprise", "22 (ALL)", "PKR 1,200,000"],
        ])

    # 7 PKG-A detail
    add_content_slide(prs, "PKG-A — Where We START ⭐", [
        "Target: Small heart clinic, 1-3 doctors, 20-80 patients/day",
        "",
        "Included modules:",
        "  M00 Core Platform (auth, licensing, audit)",
        "  M01 Patient Registration (MR number, CNIC, photo)",
        "  M02 OPD (cardiology consultation templates)",
        "  M05 Appointments (booking, queue, tokens)",
        "  M08 Cardiology (ECG, risk scores, cardiac history)",
        "",
        "Install time: 2 weeks | Year 1 cost: ~PKR 800,000",
        "First sales target: 5 clinics in Rawalpindi / Islamabad / Lahore",
    ])

    # 8 Modules
    add_section_slide(prs, "22 Modules")

    add_table_slide(prs, "Module Overview (Part 1)",
        ["ID", "Module", "Heart Only?", "In PKG-A?"],
        [
            ["M00", "Core Platform", "No — always required", "✅"],
            ["M01", "Patient Registration", "No", "✅"],
            ["M02", "OPD", "No — templates vary", "✅"],
            ["M03", "Pharmacy", "No", "❌ PKG-B"],
            ["M04", "Laboratory", "No", "❌ PKG-B"],
            ["M05", "Appointments", "No", "✅"],
            ["M06", "Billing", "No", "❌ PKG-B"],
            ["M07", "Medical Records", "No", "❌ PKG-B"],
            ["M08", "Cardiology", "✅ Yes", "✅"],
            ["M09", "Echo", "✅ Yes", "❌ PKG-B"],
            ["M10", "Emergency", "No", "❌ PKG-C"],
        ])

    add_table_slide(prs, "Module Overview (Part 2)",
        ["ID", "Module", "Heart Only?", "First Package"],
        [
            ["M11", "IPD / Beds", "No", "PKG-C"],
            ["M12", "ICU / CCU", "Partial", "PKG-E"],
            ["M13", "Radiology", "No", "PKG-C"],
            ["M14", "OT / Surgery", "No", "PKG-D"],
            ["M15", "Cath Lab", "✅ Yes", "PKG-E"],
            ["M16", "Nursing", "No", "PKG-C"],
            ["M17", "HR / Admin", "No", "PKG-D"],
            ["M18", "Finance / Purchase", "No", "PKG-D"],
            ["M19", "Reports / Analytics", "No", "PKG-B"],
            ["M20", "Telemedicine", "No", "PKG-D"],
            ["M21", "Quality / ISO", "No", "PKG-F only"],
        ])

    # 9 Non-heart
    add_content_slide(prs, "Selling to NON-Heart Hospitals Too", [
        "Same platform — different configuration",
        "",
        "Heart clinic:     Enable M08, M09 | Disable M15 until hospital scale",
        "General hospital: Disable M08, M09, M15 | Use general OPD templates",
        "Dental clinic:    M00 + M01 + M02 + M05 + M06 only",
        "Eye clinic:       M00 + M01 + M02 + M05 + M13 (lite)",
        "Lab center:       M00 + M01 + M04 + M06 (no doctor needed)",
        "",
        "No separate product — just enable/disable modules + change templates",
    ])

    # 10 Pricing
    add_section_slide(prs, "Pricing")

    add_table_slide(prs, "Year 1 Investment by Package",
        ["Package", "License/yr", "Implementation", "Infra", "Year 1 Total"],
        [
            ["PKG-A ⭐", "250,000", "150,000", "400,000", "~800,000"],
            ["PKG-B", "550,000", "300,000", "800,000", "~1.65M"],
            ["PKG-C", "1,200,000", "800,000", "2,500,000", "~4.5M"],
            ["PKG-D", "2,500,000", "1,500,000", "8,000,000", "~12M"],
            ["PKG-E", "4,500,000", "3,000,000", "25,000,000", "~32.5M"],
            ["PKG-F (RIC)", "12,000,000", "8,000,000", "55,000,000", "~35M*"],
        ])
    add_content_slide(prs, "Pricing Notes", [
        "* PKG-F (RIC) Year 1 = Wave 1-2 only — full deployment over 4 years",
        "Full RIC 5-year TCO: ~PKR 110 Million",
        "",
        "Clinic SaaS option: +20% monthly — we host, no server needed",
        "Government hospitals: 15-25% discount",
        "First 5 pilot clinics: 50% off Year 1 (in exchange for case study)",
        "",
        "Upsell example: Clinic on PKG-A adds Pharmacy → +PKR 8,000/month",
    ])

    # 11 Roadmap
    add_section_slide(prs, "Roadmap")

    add_table_slide(prs, "Clinic → RIC Timeline",
        ["Phase", "When", "Target", "Package"],
        [
            ["Phase 1", "Month 1-6", "3-5 heart clinics", "PKG-A"],
            ["Phase 2", "Month 6-12", "10 clinics (mix A/B)", "PKG-B"],
            ["Phase 3", "Year 2", "2-3 hospitals", "PKG-C/D"],
            ["Phase 4", "Year 2-3", "1 cardiac hospital", "PKG-E"],
            ["Phase 5", "Year 3-4", "RIC enterprise", "PKG-F"],
        ])

    add_content_slide(prs, "RIC — Why It Comes LAST", [
        "RIC = 60 departments, 800 users, 3,000 OPD/day",
        "HMIS tender active 2026 — but we need proof first",
        "",
        "Before RIC we must have:",
        "  ✅ 10+ clinics live on PKG-A/B",
        "  ✅ 1+ hospital live on PKG-C/D",
        "  ✅ 1 cardiac hospital on PKG-E",
        "",
        "RIC deployment = 6 waves over 16 months (NOT big-bang)",
        "Wave 1: OPD only → same module already running at clinics",
    ])

    # 12 Dev priority
    add_content_slide(prs, "Development Build Order", [
        "Priority 0 — Clinic MVP (sell PKG-A):",
        "  M00 Core → M01 Registration → M02 OPD → M05 Appointments → M08 Cardiology",
        "",
        "Priority 1 — Clinic Plus (PKG-B):",
        "  M03 Pharmacy → M04 Lab → M07 EMR → M09 Echo → M19 Reports",
        "",
        "Priority 2 — Hospital (PKG-C):",
        "  M10 Emergency → M11 IPD → M13 Radiology → M16 Nursing",
        "",
        "Priority 3-5 — Hospital → Cardiac → RIC",
        "  M12 ICU → M15 Cath Lab → M17-HR → M21 ISO",
    ])

    # 13 Team roles
    add_section_slide(prs, "Team Roles")

    add_table_slide(prs, "Who Does What",
        ["Role", "Start With", "First Action"],
        [
            ["Sales / BD", "docs/07 Sales Guide", "Find 3 heart clinics for PKG-A"],
            ["Developers", "docs/02 Module Catalog", "Build M00 + M01 + M02"],
            ["Install Team", "PKG-A README + Checklist", "Prepare clinic hardware list"],
            ["Manager", "docs/04 Roadmap + Pricing", "Approve pilot programme"],
            ["RIC Team", "ric-as-anchor-client.md", "Wait — focus on clinics first"],
        ])

    add_content_slide(prs, "What to Read — By Role", [
        "EVERYONE (20 min):",
        "  1. PulseCore-HMS-Platform-Overview.docx",
        "  2. README.md",
        "  3. docs/03-Deployment-Tiers.md",
        "",
        "Full guide: START-HERE.md (in Modular-HMS-Platform folder)",
        "",
        "All files: C:\\Users\\Faridi\\Project\\AAQSOLS\\Modular-HMS-Platform\\",
    ])

    # 14 Next steps
    add_section_slide(prs, "Next Steps")

    add_content_slide(prs, "Action Items — This Week", [
        "☐  Everyone reads START-HERE.md + Overview.docx",
        "☐  Sales: List 10 heart clinics in Rawalpindi/Islamabad",
        "☐  Sales: Prepare PKG-A pilot offer (50% off Year 1)",
        "☐  Dev: Set up M00 Core project (.NET 8 microservice)",
        "☐  Dev: Design MR number + patient registration schema",
        "☐  Install: Get PKG-A hardware quote (PKR 450K)",
        "☐  Manager: Schedule weekly progress meeting",
        "☐  Team meeting: Assign owners for each action",
    ])

    # 15 Q&A
    add_title_slide(prs, "Questions?", "PulseCore HMS — Clinic to Enterprise\nAAQSOLS | C:\\Users\\Faridi\\Project\\AAQSOLS\\Modular-HMS-Platform")

    try:
        prs.save(OUTPUT)
        print(OUTPUT)
    except PermissionError:
        prs.save(OUTPUT_ALT)
        print(OUTPUT_ALT)
        print("(Original file was open — saved as NEW copy)")


if __name__ == "__main__":
    build()

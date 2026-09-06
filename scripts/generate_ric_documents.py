"""
Generate three comprehensive RIC HMS documents.
"""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import os

OUTPUT_DIR = r"C:\Users\Faridi\Project\AAQSOLS"


def set_doc_defaults(doc):
    style = doc.styles["Normal"]
    font = style.font
    font.name = "Calibri"
    font.size = Pt(11)


def add_title(doc, text, level=0):
    if level == 0:
        p = doc.add_heading(text, level=0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        doc.add_heading(text, level=level)


def add_para(doc, text, bold=False, italic=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    return p


def add_bullets(doc, items):
    for item in items:
        doc.add_paragraph(item, style="List Bullet")


def add_numbered(doc, items):
    for item in items:
        doc.add_paragraph(item, style="List Number")


def add_table(doc, headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
        for p in hdr[i].paragraphs:
            for r in p.runs:
                r.bold = True
    for ri, row in enumerate(rows):
        cells = table.rows[ri + 1].cells
        for ci, val in enumerate(row):
            cells[ci].text = str(val)
    doc.add_paragraph()
    return table


# ─── Department master data ───────────────────────────────────────────────────
DEPARTMENTS = [
    # (name, category, size, primary_functions, hms_modules, connected_depts)
    ("Emergency / Chest Pain Unit", "Clinical", "Large",
     "24/7 cardiac emergency triage; AMI/STEMI/NSTEMI; stroke; heart failure; arrhythmia; Primary PCI; pulmonary embolism; unstable angina; aortic emergencies",
     "Emergency Module, Triage, ECG Integration, Bed Management, OT/Cath Lab Scheduling, Lab Orders, Radiology Orders, Admission, Discharge",
     "OPD, Cath Lab, ICU/CCU, Lab, Radiology, Pharmacy, Ambulance, Nursing"),
    ("OPD (Outdoor Patient Department)", "Clinical", "Large",
     "Patient registration; MR card issuance; ~1800-3000 patients/day; specialist clinics; follow-up; referral routing; HMIS-linked checkups",
     "Registration, Appointment, MR Number, Queue Management, Consultation Notes, Prescription, Referrals, Billing (if applicable)",
     "All diagnostic depts, Pharmacy, Lab, Echo, ETT, Medical Records, Home Delivery Programme"),
    ("Interventional Cardiology", "Clinical", "Large",
     "Angiography; angioplasty; stenting; complex PCI; IVUS/FFR interpretation workshops",
     "Procedure Scheduling, Cath Lab Integration, Pre/Post Procedure Notes, Device Inventory, Image Archival",
     "Cath Lab, Emergency, OPD, CCU, ICU, Radiology, Pharmacy"),
    ("Adult Cardiac Surgery", "Clinical", "Large",
     "CABG; valve replacement; adult congenital surgery; 1500-2000 surgeries/year; ~5 major surgeries/day",
     "Surgery Scheduling, Pre-op Assessment, OT Management, Post-op ICU Transfer, Consent, Implants Tracking",
     "OT, Anesthesia, Cardiac Surgical ICU, CCU, Echo, Lab, Blood Bank, Pharmacy, Rehabilitation"),
    ("Pediatric Cardiology", "Clinical", "Medium",
     "Diagnosis and management of congenital/acquired heart disease in children; fetal echo referrals",
     "Pediatric EMR, Growth Charts, Echo Orders, Surgery Referrals, PICU Transfers",
     "Echo, PICU, Pediatric Cardiac Surgery, OPD, Nuclear Cardiology"),
    ("Pediatric Cardiac Surgery", "Clinical", "Medium",
     "~400 pediatric cardiac surgeries/year; congenital heart defect repair",
     "Surgery Scheduling, Pediatric Pre-op, OT, PICU Bed Management, Parent Consent",
     "OT, PICU, Anesthesia, Echo, Blood Bank, Pharmacy"),
    ("Cardiac Catheterization Laboratory", "Clinical", "Large",
     "Diagnostic angiography; interventional procedures; Primary PCI; device implant coordination",
     "Cath Lab Workflow, DICOM/PACS Link, Procedure Logs, Radiation Dose Tracking, Inventory",
     "Interventional Cardiology, Electrophysiology, Emergency, Radiology, ICU/CCU"),
    ("Electrophysiology & Device Implantation", "Clinical", "Medium",
     "Arrhythmia management; pacemaker/ICD implantation; EP studies; ablation procedures",
     "Device Registry, Procedure Scheduling, Follow-up Clinic, Remote Monitoring Data",
     "Cath Lab, Echo, Emergency, OPD, ICU"),
    ("Coronary Care Unit (CCU)", "Clinical", "Large",
     "14-bed CCU; post-MI monitoring; unstable angina; arrhythmia management",
     "Bed Management, Vitals Monitoring, Medication Administration, Nursing Notes, Transfer Orders",
     "Emergency, Cath Lab, ICU, Lab, Pharmacy, Echo"),
    ("Cardiac Surgical ICU / Cardiac Care Units", "Clinical", "Large",
     "18-bed post-surgical ICU; ventilators; IABP; dialysis; TEE; bronchoscopy; 24/7 critical care",
     "ICU Charting, Ventilator Settings, Fluid Balance, Lab Orders, Transfer/Discharge",
     "Cardiac Surgery, OT, Anesthesia, Lab, Nephrology/Dialysis, Echo, Pharmacy"),
    ("Medical Intensive Care Unit (ICU)", "Clinical", "Large",
     "24-bed medical ICU; ventilator support; critical cardiac/medical patients",
     "ICU Management, Monitoring Integration, MAR, Ventilator Logs, Daily Rounds",
     "Emergency, CCU, Lab, Radiology, Pharmacy, Nephrology"),
    ("Pediatric Intensive Care Unit (PICU)", "Clinical", "Medium",
     "Critical care for pediatric cardiac patients post-surgery or acute illness",
     "Pediatric ICU Charting, Weight-based Dosing, Parent Communication, Transfer",
     "Pediatric Surgery, OT, Echo, Lab, Pharmacy"),
    ("Operation Theatres (4 OTs)", "Clinical", "Large",
     "Cardiac and thoracic surgeries; sterile environment; OT scheduling",
     "OT Scheduling, Checklist (WHO), Instrument Tracking, Anesthesia Record, Implants",
     "Cardiac Surgery, Anesthesia, CSSD, Blood Bank, ICU, Biomedical"),
    ("Cardiac Anesthesia", "Clinical", "Medium",
     "Pre-anesthesia assessment; intra-op anesthesia; post-op pain management",
     "Pre-anesthesia Forms, Anesthesia Record, Drug Administration, Recovery Room",
     "OT, ICU, Pharmacy, Lab"),
    ("General Medicine / GP Clinic", "Clinical", "Medium",
     "General assessment; preventive screening; referral to specialists",
     "Consultation, Vitals, Referrals, Basic Lab Orders",
     "OPD, Lab, Preventive Cardiology, All specialty clinics"),
    ("Preventive Cardiology", "Clinical", "Small",
     "Risk factor assessment; lifestyle counseling; disease prevention programmes",
     "Risk Scores, Lifestyle Plans, Follow-up Scheduling, Education Materials",
     "OPD, Nutrition, Rehabilitation, Lab, ETT"),
    ("Gynae/OBS (Cardiac Patients)", "Clinical", "Small",
     "Obstetric care for patients with cardiac conditions; high-risk pregnancy monitoring",
     "Maternal Cardiac Assessment, Fetal Echo Referrals, Multidisciplinary Notes",
     "Echo (Fetal), OPD, Lab, ICU, Anesthesia"),
    ("Nephrology & Dialysis", "Clinical", "Medium",
     "Renal care for cardiac patients; haemodialysis; renal replacement in ICU",
     "Dialysis Scheduling, Fluid Management, Lab Monitoring, ICU Integration",
     "ICU, Cardiac Surgical ICU, Lab, Pharmacy"),
    ("Psychiatry", "Clinical", "Small",
     "Mental health care for cardiac patients; anxiety/depression management post-diagnosis",
     "Psychiatric Assessment, Medication, Referrals, Counseling Notes",
     "Clinical Psychology, OPD, Pharmacy"),
    ("Clinical Psychology", "Clinical", "Small",
     "Behavioral therapy; cardiac rehabilitation psychology; patient counseling",
     "Session Notes, Assessment Scales, Referrals",
     "Psychiatry, Rehabilitation, OPD"),
    ("Dental (Cardiac Patients)", "Clinical", "Small",
     "Dental care with cardiac risk assessment; pre-surgical dental clearance",
     "Dental Records, Antibiotic Prophylaxis Protocols, Surgical Clearance",
     "Cardiac Surgery, OPD, Pharmacy"),
    ("Echocardiography (Echo Lab)", "Diagnostic", "Large",
     "TTE; TEE; fetal echo; stress echo; stereo echo; transthoracic and transesophageal studies",
     "Echo Orders, PACS Integration, Report Templates, Critical Findings Alerts",
     "OPD, Emergency, Cath Lab, Surgery, ICU, Pediatric Cardiology"),
    ("Nuclear Cardiology", "Diagnostic", "Medium",
     "SPECT imaging; perfusion/viability scans; Thallium scans; ejection fraction analysis; Siemens C-Cam gamma camera",
     "NM Orders, Dose Tracking, Image Analysis, Report Generation",
     "OPD, Cath Lab, Surgery, Radiology"),
    ("Radiology / Diagnostic Imaging", "Diagnostic", "Large",
     "X-ray; fluoroscopy; general imaging; reporting",
     "RIS/PACS, Order Management, Report Distribution, Critical Alerts",
     "Emergency, OPD, Cath Lab, Surgery, ICU, CT Unit"),
    ("CT Angiography Unit", "Diagnostic", "Medium",
     "5 CT angiography machines; cardiac CT; coronary imaging",
     "CT Scheduling, Contrast Protocols, DICOM Storage, Report Integration",
     "Radiology, Cath Lab, Emergency, OPD"),
    ("ETT (Exercise Tolerance Testing)", "Diagnostic", "Small",
     "Stress testing; exercise ECG; functional capacity assessment",
     "ETT Scheduling, Protocol Management, Report Templates",
     "OPD, Preventive Cardiology, Echo, Cath Lab"),
    ("Laboratory / Pathology (Main)", "Diagnostic", "Large",
     "150+ test parameters; cardiac-focused diagnostics; quality assurance; internal/external QA",
     "LIS Integration, Order-Result Workflow, QC Module, TAT Tracking, Critical Values",
     "All clinical departments, Blood Bank, Emergency, OPD, ICU"),
    ("Hematology & Blood Bank", "Diagnostic", "Medium",
     "CBC; coagulation; blood typing; transfusion services",
     "Blood Bank Module, Crossmatch, Inventory, Transfusion Records",
     "Surgery, Emergency, ICU, Lab"),
    ("Clinical Chemistry / Biochemistry", "Diagnostic", "Medium",
     "Cardiac enzymes; lipid profile; electrolytes; renal function; liver function",
     "Auto-analyzer Integration, Reference Ranges, Delta Checks",
     "Lab Main, Emergency, OPD, ICU"),
    ("Microbiology", "Diagnostic", "Small",
     "Culture and sensitivity; infection screening",
     "Microbiology LIS, Culture Tracking, Antibiotic Recommendations",
     "Lab, ICU, Infection Control, Surgery"),
    ("Serology", "Diagnostic", "Small",
     "Serological testing; infectious disease markers",
     "Serology Orders, Result Reporting",
     "Lab, Blood Bank, Surgery"),
    ("Special Chemistry", "Diagnostic", "Small",
     "Specialized cardiac and metabolic assays",
     "Special Test Catalog, Result Validation",
     "Lab Main, OPD, ICU"),
    ("Physiotherapy & Rehabilitation", "Therapeutic", "Medium",
     "Post-surgical rehab; cardiac rehabilitation; mobility restoration",
     "Rehab Plans, Session Tracking, Progress Notes, Discharge Recommendations",
     "Cardiac Surgery, ICU, OPD, Preventive Cardiology"),
    ("Nutrition & Dietetics", "Therapeutic", "Small",
     "Diet planning for cardiac patients; food quality oversight",
     "Diet Orders, Nutrition Assessment, Kitchen Integration",
     "OPD, ICU, Kitchen, Preventive Cardiology"),
    ("Pharmacy / Clinical Pharmacy", "Therapeutic", "Large",
     "Medication dispensing; OPD free medicines; CM Home Delivery Programme (99% enrolment); clinical pharmacy wards",
     "Pharmacy Inventory, E-Prescription, Dispensing, Home Delivery Tracking, Drug Interaction Alerts",
     "OPD, All wards, ICU, Lab, HMIS/PITB reporting"),
    ("Infection Control", "Support Clinical", "Small",
     "HAI prevention; protocol compliance; outbreak management",
     "Infection Surveillance, Incident Reporting, Audit Checklists",
     "All wards, Microbiology, CSSD, Housekeeping"),
    ("CSSD (Central Sterile Supply)", "Support Clinical", "Medium",
     "Sterilization of surgical instruments; OT supply",
     "Instrument Tracking, Sterilization Cycles, OT Dispatch",
     "OT, Biomedical, Infection Control"),
    ("Ambulance / Emergency Transport", "Support Clinical", "Medium",
     "Patient transport; emergency response coordination",
     "Dispatch Management, Trip Logs, GPS Tracking",
     "Emergency, OPD, Referral hospitals (HFH, BBGH)"),
    ("Nursing Administration", "Nursing", "Large",
     "800+ staff coordination; ward nursing; shift management; patient care standards",
     "Nursing Roster, Task Assignment, Nursing Notes, Handover, KPI Dashboard",
     "All clinical wards, ICU, OT, Emergency"),
    ("Medical Records / HMIS", "Nursing", "Medium",
     "MR card management; record archival; data integrity; PITB/SHC reporting",
     "EMR Archival, Record Retrieval, Audit Trail, Report Generation",
     "OPD, All departments, IT, Admin"),
    ("Patient Affairs / Social Welfare", "Nursing", "Small",
     "Patient grievances; financial assistance; counseling support",
     "Complaint Management, Welfare Case Tracking",
     "Admin, OPD, Medical Records"),
    ("Admin / Medical Superintendent Office", "Administrative", "Large",
     "Hospital governance; 800+ employee management; inter-department coordination; 24/7 operations oversight",
     "Dashboard, KPI Monitoring, Staff Management, Policy Distribution, Audit",
     "All departments, HR, Finance, IT"),
    ("Executive Director Office", "Administrative", "Large",
     "Strategic leadership; quality standards; external relations; ISO compliance",
     "Executive Dashboard, Quality Metrics, Board Reports",
     "Admin, Planning, Research, All clinical heads"),
    ("HR / Establishment", "Administrative", "Medium",
     "Recruitment; payroll; leave; performance; 285+ sanctioned posts historically",
     "HRMS Integration, Attendance, Leave, Payroll, Recruitment",
     "Admin, All departments"),
    ("Finance & Accounts", "Administrative", "Medium",
     "Budget management; expenditure; government fund accounting",
     "Financial Module, Budget Tracking, Expense Approval, Reports",
     "Purchase, Stores, Admin, All cost centers"),
    ("Purchase / Procurement", "Administrative", "Medium",
     "Tender management; vendor contracts; medical/surgical supplies procurement",
     "Procurement Module, Tender Tracking, Vendor Management, PO Generation",
     "Stores, Finance, Biomedical, Pharmacy, Lab"),
    ("Stores / Inventory", "Administrative", "Medium",
     "Central store; consumables; surgical supplies; Deputy MS Stores oversight",
     "Inventory Management, Stock Alerts, GRN, Issue Slips",
     "Purchase, Pharmacy, OT, CSSD, All wards"),
    ("Planning & Development", "Administrative", "Small",
     "PC-1 projects; expansion planning (470-bed project); infrastructure development",
     "Project Tracking, Budget Proposals, Milestone Reports",
     "Admin, Executive Director, Finance"),
    ("Legal / Audit", "Administrative", "Small",
     "Legal compliance; internal audit; regulatory adherence",
     "Audit Trail Review, Compliance Reports, Document Management",
     "Finance, Admin, Purchase"),
    ("Public Relations / Media", "Administrative", "Small",
     "Public communications; media relations; community awareness",
     "Announcement Module, Event Calendar",
     "Admin, Executive Director"),
    ("IT Department / HMIS & ERP", "Technical", "Medium",
     "HMIS development & maintenance; ERP; .NET/React systems; PITB integration; network infrastructure",
     "System Admin, User Management, Backup, Integration Hub, Help Desk Tickets",
     "All departments, Biomedical, Medical Records"),
    ("Biomedical Engineering", "Technical", "Medium",
     "Electromedical equipment maintenance; ventilators; CT; gamma camera; 100% uptime target",
     "Asset Management, PM Schedule, Breakdown Tickets, Calibration Records",
     "All clinical equipment users, Purchase, CSSD"),
    ("Maintenance / Engineering", "Technical", "Medium",
     "Building maintenance; HVAC; electrical; plumbing",
     "Maintenance Tickets, Asset Register, Preventive Maintenance",
     "Admin, Housekeeping, All departments"),
    ("Learning Resource Center (LRC)", "Education", "Small",
     "Medical training workshops; IVUS/FFR/MRI workshops; paramedical education",
     "Training Calendar, Workshop Registration, Resource Booking",
     "Medical Education, Library, All clinical departments"),
    ("Library", "Education", "Small",
     "Medical literature; research resources; journal access",
     "Catalog Management, Digital Resources",
     "Research, Medical Education, LRC"),
    ("Medical Education & Training", "Education", "Medium",
     "CPSP affiliation; house officer training; continuing medical education",
     "CME Tracking, Trainee Rotations, Evaluation Forms",
     "All clinical departments, LRC, Research"),
    ("Research Department", "Education", "Small",
     "Cardiac research; clinical trials; publications; evidenced-based practice",
     "Research Registry, Ethics Submissions, Data Collection",
     "All clinical departments, Library, Medical Education"),
    ("Quality Assurance / ISO Compliance", "Education", "Small",
     "ISO healthcare quality certification (2026); process audits; quality improvement",
     "Audit Checklists, NCR Management, Quality Dashboards, CAPA",
     "All departments, Infection Control, Admin"),
    ("Housekeeping / Sanitation", "General Services", "Medium",
     "Ward cleaning; waste management; hygiene standards",
     "Cleaning Schedules, Waste Logs, Inspection Checklists",
     "Infection Control, All wards"),
    ("Security", "General Services", "Medium",
     "Hospital security; access control; emergency response",
     "Access Logs, Incident Reports, Visitor Management",
     "Admin, Emergency, All entry points"),
    ("Kitchen / Diet Kitchen", "General Services", "Medium",
     "Patient meal preparation; dietary compliance",
     "Meal Orders from Nutrition, Production Planning",
     "Nutrition, Wards, ICU"),
    ("Telemedicine / Referral Coordination", "Clinical", "Medium",
     "Telemedicine services; MoU with HFH & BBGH; post-stent/surgery observation transfers; district cardiac unit guidelines",
     "Teleconsult Module, Referral Tracking, MoU Patient Transfer, Remote Monitoring",
     "Emergency, Cath Lab, Surgery, OPD, Ambulance"),
]


def generate_doc1():
    doc = Document()
    set_doc_defaults(doc)

    add_title(doc, "Proposal for Hospital Management System (HMS) Development")
    add_para(doc, "Submitted to: Rawalpindi Institute of Cardiology (RIC)", bold=True)
    add_para(doc, "Submitted by: AAQSOLS", bold=True)
    add_para(doc, "Document Version: 2.0 | Date: August 2026", italic=True)
    add_para(doc, "Classification: Comprehensive Proposal — Enhanced Edition")
    doc.add_page_break()

    # 1. Executive Summary
    add_title(doc, "1. Executive Summary", 1)
    add_para(doc,
        "This document presents a comprehensive proposal for the development, deployment, and maintenance of a "
        "next-generation Hospital Management System (HMS) tailored specifically for the Rawalpindi Institute "
        "of Cardiology (RIC). RIC is a 272-bed (expanding to 742 beds) tertiary cardiac care facility serving "
        "patients from Rawalpindi Division, Khyber Pakhtunkhwa, Azad Kashmir, Gilgit-Baltistan, and broader Punjab.")
    add_para(doc,
        "RIC currently operates approximately 60 departments and units — ranging from large clinical departments "
        "such as Emergency, OPD, Cath Lab, and Cardiac Surgery to smaller support units including Library, "
        "Infection Control, and Clinical Psychology. The hospital handles 1,800–3,000 OPD patients daily, up to "
        "500 emergency cases daily, 1,500–2,000 cardiac surgeries annually, and maintains 800+ administrative and "
        "clinical staff.")
    add_para(doc,
        "RIC already uses a basic HMIS (linked to OPD MR cards and Punjab PITB/SHC&MED reporting). A formal "
        "tender for 'Development & Maintenance Contract of HMIS for RIC' was published in 2026, signaling the "
        "institute's commitment to modernizing its digital infrastructure. This proposal builds upon that foundation "
        "to deliver a fully integrated, scalable, secure HMS covering all 60 departments.")

    # 2. About RIC
    add_title(doc, "2. Institutional Profile — Rawalpindi Institute of Cardiology", 1)
    add_table(doc,
        ["Attribute", "Details"],
        [
            ["Full Name", "Rawalpindi Institute of Cardiology (RIC)"],
            ["Location", "Rawal Road, Rawalpindi, Punjab, Pakistan"],
            ["Established", "September 2012 (Construction: June 2010)"],
            ["Type", "Non-profit, Public/Government Tertiary Cardiac Hospital"],
            ["Bed Capacity", "272 beds (expansion project: +470 beds, PC-1 Rs 7.5 billion)"],
            ["Emergency Beds", "48 beds"],
            ["ICU", "24 beds"],
            ["CCU", "14 beds"],
            ["Cardiac Surgical ICU", "18 beds"],
            ["Operation Theatres", "4"],
            ["Ventilators", "26 medical ventilators"],
            ["CT Angiography", "5 machines"],
            ["Daily OPD Load", "1,800 – 3,000 patients"],
            ["Daily Emergency Load", "Up to 500 patients"],
            ["Annual Surgeries", "1,500 – 2,000 (incl. ~400 pediatric)"],
            ["Departments/Units", "~60 (clinical, diagnostic, admin, support)"],
            ["Staff", "800+ employees (Admin dept.); 285 sanctioned posts at inception"],
            ["Executive Director", "Prof. Dr. Musfireh Siddiqeh (Cardiac Surgeon)"],
            ["Medical Superintendent", "Dr. Qurban Hussain Khan (Cardiac Electrophysiologist)"],
            ["Affiliation", "College of Physicians & Surgeons of Pakistan (CPSP)"],
            ["Certification", "ISO Healthcare Quality Management (May 2026)"],
            ["Website", "www.ric.gop.pk | ihc.ric.gop.pk"],
            ["Contact", "+92-51-9281111-9 | info@ricgop.online"],
        ])

    add_title(doc, "2.1 Current Digital Infrastructure", 2)
    add_bullets(doc, [
        "OPD fully computerized and linked to existing HMIS system",
        "MR (Medical Record) cards issued with unique MR numbers for every patient",
        "Integration with Punjab SHC&MED/PITB for provincial health reporting",
        "CM Medicine Home-Delivery Programme — RIC achieved 99% enrolment (highest among 10 Punjab cardiac institutes, June 2026)",
        "13,018 new OPD patients registered in June 2026 reporting period",
        "Telemedicine services and referral MoUs with Holy Family Hospital (HFH) and Benazir Bhutto General Hospital (BBGH)",
        "Active HMIS development & maintenance tender (2026)",
    ])

    add_title(doc, "2.2 Key Challenges Driving HMS Need", 2)
    add_bullets(doc, [
        "Extreme patient load exceeding physical capacity (3,000 OPD/day vs. 272 beds)",
        "Incomplete 470-bed expansion project creating operational pressure",
        "Need for new OPD block (proposed separate building)",
        "Limited inter-department data sharing beyond basic HMIS",
        "Manual or semi-automated workflows in ICU, OT, Cath Lab, and Pharmacy",
        "Growing requirement for provincial/national reporting (PITB, ISO audits)",
        "Referral coordination with partner hospitals (HFH, BBGH) needs digital tracking",
        "Home delivery programme scaling requires robust pharmacy-HMIS integration",
    ])

    # 3. Project Overview
    add_title(doc, "3. Project Overview & Objectives", 1)
    add_title(doc, "3.1 Primary Objective", 2)
    add_para(doc,
        "To develop a comprehensive, integrated Hospital Management System (HMS) that digitizes and streamlines "
        "operations across all ~60 departments at RIC, enhancing efficiency, patient safety, data security, "
        "and regulatory compliance while supporting future scalability.")

    add_title(doc, "3.2 Specific Objectives", 2)
    add_numbered(doc, [
        "Unified patient record accessible across all departments via MR number",
        "End-to-end digital workflows from registration to discharge and follow-up",
        "Real-time bed, OT, and Cath Lab availability management",
        "Integrated Laboratory Information System (LIS) with 150+ test parameters",
        "Radiology/PACS integration for imaging workflows",
        "E-prescription and pharmacy dispensing with home delivery tracking",
        "Role-based access control (RBAC) for 60+ departments and 800+ users",
        "Provincial reporting integration (PITB/SHC&MED)",
        "Executive dashboards and KPI monitoring for hospital leadership",
        "ISO-compliant audit trails and quality management support",
        "Telemedicine and inter-hospital referral module",
        "Mobile-responsive interfaces for ward and emergency use",
    ])

    add_title(doc, "3.3 Project Scope", 2)
    add_para(doc, "In Scope:", bold=True)
    add_bullets(doc, [
        "All 60 identified departments (see Section 4 and companion Document 2)",
        "Patient Registration, OPD, Emergency, IPD, ICU/CCU/PICU management",
        "Cath Lab, OT, and procedure management",
        "Laboratory, Radiology, Echo, Nuclear Medicine, ETT",
        "Pharmacy, Blood Bank, CSSD",
        "Nursing, Rehabilitation, Nutrition",
        "Administration: HR, Finance, Purchase, Stores",
        "IT infrastructure, HMIS maintenance, training, and 12-month post-go-live support",
    ])
    add_para(doc, "Out of Scope (Phase 1 — can be Phase 2):", bold=True)
    add_bullets(doc, [
        "Full ERP for non-clinical government accounting (can integrate via API)",
        "Biometric hardware procurement (integration supported)",
        "New hardware for lab analyzers (integration interfaces provided)",
    ])

    # 4. Department Landscape
    add_title(doc, "4. Department Landscape (~60 Units)", 1)
    add_para(doc,
        "RIC operates a diverse ecosystem of departments. The following table summarizes all identified units "
        "compiled from RIC official website, Wikipedia, appointment portal, news reports, and LinkedIn data.")

    categories = {}
    for d in DEPARTMENTS:
        categories.setdefault(d[1], []).append(d)

    for cat, depts in categories.items():
        add_title(doc, f"4.{list(categories.keys()).index(cat)+1} {cat} Departments", 2)
        rows = [[d[0], d[2], d[3][:80] + "..." if len(d[3]) > 80 else d[3]] for d in depts]
        add_table(doc, ["Department", "Size", "Primary Function"], rows)

    # 5. Team Structure
    add_title(doc, "5. Proposed Development Team Structure", 1)
    add_table(doc,
        ["Role", "Count", "Responsibility"],
        [
            ["Project Manager", "1", "Timeline, stakeholder coordination, delivery oversight"],
            ["Business Analyst", "1", "Requirements gathering across 60 departments, UAT coordination"],
            ["Solution Architect", "1", "System design, microservices architecture, integration design"],
            [".NET Backend Developers", "3-5", "API development, business logic, database services"],
            ["Frontend Developers (React.js)", "2-3", "Responsive UI, dashboards, ward interfaces"],
            ["Database Administrator", "1", "SQL Server design, optimization, backup/recovery"],
            ["UI/UX Designer", "1", "Intuitive interfaces for medical staff with minimal IT training"],
            ["QA Testers", "2-3", "Functional, regression, performance, security testing"],
            ["DevOps Engineer", "1", "CI/CD, Docker, deployment, monitoring"],
            ["Integration Specialist", "1", "LIS, PACS, lab analyzer, PITB API integration"],
            ["IT Help Desk", "2", "Post-launch support, user training, troubleshooting"],
        ])

    # 6. Execution Plan
    add_title(doc, "6. Project Execution Plan", 1)
    phases = [
        ("Phase 1: Discovery & Prototyping", "2-3 months", [
            "Stakeholder interviews across all 60 departments",
            "Current HMIS gap analysis and workflow mapping",
            "Department-functionality matrix finalization (Document 2)",
            "Clickable UI prototypes for OPD, Emergency, Lab, Pharmacy",
            "Technical architecture sign-off (Document 3)",
            "Data migration strategy for existing MR records",
        ]),
        ("Phase 2: Core Development", "6-8 months", [
            "Patient Registration & MR Management module",
            "OPD & Appointment module with queue management",
            "Emergency & Triage module",
            "IPD, Bed Management, ICU/CCU/PICU modules",
            "Laboratory Information System (LIS)",
            "Radiology/RIS/PACS integration",
            "Pharmacy & E-prescription module",
            "OT & Cath Lab scheduling modules",
            "Admin modules: HR, Finance, Purchase, Stores",
            "RBAC and audit trail implementation",
            "PITB/SHC&MED reporting integration",
        ]),
        ("Phase 3: Testing & UAT", "2-3 months", [
            "Unit and integration testing",
            "Department-wise UAT (all 60 units)",
            "Performance testing (3000 OPD/day simulation)",
            "Security penetration testing",
            "Data migration dry runs",
            "Staff training programme (see Section 8)",
        ]),
        ("Phase 4: Deployment & Support", "2-3 months", [
            "Phased go-live (Admin → OPD/Lab → Emergency/ICU → OT/Cath Lab)",
            "Parallel run with existing HMIS (2-4 weeks)",
            "Full cutover and legacy decommission",
            "12-month warranty and support",
            "Monthly review meetings with RIC leadership",
        ]),
    ]
    for name, duration, items in phases:
        add_title(doc, f"{name} ({duration})", 2)
        add_bullets(doc, items)

    # 7. Key Considerations
    add_title(doc, "7. Key Considerations for RIC", 1)
    considerations = [
        ("Security & Compliance",
         "HIPAA-equivalent data protection; role-based access for 60 departments; encryption at rest and in transit; "
         "audit logs for ISO compliance; session management; two-factor authentication for admin roles."),
        ("Scalability",
         "Designed for 800+ concurrent users, 3,000+ daily OPD transactions, 500 emergency cases/day; "
         "microservices architecture; load balancing; horizontal scaling for 742-bed future capacity."),
        ("User Experience",
         "Minimal-click workflows for emergency and ICU; Urdu/English interface option; large-font mode for older staff; "
         "tablet-compatible ward interfaces; offline-capable emergency module."),
        ("Integration",
         "PITB/SHC&MED provincial reporting; lab analyzer HL7/FHIR interfaces; PACS/DICOM for radiology; "
         "existing MR number continuity; telemedicine platform; partner hospital referral APIs (HFH, BBGH)."),
        ("High Availability",
         "99.9% uptime target; redundant database; automated backups every 4 hours; disaster recovery plan; "
         "on-premise primary with cloud backup option."),
        ("Maintenance & Enhancement",
         "Dedicated support team post-launch; quarterly feature releases; annual security audits; "
         "expansion module ready for 470-bed project."),
    ]
    for title, desc in considerations:
        add_title(doc, title, 2)
        add_para(doc, desc)

    # 8. Training
    add_title(doc, "8. Training & Change Management", 1)
    add_table(doc,
        ["User Group", "Training Duration", "Topics"],
        [
            ["OPD Registration Staff", "3 days", "Registration, MR cards, appointments, queue"],
            ["Doctors & Consultants", "2 days", "Consultation notes, orders, prescriptions, referrals"],
            ["Nursing Staff", "3 days", "Ward management, MAR, vitals, handover"],
            ["Lab & Radiology Techs", "2 days", "Order processing, result entry, QC"],
            ["Pharmacy Staff", "2 days", "Dispensing, inventory, home delivery"],
            ["ICU/OT/Cath Lab", "3 days", "Specialized workflows, scheduling, critical alerts"],
            ["Admin & Finance", "2 days", "Reports, procurement, HR modules"],
            ["IT Staff", "5 days", "System admin, troubleshooting, backup"],
            ["Train-the-Trainer", "5 days", "Internal champions for ongoing training"],
        ])

    # 9. Technologies
    add_title(doc, "9. Technologies & Tools", 1)
    add_table(doc,
        ["Layer", "Technology", "Rationale"],
        [
            ["Backend", ".NET 8, Entity Framework Core, JWT Auth", "Enterprise-grade; RIC IT team familiar with .NET"],
            ["Architecture", "Microservices, REST APIs, Message Queue", "Scalable; independent module deployment"],
            ["Frontend", "React.js, Redux, Material-UI / Ant Design", "Responsive; component-rich medical UI"],
            ["Mobile", "React Native (optional Phase 2)", "Ward rounds; emergency alerts"],
            ["Database", "SQL Server 2022, Redis Cache", "RIC standard; proven healthcare workloads"],
            ["Integration", "HL7 FHIR, DICOM, REST APIs", "Lab, PACS, provincial systems"],
            ["DevOps", "Azure DevOps / GitLab CI/CD, Docker", "Automated build, test, deploy"],
            ["Monitoring", "Application Insights / ELK Stack", "Performance and error tracking"],
            ["Reporting", "Power BI / SSRS", "Executive dashboards; PITB reports"],
            ["Security", "OAuth 2.0, RBAC, AES-256, TLS 1.3", "Healthcare data protection"],
        ])

    # 10. Team Size Options
    add_title(doc, "10. Team Size Impact on Timeline", 1)
    add_title(doc, "Option 1: Expanded Team (Faster Delivery)", 2)
    add_bullets(doc, [
        "Add 1-2 backend developers, 1 frontend developer, 1 QA tester",
        "Timeline reduction: 20-30% (total project: ~10-12 months vs 13-17 months)",
        "Higher cost; requires strong PM for coordination",
        "Recommended if RIC HMIS tender deadline is critical",
    ])
    add_title(doc, "Option 2: Standard Team (Balanced)", 2)
    add_bullets(doc, [
        "Team as defined in Section 5",
        "Timeline: 13-17 months total",
        "Optimal cost-quality balance",
    ])
    add_title(doc, "Option 3: Reduced Team (Budget-Conscious)", 2)
    add_bullets(doc, [
        "Remove 1 backend and 1 frontend developer",
        "Timeline extension: 20-30%",
        "Higher risk during UAT phase with 60 departments",
    ])

    # 11. Timeline
    add_title(doc, "11. Master Timeline", 1)
    add_table(doc,
        ["Phase", "Duration", "Months"],
        [
            ["Discovery & Prototyping", "2-3 months", "Month 1-3"],
            ["Core Development", "6-8 months", "Month 4-11"],
            ["Testing & UAT", "2-3 months", "Month 10-13"],
            ["Deployment & Support", "2-3 months", "Month 13-16"],
            ["Total (Standard Team)", "13-17 months", ""],
            ["Total (Expanded Team)", "10-12 months", ""],
        ])

    # 12. Success Metrics
    add_title(doc, "12. Success Metrics & KPIs", 1)
    add_table(doc,
        ["KPI", "Current Baseline", "Target (Post-HMS)"],
        [
            ["OPD registration time", "~10-15 min manual", "< 5 min digital"],
            ["Lab result TAT", "Variable", "30% reduction"],
            ["MR record retrieval", "Manual file search", "Instant digital access"],
            ["Pharmacy dispensing errors", "Unknown", "Near-zero with barcode"],
            ["Bed occupancy visibility", "Manual/board", "Real-time dashboard"],
            ["Home delivery tracking", "Partial HMIS", "100% tracked end-to-end"],
            ["Provincial report generation", "Manual export", "Automated daily sync"],
            ["System uptime", "N/A", "99.9%"],
            ["User adoption", "OPD only", "All 60 departments"],
        ])

    # 13. Conclusion
    add_title(doc, "13. Conclusion", 1)
    add_para(doc,
        "We propose a flexible, secure, and scalable HMS solution purpose-built for RIC's unique position as Punjab's "
        "leading public cardiac institute. With ~60 departments, 3,000 daily OPD patients, and ambitious expansion "
        "plans, RIC requires a system that not only digitizes today's workflows but grows with tomorrow's capacity.")
    add_para(doc,
        "Our experienced team — backed by detailed department-functionality mapping (Document 2) and technical "
        "architecture specification (Document 3) — is prepared to deliver high-quality results on time and provide "
        "ongoing support to ensure smooth operations post-launch.")
    add_para(doc,
        "We welcome the opportunity to present this proposal to RIC leadership and begin the discovery phase "
        "with department heads across the institute.")

    path = os.path.join(OUTPUT_DIR, "RIC Document 1 - Complete HMS Proposal.docx")
    doc.save(path)
    return path


def generate_doc2():
    doc = Document()
    set_doc_defaults(doc)

    add_title(doc, "RIC Hospital Management System")
    add_title(doc, "Document 2: Department–Functionality Mapping Matrix")
    add_para(doc, "Rawalpindi Institute of Cardiology (RIC) | Prepared by: AAQSOLS", bold=True)
    add_para(doc, "Version 2.0 | August 2026", italic=True)
    doc.add_page_break()

    add_title(doc, "1. Purpose", 1)
    add_para(doc,
        "This document maps all ~60 RIC departments to their primary functions, required HMS modules, "
        "connected departments, key workflows, user roles, and data flows. It serves as the functional "
        "requirements baseline for HMS development.")

    add_title(doc, "2. Legend", 1)
    add_table(doc,
        ["Symbol/Term", "Meaning"],
        [
            ["→", "Sends data/requests to"],
            ["←", "Receives data/results from"],
            ["↔", "Bidirectional integration"],
            ["Large", "High patient volume / critical hospital function"],
            ["Medium", "Moderate volume / specialized function"],
            ["Small", "Limited volume / support function"],
        ])

    add_title(doc, "3. Master Department-Functionality Matrix", 1)
    for i, d in enumerate(DEPARTMENTS, 1):
        name, cat, size, functions, modules, connected = d
        add_title(doc, f"3.{i} {name}", 2)
        add_table(doc,
            ["Attribute", "Detail"],
            [
                ["Category", cat],
                ["Operational Size", size],
                ["Primary Functions", functions],
                ["HMS Modules Required", modules],
                ["Connected Departments", connected],
            ])

        # Derive user roles
        roles = []
        if "Clinical" in cat or cat in ("Diagnostic", "Therapeutic", "Support Clinical"):
            roles.extend(["Doctor/Consultant", "Nurse", "Technician"])
        if "Administrative" in cat or cat == "Technical":
            roles.extend(["Admin Officer", "Manager"])
        if "Nursing" in cat:
            roles.extend(["Head Nurse", "Staff Nurse"])
        if "Education" in cat:
            roles.extend(["Trainer", "Trainee"])
        if "General" in cat:
            roles.extend(["Supervisor", "Staff"])
        roles = list(dict.fromkeys(roles))
        add_para(doc, f"Key User Roles: {', '.join(roles)}", bold=True)

        # Workflow summary
        add_para(doc, "Typical Workflow:", bold=True)
        if "Emergency" in name:
            add_numbered(doc, [
                "Patient arrives → Triage assessment → MR lookup/registration",
                "ECG/Vitals → Doctor assessment → Lab/Radiology orders",
                "Treatment decision → Cath Lab/ICU admission OR OPD referral OR Discharge",
                "Prescription → Pharmacy → Follow-up appointment",
            ])
        elif "OPD" in name:
            add_numbered(doc, [
                "Patient registration → MR card issuance → Queue assignment",
                "Vitals → Doctor consultation → Diagnostic orders",
                "Results review → Prescription/referral → Pharmacy/home delivery",
                "Follow-up scheduling → Medical record update",
            ])
        elif "Laboratory" in name or "Pathology" in name:
            add_numbered(doc, [
                "Receive orders from clinical departments → Sample collection",
                "Processing on automated equipment → Result validation",
                "Critical value alerts → Result delivery to ordering department",
                "QC logging → Provincial reporting sync",
            ])
        elif "Pharmacy" in name:
            add_numbered(doc, [
                "Receive e-prescription → Drug interaction check → Dispensing",
                "Inventory update → Home delivery marking (CM Programme)",
                "Delivery tracking → PITB reporting sync",
            ])
        elif "Cath" in name or "Interventional" in name:
            add_numbered(doc, [
                "Procedure order from Emergency/OPD → Scheduling",
                "Pre-procedure checklist → Procedure execution → Image capture",
                "Post-procedure notes → CCU/ward transfer → Follow-up scheduling",
            ])
        elif "Surgery" in name or "OT" in name:
            add_numbered(doc, [
                "Surgery booking → Pre-op assessment → Anesthesia clearance",
                "OT scheduling → Procedure → Post-op ICU transfer",
                "Recovery monitoring → Rehabilitation referral → Discharge planning",
            ])
        elif "ICU" in name or "CCU" in name or "PICU" in name:
            add_numbered(doc, [
                "Patient admission from Emergency/OT → Bed assignment",
                "Continuous monitoring → Medication administration → Lab orders",
                "Daily rounds documentation → Transfer to ward OR Discharge",
            ])
        elif "Admin" in name or "Executive" in name:
            add_numbered(doc, [
                "Dashboard monitoring → KPI review → Resource allocation",
                "Policy distribution → Inter-department coordination → Audit oversight",
            ])
        elif "IT" in name or "HMIS" in name:
            add_numbered(doc, [
                "System monitoring → User support tickets → Integration maintenance",
                "Backup verification → Security updates → New module deployment",
            ])
        else:
            add_numbered(doc, [
                f"Receive request from connected departments → Process {name} function",
                "Document in HMS → Return results/confirmation → Update patient record",
            ])
        doc.add_paragraph()

    # Inter-department connection summary
    add_title(doc, "4. Inter-Department Connection Map (Summary)", 1)
    add_para(doc,
        "The following table shows the primary data flows between major department clusters:")

    connections = [
        ["Patient Entry (OPD/Emergency)", "All Diagnostic Depts", "Orders (Lab, Echo, Radiology, ETT, Nuclear)"],
        ["Diagnostic Depts", "Clinical Depts", "Results & Reports"],
        ["Clinical Depts", "Pharmacy", "E-Prescriptions"],
        ["Emergency", "Cath Lab / ICU / CCU", "Emergency Procedures & Admissions"],
        ["OPD", "Specialty Clinics", "Referrals & Follow-ups"],
        ["Cardiac Surgery", "OT → ICU → Rehabilitation", "Surgical Care Pathway"],
        ["All Clinical", "Medical Records", "Patient Documentation"],
        ["All Departments", "Admin/Executive", "KPI Reports & Dashboards"],
        ["Pharmacy", "PITB/Provincial", "Home Delivery & OPD Reporting"],
        ["Lab", "PITB/Provincial", "Test Volume & Quality Reports"],
        ["RIC", "HFH / BBGH (Partner Hospitals)", "Referral & Post-procedure Transfers"],
        ["Biomedical", "All Equipment Users", "Asset Status & Maintenance Alerts"],
        ["Purchase/Stores", "All Departments", "Supply Requests & Inventory"],
        ["HR", "All Departments", "Staff Rosters & Attendance"],
        ["Quality/ISO", "All Departments", "Audit Findings & CAPA"],
    ]
    add_table(doc, ["Source", "Destination", "Data/Process Flow"], connections)

    add_title(doc, "5. HMS Module to Department Coverage", 1)
    module_map = {}
    for d in DEPARTMENTS:
        for mod in d[4].split(", "):
            module_map.setdefault(mod.strip(), []).append(d[0])

    rows = [[mod, str(len(depts)), ", ".join(depts[:5]) + ("..." if len(depts) > 5 else "")]
            for mod, depts in sorted(module_map.items(), key=lambda x: -len(x[1]))]
    add_table(doc, ["HMS Module", "# Depts", "Primary Departments"], rows[:30])

    path = os.path.join(OUTPUT_DIR, "RIC Document 2 - Department Functionality Matrix.docx")
    doc.save(path)
    return path


def generate_doc3():
    doc = Document()
    set_doc_defaults(doc)

    add_title(doc, "RIC Hospital Management System")
    add_title(doc, "Document 3: Modules, Workflows & Integration Specification")
    add_para(doc, "Rawalpindi Institute of Cardiology (RIC) | Prepared by: AAQSOLS", bold=True)
    add_para(doc, "Version 2.0 | August 2026", italic=True)
    doc.add_page_break()

    # 1. Architecture
    add_title(doc, "1. System Architecture Overview", 1)
    add_para(doc,
        "The RIC HMS follows a modular microservices architecture deployed on-premises at RIC data center "
        "with optional cloud backup. Each clinical and administrative domain operates as an independent service "
        "communicating via an API Gateway and Event Bus.")
    add_para(doc, "Architecture Layers:", bold=True)
    add_numbered(doc, [
        "Presentation Layer: React.js web application (desktop + tablet responsive)",
        "API Gateway: Authentication, rate limiting, routing, logging",
        "Microservices Layer: 15+ domain services (see Section 2)",
        "Integration Layer: HL7 FHIR, DICOM, REST adapters for external systems",
        "Data Layer: SQL Server (primary), Redis (cache), File Storage (DICOM/docs)",
        "Infrastructure Layer: Docker containers, CI/CD, monitoring, backup",
    ])

    add_title(doc, "1.1 Architecture Diagram (Textual)", 2)
    add_para(doc,
        "[Users: Doctors, Nurses, Admin, Lab Techs, Pharmacists]\n"
        "        ↓\n"
        "[React.js Frontend + Role-Based UI]\n"
        "        ↓\n"
        "[API Gateway — JWT Auth, RBAC, Rate Limiting]\n"
        "        ↓\n"
        "┌──────────────────────────────────────────────────────┐\n"
        "│  Microservices:                                      │\n"
        "│  Registration | OPD | Emergency | IPD | ICU          │\n"
        "│  Lab/LIS | Radiology/RIS | Pharmacy | OT | Cath Lab │\n"
        "│  Blood Bank | Nursing | HR | Finance | Purchase      │\n"
        "│  Reports | Notification | Audit | Integration Hub    │\n"
        "└──────────────────────────────────────────────────────┘\n"
        "        ↓                          ↓\n"
        "[SQL Server DB]          [External Systems]\n"
        "                          PITB | PACS | Lab Analyzers\n"
        "                          HFH/BBGH | Telemedicine")

    # 2. Core Modules
    add_title(doc, "2. Core HMS Modules — Detailed Specification", 1)

    modules_spec = [
        ("2.1 Patient Registration & MR Management", [
            ("Purpose", "Central patient identity management with MR number continuity from existing HMIS"),
            ("Features", "New registration; MR card printing; duplicate detection (CNIC/phone); "
             "demographics; insurance/govt scheme; photo capture; barcode/QR on MR card"),
            ("Users", "OPD registration staff, Emergency triage, Medical Records"),
            ("Integrations", "All modules (MR number as universal key); Existing HMIS data migration"),
            ("Departments Served", "OPD, Emergency, All clinical departments (60)"),
        ]),
        ("2.2 OPD & Appointment Management", [
            ("Purpose", "Manage 1,800-3,000 daily outpatient visits across specialty clinics"),
            ("Features", "Online/walk-in appointments; token queue; clinic routing; consultation templates; "
             "follow-up scheduling; no-show tracking; specialist roster"),
            ("Users", "Registration staff, Doctors, Nurses, Patients (online portal)"),
            ("Integrations", "Lab, Echo, Radiology, Pharmacy, Medical Records, PITB reporting"),
            ("Departments Served", "OPD, All OPD-based specialty clinics (15+)"),
        ]),
        ("2.3 Emergency & Triage", [
            ("Purpose", "24/7 emergency cardiac care for up to 500 patients/day"),
            ("Features", "ESI triage; fast-track STEMI pathway; ECG upload; vitals monitoring; "
             "Primary PCI activation; bed tracking (48 ED beds); ambulance pre-alert"),
            ("Users", "Emergency doctors, Triage nurses, Ambulance dispatch"),
            ("Integrations", "Cath Lab (STAT activation), Lab (STAT orders), ICU/CCU, Radiology"),
            ("Departments Served", "Emergency, Cath Lab, CCU, ICU, Lab, Ambulance"),
        ]),
        ("2.4 Inpatient & Bed Management", [
            ("Purpose", "Real-time bed tracking across 272 beds (future 742)"),
            ("Features", "Admission/discharge/transfer (ADT); bed board dashboard; ward census; "
             "expected discharge date; inter-ward transfers; partner hospital transfers (HFH, BBGH)"),
            ("Users", "Ward nurses, Admitting officers, Bed management coordinators"),
            ("Integrations", "Emergency, OT, ICU, CCU, PICU, Pharmacy, Billing"),
            ("Departments Served", "All inpatient wards, ICU, CCU, PICU, Cardiac Surgical ICU"),
        ]),
        ("2.5 ICU/CCU/PICU Management", [
            ("Purpose", "Critical care documentation and monitoring for 56+ critical beds"),
            ("Features", "ICU flow sheets; ventilator settings; IABP tracking; fluid balance; "
             "medication administration record (MAR); daily goals; scoring (APACHE/SOFA); "
             "dialysis integration; TEE reports"),
            ("Users", "Intensivists, ICU nurses, Respiratory therapists"),
            ("Integrations", "Lab (STAT), Pharmacy, Echo, Nephrology/Dialysis, OT"),
            ("Departments Served", "ICU (24 beds), CCU (14 beds), PICU, Cardiac Surgical ICU (18 beds)"),
        ]),
        ("2.6 Operation Theatre (OT) Management", [
            ("Purpose", "Scheduling and documentation for 4 OTs, ~5 surgeries/day"),
            ("Features", "Surgery scheduling; WHO checklist; anesthesia record; implant tracking; "
             "instrument count; post-op destination assignment; surgery logbook"),
            ("Users", "Surgeons, Anesthetists, OT nurses, CSSD staff"),
            ("Integrations", "CSSD, Blood Bank, ICU, Pharmacy, Biomedical"),
            ("Departments Served", "OT, Cardiac Surgery, Pediatric Cardiac Surgery, Anesthesia"),
        ]),
        ("2.7 Cath Lab Management", [
            ("Purpose", "Interventional cardiology procedure management"),
            ("Features", "Procedure scheduling; pre/post procedure notes; contrast log; "
             "radiation dose tracking; Primary PCI timer; device/stent inventory; DICOM storage"),
            ("Users", "Interventional cardiologists, Cath lab technicians, Nurses"),
            ("Integrations", "Emergency (STAT PCI), Echo, Radiology/PACS, CCU, Inventory"),
            ("Departments Served", "Cath Lab, Interventional Cardiology, Electrophysiology"),
        ]),
        ("2.8 Laboratory Information System (LIS)", [
            ("Purpose", "Manage 150+ test parameters across 7 lab sections"),
            ("Features", "Order-entry from all departments; barcode sample tracking; "
             "analyzer interfacing; result validation; critical value alerts; QC module; "
             "TAT monitoring; reflex testing; cumulative reports"),
            ("Users", "Lab technicians, Pathologists, Microbiologists"),
            ("Integrations", "All clinical departments, Blood Bank, PITB reporting"),
            ("Departments Served", "Lab/Pathology, Hematology, Biochemistry, Microbiology, Serology, Special Chemistry"),
        ]),
        ("2.9 Radiology / RIS / PACS", [
            ("Purpose", "Imaging workflow for X-ray, CT, Fluoroscopy, NM"),
            ("Features", "Exam ordering; scheduling (5 CT machines); DICOM storage; "
             "structured reporting; critical finding alerts; comparison priors; dose tracking"),
            ("Users", "Radiologists, Radiology technicians, Referring physicians"),
            ("Integrations", "PACS, Cath Lab, Echo, Nuclear Medicine, All ordering departments"),
            ("Departments Served", "Radiology, CT Angiography, Nuclear Cardiology, Echo"),
        ]),
        ("2.10 Pharmacy & Inventory", [
            ("Purpose", "Medication management and CM Home Delivery Programme"),
            ("Features", "E-prescription processing; drug interaction alerts; dispensing; "
             "inventory management; expiry tracking; home delivery marking & tracking; "
             " ward pharmacy; controlled drug register"),
            ("Users", "Pharmacists, Pharmacy assistants, Clinical pharmacists"),
            ("Integrations", "All prescribing departments, Stores, PITB/SHC&MED, Home delivery courier"),
            ("Departments Served", "Pharmacy, OPD, All wards, ICU, Emergency"),
        ]),
        ("2.11 Blood Bank", [
            ("Purpose", "Safe blood transfusion management"),
            ("Features", "Donor registration; blood grouping; crossmatch; issue/return; "
             "transfusion reaction reporting; inventory by blood group"),
            ("Users", "Blood bank technicians, Surgeons, ICU nurses"),
            ("Integrations", "Lab (Hematology), OT, Emergency, ICU"),
            ("Departments Served", "Blood Bank/Hematology, Surgery, Emergency, ICU"),
        ]),
        ("2.12 Nursing Management", [
            ("Purpose", "Coordinated nursing care across all wards"),
            ("Features", "Nursing assessments; care plans; shift handover; task lists; "
             "medication administration; vitals charting; incident reporting"),
            ("Users", "Head nurses, Staff nurses, Nurse managers"),
            ("Integrations", "All wards, Pharmacy (MAR), Lab, Doctor orders"),
            ("Departments Served", "Nursing Administration, All clinical wards"),
        ]),
        ("2.13 Rehabilitation & Allied Services", [
            ("Purpose", "Post-care recovery and supportive services"),
            ("Features", "Rehab session scheduling; progress tracking; diet orders; "
             "psychology session notes; dental records"),
            ("Users", "Physiotherapists, Dietitians, Psychologists, Dentists"),
            ("Integrations", "Cardiac Surgery, ICU, OPD, Kitchen"),
            ("Departments Served", "Rehabilitation, Nutrition, Psychology, Psychiatry, Dental"),
        ]),
        ("2.14 Administration & HR", [
            ("Purpose", "Hospital governance and human resource management"),
            ("Features", "Employee directory; attendance; leave management; payroll integration; "
             "organizational chart; policy documents; KPI dashboards"),
            ("Users", "Admin officers, HR staff, Department heads, Executive Director"),
            ("Integrations", "All departments (staff roster), Finance"),
            ("Departments Served", "Admin, HR, Executive Director Office"),
        ]),
        ("2.15 Finance, Purchase & Stores", [
            ("Purpose", "Financial and supply chain management"),
            ("Features", "Budget tracking; purchase requisitions; tender management; "
             "vendor database; GRN; stock management; reorder alerts; expense approval workflow"),
            ("Users", "Finance officers, Purchase officers, Store keepers"),
            ("Integrations", "All departments (supply requests), Pharmacy, Lab, OT"),
            ("Departments Served", "Finance, Purchase, Stores"),
        ]),
        ("2.16 Quality, Audit & ISO", [
            ("Purpose", "Support ISO 2026 certification and continuous quality improvement"),
            ("Features", "Audit scheduling; checklist management; NCR/CAPA tracking; "
             "incident reporting; infection surveillance dashboards; quality indicators"),
            ("Users", "Quality officers, Department heads, Infection control nurses"),
            ("Integrations", "All departments, Infection Control, Admin"),
            ("Departments Served", "Quality Assurance, Infection Control, All departments"),
        ]),
        ("2.17 Reporting & Analytics", [
            ("Purpose", "Executive and operational intelligence"),
            ("Features", "Real-time dashboards; OPD/emergency/surgery statistics; "
             "bed occupancy; lab TAT; pharmacy consumption; financial reports; "
             "PITB automated export; custom report builder"),
            ("Users", "Executive Director, Medical Superintendent, Department heads"),
            ("Integrations", "All modules, PITB/SHC&MED, Power BI"),
            ("Departments Served", "Executive Director, Admin, All department heads"),
        ]),
        ("2.18 Telemedicine & Referral", [
            ("Purpose", "Remote care and inter-hospital coordination"),
            ("Features", "Video consultation; referral creation; MoU patient tracking (HFH, BBGH); "
             "post-stent/surgery transfer documentation; district cardiac unit guidelines"),
            ("Users", "Doctors, Referral coordinators, Partner hospital staff"),
            ("Integrations", "OPD, Emergency, Cath Lab, Surgery, Ambulance"),
            ("Departments Served", "Telemedicine, Emergency, OPD, Partner hospitals"),
        ]),
    ]

    for title, specs in modules_spec:
        add_title(doc, title, 2)
        for label, content in specs:
            add_para(doc, f"{label}: ", bold=True)
            add_para(doc, content)

    # 3. Patient Journey Workflows
    add_title(doc, "3. End-to-End Patient Journey Workflows", 1)

    journeys = [
        ("3.1 OPD Patient Journey", [
            "Arrival → Registration desk (CNIC, history) → MR card issued/retrieved",
            "Token generated → Waiting area → Vitals station (BP, weight, pulse)",
            "Doctor consultation (specialty clinic) → Orders placed (Lab/Echo/ETT/Rx)",
            "Diagnostic departments process orders → Results auto-linked to MR",
            "Doctor review → Prescription finalized → Pharmacy dispensing",
            "Home delivery marked (CM Programme) → Follow-up date scheduled → Departure",
        ]),
        ("3.2 Emergency STEMI Pathway", [
            "Ambulance alert OR walk-in → Immediate triage → ECG within 10 min",
            "STEMI confirmed → MR registration (fast-track) → Cath Lab STAT activation",
            "Primary PCI performed → CCU/ICU admission → Post-procedure monitoring",
            "Lab orders (cardiac enzymes, coagulation) → Medication protocol initiated",
            "Stable → Transfer to ward OR Discharge with follow-up OPD appointment",
        ]),
        ("3.3 Cardiac Surgery Pathway", [
            "OPD/Emergency referral → Cardiac surgery clinic assessment",
            "Pre-op workup (Echo, Cath, Lab, Dental clearance, Anesthesia assessment)",
            "Surgery date allocated → OT scheduled → Blood reserved",
            "WHO checklist → Surgery performed → Cardiac Surgical ICU admission",
            "ICU recovery (ventilator weaning, monitoring) → Ward transfer",
            "Rehabilitation referral → Discharge planning → OPD follow-up",
        ]),
        ("3.4 Inpatient Admission & Discharge", [
            "Admission order (Emergency/OPD/OT) → Bed assigned → Nursing assessment",
            "Daily rounds → Orders (Lab, Rx, procedures) → MAR administration",
            "Inter-department transfers (ICU ↔ Ward) tracked in system",
            "Discharge planning → Final prescriptions → Summary generated",
            "Billing (if applicable) → MR finalized → Follow-up appointments booked",
        ]),
        ("3.5 Laboratory Order-to-Result", [
            "Doctor places order in HMS → Order visible in LIS queue",
            "Sample collected → Barcode scanned → Sent to appropriate section",
            "Analyzer processes → Results auto-populated OR manual entry",
            "Pathologist validation → Critical values trigger alert to ordering doctor",
            "Results visible in patient MR → Notification to doctor/nurse",
        ]),
    ]

    for title, steps in journeys:
        add_title(doc, title, 2)
        add_numbered(doc, steps)

    # 4. Integration Specification
    add_title(doc, "4. External System Integration Specification", 1)
    add_table(doc,
        ["External System", "Protocol", "Direction", "Data Exchanged", "Priority"],
        [
            ["PITB/SHC&MED (Punjab)", "REST API / File Export", "Outbound", "OPD stats, pharmacy, home delivery", "Critical"],
            ["Existing HMIS", "Database/API Migration", "Inbound", "MR records, patient history", "Critical"],
            ["Lab Analyzers", "HL7 v2 / ASTM", "Bidirectional", "Orders, results", "Critical"],
            ["PACS/DICOM", "DICOM / HL7", "Bidirectional", "Images, reports", "High"],
            ["HFH & BBGH", "REST API / HL7", "Bidirectional", "Referrals, transfers, summaries", "High"],
            ["Telemedicine Platform", "WebRTC / REST", "Bidirectional", "Consultations, prescriptions", "Medium"],
            ["SMS Gateway", "REST API", "Outbound", "Appointment reminders, alerts", "Medium"],
            ["Biometric Attendance", "API", "Inbound", "Staff attendance for HR", "Low"],
            ["Power BI", "SQL/Data Export", "Outbound", "Analytics datasets", "Medium"],
            ["Home Delivery Courier", "REST API", "Outbound", "Delivery assignments, tracking", "High"],
        ])

    # 5. RBAC
    add_title(doc, "5. Role-Based Access Control (RBAC) Matrix", 1)
    add_table(doc,
        ["Role", "Registration", "OPD", "Emergency", "Lab", "Pharmacy", "ICU", "OT", "Admin", "Reports"],
        [
            ["Registration Clerk", "Full", "Write", "Read", "—", "—", "—", "—", "—", "—"],
            ["Doctor/Consultant", "Read", "Full", "Full", "Order", "Prescribe", "Full", "Full", "—", "Dept"],
            ["Staff Nurse", "Read", "Write", "Write", "—", "Administer", "Full", "Assist", "—", "—"],
            ["Lab Technician", "Read", "—", "—", "Full", "—", "—", "—", "—", "Lab"],
            ["Pharmacist", "Read", "Read", "Read", "—", "Full", "Dispense", "—", "—", "Pharm"],
            ["Radiology Tech", "Read", "—", "Order", "—", "—", "—", "—", "—", "—"],
            ["Dept Head", "Read", "Full", "Full", "View", "View", "View", "View", "Dept", "Dept Full"],
            ["Medical Superintendent", "Full", "Full", "Full", "View", "View", "View", "View", "Full", "Full"],
            ["Executive Director", "View", "View", "View", "View", "View", "View", "View", "View", "Full"],
            ["IT Admin", "Config", "Config", "Config", "Config", "Config", "Config", "Config", "Config", "Config"],
            ["Finance Officer", "—", "—", "—", "—", "View", "—", "—", "Full", "Financial"],
        ])

    # 6. Data Model
    add_title(doc, "6. Core Data Entities", 1)
    add_table(doc,
        ["Entity", "Key Fields", "Linked Modules"],
        [
            ["Patient", "MR Number, CNIC, Name, DOB, Gender, Contact, Photo", "All modules"],
            ["Encounter", "Encounter ID, Type (OPD/IPD/ER), Date, Dept, Doctor", "OPD, Emergency, IPD"],
            ["Order", "Order ID, Type (Lab/Rx/Img/Proc), Status, Priority", "Lab, Pharmacy, Radiology, OT"],
            ["Result", "Result ID, Order ID, Value, Range, Critical Flag", "Lab, Radiology, Echo"],
            ["Prescription", "Rx ID, Drugs, Dosage, Duration, Dispensed Flag", "Pharmacy, OPD, Wards"],
            ["Bed", "Bed ID, Ward, Status, Patient ID", "IPD, ICU, CCU, PICU"],
            ["Procedure", "Proc ID, Type (Surgery/Cath), OT/Cath Lab, Outcome", "OT, Cath Lab"],
            ["Staff", "Employee ID, Role, Department, Credentials", "HR, RBAC, All modules"],
            ["Inventory Item", "Item ID, Category, Stock, Reorder Level", "Pharmacy, Stores, OT"],
            ["Audit Log", "Timestamp, User, Action, Entity, IP", "All modules (ISO compliance)"],
        ])

    # 7. Non-Functional Requirements
    add_title(doc, "7. Non-Functional Requirements", 1)
    add_table(doc,
        ["Requirement", "Specification"],
        [
            ["Concurrent Users", "800+ (peak 200 simultaneous)"],
            ["Daily Transactions", "5,000+ (OPD 3000 + ER 500 + IPD 1000+)"],
            ["Response Time", "< 2 seconds for standard queries; < 500ms for critical paths"],
            ["Availability", "99.9% uptime (max 8.7 hours downtime/year)"],
            ["Backup", "Full daily + incremental every 4 hours; 30-day retention"],
            ["Disaster Recovery", "RTO: 4 hours; RPO: 1 hour"],
            ["Data Retention", "Patient records: lifetime; Audit logs: 7 years"],
            ["Browser Support", "Chrome, Edge, Firefox (latest 2 versions)"],
            ["Accessibility", "Large font mode; keyboard navigation; Urdu language option"],
            ["Scalability", "Horizontal scaling for 742-bed expansion"],
        ])

    # 8. Deployment
    add_title(doc, "8. Deployment Strategy", 1)
    add_title(doc, "8.1 Phased Go-Live Plan", 2)
    add_table(doc,
        ["Wave", "Modules", "Departments", "Duration"],
        [
            ["Wave 1", "Registration, OPD, Medical Records", "OPD, Admin, IT", "2 weeks parallel run"],
            ["Wave 2", "Lab/LIS, Basic Pharmacy", "Lab (all sections), Pharmacy", "2 weeks parallel run"],
            ["Wave 3", "Emergency, IPD, Bed Management", "Emergency, Wards, ICU, CCU", "2 weeks parallel run"],
            ["Wave 4", "OT, Cath Lab, Blood Bank", "Surgery, Cath Lab, Blood Bank", "2 weeks parallel run"],
            ["Wave 5", "Admin (HR, Finance, Purchase)", "All admin departments", "1 week"],
            ["Wave 6", "Reporting, Telemedicine, Quality", "All remaining departments", "1 week"],
        ])

    add_title(doc, "8.2 Infrastructure Requirements", 2)
    add_table(doc,
        ["Component", "Minimum Spec", "Recommended"],
        [
            ["Application Server", "16 CPU, 64GB RAM", "32 CPU, 128GB RAM (redundant)"],
            ["Database Server", "16 CPU, 128GB RAM, SSD RAID", "32 CPU, 256GB RAM, SSD RAID (mirror)"],
            ["Storage", "10 TB (DICOM + documents)", "20 TB with expansion"],
            ["Network", "1 Gbps internal", "10 Gbps backbone"],
            ["UPS", "30 min minimum", "60 min + generator backup"],
            ["SSL Certificate", "Required", "Wildcard cert for subdomains"],
        ])

    # 9. Security
    add_title(doc, "9. Security Specification", 1)
    add_bullets(doc, [
        "JWT-based authentication with refresh tokens; session timeout: 30 min inactive",
        "Role-based access control (RBAC) with department-level granularity",
        "AES-256 encryption for data at rest; TLS 1.3 for data in transit",
        "Comprehensive audit trail (who, what, when, where) for ISO compliance",
        "Password policy: min 12 chars, complexity, 90-day rotation",
        "Two-factor authentication (2FA) for admin and executive roles",
        "IP whitelisting for admin panel access",
        "Regular vulnerability assessments and penetration testing",
        "Data anonymization for research module access",
        "Automatic screen lock on ward workstations after 5 min",
    ])

    # 10. Future Roadmap
    add_title(doc, "10. Future Enhancement Roadmap (Post Phase 1)", 1)
    add_table(doc,
        ["Phase", "Timeline", "Enhancements"],
        [
            ["Phase 2", "Month 17-24", "Mobile app (React Native); AI triage assist; patient portal"],
            ["Phase 3", "Month 24-36", "470-bed expansion modules; IoT device integration (ventilators); predictive analytics"],
            ["Phase 4", "Month 36+", "Regional cardiac network hub; blockchain MR sharing; research database"],
        ])

    path = os.path.join(OUTPUT_DIR, "RIC Document 3 - Modules Workflows Integration.docx")
    doc.save(path)
    return path


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    p1 = generate_doc1()
    p2 = generate_doc2()
    p3 = generate_doc3()
    print("Generated:")
    print(p1)
    print(p2)
    print(p3)

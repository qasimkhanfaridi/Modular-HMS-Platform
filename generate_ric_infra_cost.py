"""Generate RIC HMS Infrastructure Cost document."""
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import os

OUTPUT = r"C:\Users\Faridi\Project\AAQSOLS\RIC Document 4 - Infrastructure Cost Estimate.docx"


def add_title(doc, text, level=0):
    if level == 0:
        p = doc.add_heading(text, level=0)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        doc.add_heading(text, level=level)


def add_para(doc, text, bold=False):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = bold


def add_table(doc, headers, rows):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Table Grid"
    for i, h in enumerate(headers):
        t.rows[0].cells[i].text = h
        for p in t.rows[0].cells[i].paragraphs:
            for r in p.runs:
                r.bold = True
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            t.rows[ri + 1].cells[ci].text = str(val)
    doc.add_paragraph()


doc = Document()
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

add_title(doc, "RIC Hospital Management System")
add_title(doc, "Document 4: Infrastructure Cost Estimate")
add_para(doc, "Rawalpindi Institute of Cardiology (RIC) | Prepared by: AAQSOLS", bold=True)
add_para(doc, "Version 1.0 | August 2026 | Currency: PKR (Pakistani Rupee)")
add_para(doc, "Exchange rate used: 1 USD = PKR 280 (planning estimate)")
doc.add_page_break()

add_title(doc, "1. Executive Summary", 1)
add_para(doc,
    "This document estimates on-premise IT infrastructure costs for the RIC HMS covering ~60 departments, "
    "800+ users, 3,000 daily OPD transactions, and DICOM/imaging storage. Two tiers are provided: "
    "Minimum (single-node, budget) and Recommended (high-availability, production-grade for a tertiary cardiac hospital).")

add_table(doc, ["Tier", "One-Time (CapEx)", "Annual (OpEx)", "Notes"],
    [
        ["Minimum", "PKR 28 – 35 Million", "PKR 4 – 6 Million/year", "Single servers, basic redundancy"],
        ["Recommended (HA)", "PKR 52 – 68 Million", "PKR 8 – 12 Million/year", "Dual servers, mirror DB, 99.9% uptime"],
        ["Expansion-ready (742 beds)", "PKR 75 – 95 Million", "PKR 12 – 16 Million/year", "Future-proof for 470-bed expansion"],
    ])

add_title(doc, "2. Scope & Assumptions", 1)
add_para(doc, "Infrastructure scope includes:", bold=True)
items = [
    "On-premise data center at RIC (primary deployment)",
    "Application, database, storage, network, security, backup",
    "Software licensing (SQL Server, Windows Server, SSL, antivirus)",
    "End-user devices: ward PCs, lab/pharmacy printers, barcode scanners",
    "Excludes: development team salaries, HMS software development cost, building/room construction",
    "Excludes: lab analyzer hardware, PACS modality equipment (integration only)",
    "RIC may already have: generator, building UPS, internet connectivity, some workstations",
    "Government procurement may attract 15-20% variation in vendor quotes",
]
for i in items:
    doc.add_paragraph(i, style="List Bullet")

add_title(doc, "3. Server & Compute Hardware", 1)

add_title(doc, "3.1 Minimum Configuration", 2)
add_table(doc,
    ["Item", "Specification", "Qty", "Unit Cost (PKR)", "Total (PKR)"],
    [
        ["Application Server", "Dell R760 / HPE DL380 — 16 core, 64GB RAM, 2×960GB SSD RAID1", "1", "2,800,000", "2,800,000"],
        ["Database Server", "Dell R760 — 16 core, 128GB RAM, 4×1.92TB NVMe RAID10", "1", "4,200,000", "4,200,000"],
        ["Redis / Cache Server", "VM on app server OR 1U — 8 core, 32GB RAM", "1", "800,000", "800,000"],
        ["File/Backup Server", "2U storage — 8 core, 64GB, 4×4TB HDD RAID5", "1", "1,500,000", "1,500,000"],
        ["Subtotal Compute", "", "", "", "9,300,000"],
    ])

add_title(doc, "3.2 Recommended HA Configuration", 2)
add_table(doc,
    ["Item", "Specification", "Qty", "Unit Cost (PKR)", "Total (PKR)"],
    [
        ["Application Server (Primary)", "32 core, 128GB RAM, 2×1.92TB NVMe, dual PSU", "1", "4,500,000", "4,500,000"],
        ["Application Server (Secondary)", "Same spec — load balancer failover", "1", "4,500,000", "4,500,000"],
        ["Database Server (Primary)", "32 core, 256GB RAM, 8×1.92TB NVMe RAID10, dual PSU", "1", "6,500,000", "6,500,000"],
        ["Database Server (Mirror)", "Same spec — Always On availability group", "1", "6,500,000", "6,500,000"],
        ["Redis Cluster Node", "16 core, 64GB RAM", "2", "2,000,000", "4,000,000"],
        ["Load Balancer / Reverse Proxy", "Hardware or dedicated VM host", "1", "1,200,000", "1,200,000"],
        ["Subtotal Compute (HA)", "", "", "", "27,200,000"],
    ])

add_title(doc, "4. Storage", 1)
add_table(doc,
    ["Item", "Specification", "Min (PKR)", "Recommended (PKR)", "Purpose"],
    [
        ["Primary SAN/NAS", "20TB usable, SSD tier + HDD tier", "2,000,000", "4,500,000", "DICOM, documents, backups"],
        ["Backup Storage", "20TB dedicated (immutable)", "1,200,000", "2,500,000", "Daily + 4hr incremental"],
        ["Tape/LTO (optional)", "LTO-9 library for offsite", "800,000", "1,500,000", "Disaster recovery archive"],
        ["Subtotal Storage", "", "4,000,000", "8,500,000", ""],
    ])
add_para(doc,
    "Storage sizing: ~3,000 OPD/day × 2MB avg record = 6GB/day patient data; DICOM images ~50-200GB/month; "
    "5-year retention estimate: 10-20TB. Recommended tier allows 742-bed expansion.")

add_title(doc, "5. Network & Security", 1)
add_table(doc,
    ["Item", "Specification", "Min (PKR)", "Recommended (PKR)"],
    [
        ["Core Switch", "48-port managed L3, 10Gbps uplink", "350,000", "800,000"],
        ["Access Switches", "24-port PoE × 4 (wards, OPD, lab)", "400,000", "700,000"],
        ["Firewall", "FortiGate / Palo Alto — hospital grade", "600,000", "1,200,000"],
        ["Wi-Fi (Clinical)", "Enterprise APs × 20 (wards, OPD, ER)", "500,000", "900,000"],
        ["Structured Cabling", "Cat6A / fiber patch, rack PDU", "300,000", "600,000"],
        ["Network Access Control", "Role-based VLAN, guest isolation", "—", "500,000"],
        ["Subtotal Network", "", "2,150,000", "4,700,000"],
    ])

add_title(doc, "6. Power & Physical Infrastructure", 1)
add_table(doc,
    ["Item", "Specification", "Min (PKR)", "Recommended (PKR)"],
    [
        ["Server Room UPS", "10-20 KVA, 30 min runtime", "600,000", "1,200,000"],
        ["Server Rack", "42U with PDU, KVM, cable mgmt", "250,000", "400,000"],
        ["Precision Cooling", "Dedicated AC for server room (if needed)", "500,000", "800,000"],
        ["Environmental Monitoring", "Temp/humidity sensors, alerts", "100,000", "200,000"],
        ["Subtotal Physical", "", "1,450,000", "2,600,000"],
    ])
add_para(doc, "Note: RIC main building generator backup assumed available. Server room UPS is still required for clean power.")

add_title(doc, "7. End-User & Peripheral Hardware", 1)
add_table(doc,
    ["Item", "Qty", "Unit (PKR)", "Min Total", "Recommended Total", "Departments"],
    [
        ["Desktop PC (ward/OPD)", "40 / 80", "85,000", "3,400,000", "6,800,000", "OPD, wards, admin"],
        ["Barcode Scanner", "8 / 15", "25,000", "200,000", "375,000", "Lab, pharmacy, blood bank"],
        ["Label Printer", "6 / 10", "45,000", "270,000", "450,000", "Lab, pharmacy, MR"],
        ["MR Card Printer", "2 / 3", "120,000", "240,000", "360,000", "OPD registration"],
        ["Receipt/Thermal Printer", "10 / 20", "15,000", "150,000", "300,000", "OPD, pharmacy"],
        ["Tablet (ICU/ward rounds)", "0 / 15", "80,000", "—", "1,200,000", "ICU, CCU, nursing"],
        ["Subtotal End-User", "", "", "4,260,000", "9,485,000", ""],
    ])

add_title(doc, "8. Software Licensing", 1)

add_title(doc, "8.1 Microsoft SQL Server", 2)
add_para(doc,
    "RIC HMS requires SQL Server for 800+ users. Two licensing paths:")
add_table(doc,
    ["Option", "Model", "Calculation", "Est. Cost (USD)", "Est. Cost (PKR)"],
    [
        ["A — Standard Per-Core (Recommended)", "16 core (32 vCPU) on DB server", "8 × 2-core packs × $3,945", "$31,560", "8,836,800"],
        ["B — Standard Server + CAL", "1 server + 800 CALs", "$989 + (800 × $230)", "$184,989", "51,796,920"],
        ["C — Enterprise Per-Core", "16 core, full HA features", "8 × $15,123", "$120,984", "33,875,520"],
    ])
add_para(doc,
    "Recommendation: Option A (Standard Per-Core, 16 cores) — PKR ~8.8M one-time + 25% Software Assurance "
    "annually (~PKR 2.2M/year). Option B is prohibitive at 800 CALs. Option C only if Always On Enterprise features mandatory.")

add_title(doc, "8.2 Other Software", 2)
add_table(doc,
    ["Software", "Min (PKR)", "Recommended (PKR)", "Notes"],
    [
        ["Windows Server Datacenter", "1,200,000", "2,400,000", "2× servers HA; unlimited VMs"],
        ["Windows Server Standard", "600,000", "—", "Alternative if single host"],
        ["SSL Wildcard Certificate", "80,000/yr", "80,000/yr", "ric.gop.pk domain"],
        ["Endpoint Antivirus (800 seats)", "400,000/yr", "600,000/yr", "Sophos / ESET enterprise"],
        ["Backup Software (Veeam)", "500,000", "900,000", "VM + SQL backup"],
        ["Monitoring (Zabbix free / PRTG)", "—", "300,000", "Optional commercial"],
        ["Office/PDF tools", "200,000", "400,000", "Admin workstations"],
        ["Subtotal Software (Year 1)", "2,980,000", "6,680,000", "Excludes SQL Server Option A"],
    ])

add_title(doc, "9. Implementation & Services (One-Time)", 1)
add_table(doc,
    ["Service", "Min (PKR)", "Recommended (PKR)"],
    [
        ["Data center setup & rack installation", "300,000", "500,000"],
        ["Network deployment & VLAN config", "400,000", "800,000"],
        ["Server OS & SQL installation", "200,000", "400,000"],
        ["Backup & DR configuration", "150,000", "350,000"],
        ["Security hardening & penetration test", "300,000", "600,000"],
        ["Existing HMIS data migration", "500,000", "1,000,000"],
        ["End-user device deployment (60 depts)", "400,000", "800,000"],
        ["Subtotal Implementation", "2,250,000", "4,450,000"],
    ])

add_title(doc, "10. Total Cost Summary", 1)

add_title(doc, "10.1 Minimum Tier — One-Time (CapEx)", 2)
add_table(doc, ["Category", "Amount (PKR)"],
    [
        ["Compute Servers", "9,300,000"],
        ["Storage", "4,000,000"],
        ["Network & Security", "2,150,000"],
        ["Power & Physical", "1,450,000"],
        ["End-User Hardware", "4,260,000"],
        ["SQL Server Standard (16 core)", "8,836,800"],
        ["Other Software (Year 1)", "2,980,000"],
        ["Implementation Services", "2,250,000"],
        ["Contingency (10%)", "3,522,680"],
        ["TOTAL MINIMUM CapEx", "34,749,480"],
    ])
add_para(doc, "Rounded estimate: PKR 28 – 35 Million (if RIC reuses existing PCs, network, UPS)", bold=True)

add_title(doc, "10.2 Recommended HA Tier — One-Time (CapEx)", 2)
add_table(doc, ["Category", "Amount (PKR)"],
    [
        ["Compute Servers (HA cluster)", "27,200,000"],
        ["Storage (primary + backup)", "8,500,000"],
        ["Network & Security", "4,700,000"],
        ["Power & Physical", "2,600,000"],
        ["End-User Hardware", "9,485,000"],
        ["SQL Server Standard (16 core)", "8,836,800"],
        ["Other Software (Year 1)", "6,680,000"],
        ["Implementation Services", "4,450,000"],
        ["Contingency (10%)", "7,245,180"],
        ["TOTAL RECOMMENDED CapEx", "79,696,980"],
    ])
add_para(doc, "Rounded estimate: PKR 52 – 68 Million (vendor negotiation, gov tender pricing)", bold=True)

add_title(doc, "10.3 Annual Operating Cost (OpEx)", 2)
add_table(doc,
    ["Item", "Minimum (PKR/yr)", "Recommended (PKR/yr)"],
    [
        ["Hardware warranty (ProSupport NBD)", "1,200,000", "2,800,000"],
        ["SQL Server Software Assurance (25%)", "2,200,000", "2,200,000"],
        ["Windows Server SA", "300,000", "600,000"],
        ["SSL certificate renewal", "80,000", "80,000"],
        ["Antivirus subscription", "400,000", "600,000"],
        ["Backup media / cloud offsite", "200,000", "500,000"],
        ["UPS battery replacement (amortized)", "100,000", "200,000"],
        ["IT staff (2 FTE infra support)", "2,400,000", "3,600,000"],
        ["Annual security audit", "300,000", "500,000"],
        ["Spare parts / break-fix buffer", "200,000", "500,000"],
        ["TOTAL Annual OpEx", "7,380,000", "11,580,000"],
    ])
add_para(doc, "Rounded: Minimum PKR 4–6M/year | Recommended PKR 8–12M/year", bold=True)
add_para(doc, "(Lower OpEx if RIC existing IT staff absorb support duties)")

add_title(doc, "11. 5-Year Total Cost of Ownership (TCO)", 1)
add_table(doc,
    ["Tier", "CapEx", "OpEx (5 yr)", "5-Year TCO"],
    [
        ["Minimum", "PKR 32M", "PKR 25M", "PKR 57M"],
        ["Recommended (HA)", "PKR 60M", "PKR 50M", "PKR 110M"],
        ["Expansion-ready", "PKR 85M", "PKR 70M", "PKR 155M"],
    ])

add_title(doc, "12. Cost Optimization Options for RIC", 1)
opts = [
    "Reuse existing OPD workstations and network switches where compatible — saves PKR 3-5M",
    "Phase hardware: Year 1 core servers + OPD; Year 2 HA + ward devices — spreads CapEx",
    "PostgreSQL instead of SQL Server — saves PKR 8-10M licensing (requires architecture change)",
    "Open-source monitoring (Zabbix, Grafana) — saves PKR 300-500K",
    "Punjab government centralized procurement — possible 10-15% discount via ST&IT/PSHA",
    "Donated/refurbished enterprise servers from corporate CSR — common in public hospitals",
    "Hybrid cloud backup (Azure/AWS offsite only) — PKR 200-400K/year vs PKR 2.5M tape library",
]
for o in opts:
    doc.add_paragraph(o, style="List Bullet")

add_title(doc, "13. Cloud Hybrid Alternative (Optional Comparison)", 1)
add_para(doc,
    "Full cloud deployment is NOT recommended for RIC due to patient volume, DICOM bandwidth, "
    "and government data sovereignty. However, a hybrid model reduces CapEx:")
add_table(doc,
    ["Component", "On-Premise", "Cloud (Monthly)", "Notes"],
    [
        ["Primary HMS servers", "PKR 27M", "—", "Must stay on-prem"],
        ["DR / Backup", "PKR 2.5M", "PKR 80-150K/mo", "Azure Blob / AWS S3"],
        ["Email / SMS alerts", "—", "PKR 20-40K/mo", "Twilio / local SMS gateway"],
        ["Dev/Test environment", "PKR 2M", "PKR 50K/mo", "Cloud cheaper for non-prod"],
    ])

add_title(doc, "14. Payment & Procurement Recommendation", 1)
for item in [
    "CapEx funded via RIC PC-1 / Punjab SHC&MED budget line for IT infrastructure",
    "Split payment: 40% on delivery, 40% on go-live, 20% after 6-month warranty",
    "OpEx from annual recurring budget (maintenance contract)",
    "Request 3 vendor quotes (Dell/HPE authorized partners in Rawalpindi/Islamabad)",
    "Include 3-year hardware warranty + 5-year SQL Server SA in tender",
]:
    doc.add_paragraph(item, style="List Number")

doc.save(OUTPUT)
print(OUTPUT)

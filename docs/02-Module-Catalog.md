# 02 — Module Catalog

Every module is a **separate microservice** with its own database schema, API, UI bundle, and license key.  
**M00 is mandatory** for all deployments.

---

## Module Dependency Graph

```
M00 Core (REQUIRED)
 ├── M01 Patient Registration ──┬── M02 OPD
 │                              ├── M05 Appointments
 │                              └── M07 Medical Records
 ├── M02 OPD ── M03 Pharmacy
 │         └── M04 Laboratory
 ├── M06 Billing (optional any tier)
 ├── M08 Cardiology ── M09 Echo (heart-specific)
 ├── M10 Emergency (requires M02 or M01)
 ├── M11 IPD Beds (requires M01)
 ├── M12 ICU (requires M11)
 ├── M13 Radiology (standalone diagnostic)
 ├── M14 OT Surgery (requires M11)
 ├── M15 Cath Lab (requires M08, M13) [cardiac only]
 ├── M16 Nursing (requires M11)
 ├── M17 HR Admin
 ├── M18 Finance & Procurement
 ├── M19 Reports & Analytics (requires M00 + any 2 modules)
 ├── M20 Telemedicine (requires M02)
 └── M21 Quality & ISO (enterprise)
```

---

## Module Summary Table

| ID | Module | Standalone? | Heart-Specific? | Min Package | RIC Package |
|----|--------|-------------|-----------------|-------------|-------------|
| M00 | Core Platform | Yes (base) | No | A | F |
| M01 | Patient Registration | Yes | No | A | F |
| M02 | OPD | Yes | No | A | F |
| M03 | Pharmacy | Yes | No | A | F |
| M04 | Laboratory (LIS) | Yes | No | B | F |
| M05 | Appointments | Yes | No | A | F |
| M06 | Billing & Payments | Yes | No | B | F |
| M07 | Medical Records (EMR) | Yes | No | B | F |
| M08 | Cardiology General | Yes | **Yes** | A | F |
| M09 | Echocardiography | Partial | **Yes** | A | F |
| M10 | Emergency / ER | Yes | No | C | F |
| M11 | IPD & Bed Management | Yes | No | C | F |
| M12 | ICU / CCU / PICU | Partial | Partial | E | F |
| M13 | Radiology / RIS | Yes | No | C | F |
| M14 | OT & Surgery | Yes | No | C | F |
| M15 | Cath Lab | Partial | **Yes** | E | F |
| M16 | Nursing Management | Partial | No | C | F |
| M17 | HR & Admin | Yes | No | D | F |
| M18 | Finance & Procurement | Yes | No | D | F |
| M19 | Reports & Analytics | Yes | No | B | F |
| M20 | Telemedicine & Referral | Yes | No | D | F |
| M21 | Quality & ISO | Yes | No | F | F |

---

## Module Details

### M00 — Core Platform (Mandatory)
- **Purpose:** Auth, RBAC, API gateway, audit log, tenant config, module licensing
- **Standalone value:** User management for any healthcare facility
- **Dependencies:** None
- **Key APIs:** `/auth`, `/users`, `/roles`, `/modules`, `/audit`
- **Infra:** Included in all tiers

### M01 — Patient Registration
- **Purpose:** MR number, demographics, CNIC, photo, duplicate detection
- **Standalone value:** Digital patient index for any clinic
- **Dependencies:** M00
- **Works without:** OPD (can register for lab-only or pharmacy-only visits)

### M02 — OPD
- **Purpose:** Consultation, vitals, notes, prescriptions, referrals
- **Standalone value:** Full outpatient clinic management
- **Dependencies:** M00, M01
- **Specialty configs:** Cardiology templates, general medicine, pediatrics, gynae

### M03 — Pharmacy
- **Purpose:** E-prescription, dispensing, inventory, expiry alerts
- **Standalone value:** Pharmacy can run without full OPD (walk-in Rx)
- **Dependencies:** M00 (M02 recommended)

### M04 — Laboratory (LIS)
- **Purpose:** Orders, samples, results, QC, analyzer interface
- **Standalone value:** Lab-only facility (collection center)
- **Dependencies:** M00, M01
- **Cardiac preset:** Cardiac enzyme panel, lipid profile, BNP

### M05 — Appointments
- **Purpose:** Online + walk-in scheduling, SMS reminders, queue tokens
- **Standalone value:** Appointment system for any clinic
- **Dependencies:** M00, M01

### M06 — Billing & Payments
- **Purpose:** Service charges, receipts, insurance, gov schemes
- **Standalone value:** Billing for clinics that charge fees
- **Dependencies:** M00
- **Note:** RIC is mostly free — module used for reporting, not collection

### M07 — Medical Records (EMR)
- **Purpose:** Longitudinal record, document upload, visit history
- **Standalone value:** Digital MR archive
- **Dependencies:** M00, M01

### M08 — Cardiology General (Heart-Specific)
- **Purpose:** Cardiac history templates, risk scores (Framingham, ASCVD), ECG workflow, medication protocols (ACE-I, beta-blocker, statin)
- **Standalone value:** Heart clinic without full HMS
- **Dependencies:** M00, M02 recommended
- **Non-heart hospitals:** Do not install

### M09 — Echocardiography (Heart-Specific)
- **Purpose:** Echo orders, structured reports (LVEF, valves, chambers), image links
- **Standalone value:** Echo lab standalone
- **Dependencies:** M00, M01 (M08 recommended)
- **Non-heart hospitals:** Replace with M13 general radiology

### M10 — Emergency / ER
- **Purpose:** Triage, fast-track, STAT orders, bed tracking
- **Dependencies:** M00, M01, M02 recommended
- **Cardiac preset:** STEMI pathway, Primary PCI timer

### M11 — IPD & Bed Management
- **Purpose:** Admission, discharge, transfer, bed board
- **Dependencies:** M00, M01

### M12 — ICU / CCU / PICU
- **Purpose:** Critical care charting, ventilator, MAR, scoring
- **Dependencies:** M11
- **Cardiac preset:** IABP, post-PCI monitoring, CCU flows

### M13 — Radiology / RIS
- **Purpose:** Imaging orders, scheduling, reports (non-echo)
- **Dependencies:** M00, M01
- **General hospital:** X-ray, CT, ultrasound

### M14 — OT & Surgery
- **Purpose:** OT schedule, checklists, implants, anesthesia record
- **Dependencies:** M11
- **Configs:** Cardiac surgery, general surgery, ortho, gynae

### M15 — Cath Lab (Heart-Specific)
- **Purpose:** Angiography, PCI, procedure log, radiation dose
- **Dependencies:** M08, M11 or M10, M13
- **Non-heart hospitals:** Do not install

### M16 — Nursing Management
- **Purpose:** Care plans, handover, task lists, MAR
- **Dependencies:** M11

### M17 — HR & Admin
- **Purpose:** Staff directory, attendance, leave, roster
- **Dependencies:** M00

### M18 — Finance & Procurement
- **Purpose:** Budget, purchase, stores, inventory
- **Dependencies:** M00, M17 recommended

### M19 — Reports & Analytics
- **Purpose:** Dashboards, KPIs, PITB export, custom reports
- **Dependencies:** M00 + any 2 clinical modules

### M20 — Telemedicine & Referral
- **Purpose:** Video consult, referral letters, partner hospital transfer
- **Dependencies:** M02

### M21 — Quality & ISO
- **Purpose:** Audits, NCR, CAPA, infection surveillance
- **Dependencies:** M00 + enterprise deployment
- **RIC target:** ISO 2026 compliance support

---

## Enabling a New Module (Customer Upgrade)

1. Customer purchases module license
2. License key activated in M00 Core
3. Docker container / service deployed (or auto-enabled in cloud)
4. Database migration runs automatically
5. UI menu item appears for licensed users
6. Training session (included in implementation fee)
7. **No data migration** — existing patient records stay intact

---

See each `modules/Mxx-*/MODULE.md` for full specification per module.

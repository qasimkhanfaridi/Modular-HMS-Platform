# 01 — Business Requirements Document (BRD)

**Project:** AAQSOLS Heart Clinic HMS (LOOM Replica)  
**Version:** 1.0 | **Date:** September 2026  
**Prepared by:** AAQSOLS  
**Source:** LOOM demo analysis (video + audio) — no source code

---

## 1. Executive summary

AAQSOLS will build a **Heart Clinic Management System** replicating the functional behaviour of the existing **LOOM** system used at **The Heart Clinic**, with ownership of full source code and roadmap for improvements. Requirements are derived from a 20-minute screen recording and 21-minute Urdu audio walkthrough.

---

## 2. Business objectives

| # | Objective |
|---|-----------|
| BO-1 | Replace dependency on LOOM vendor for core clinic operations |
| BO-2 | Own intellectual property for sales to other heart clinics |
| BO-3 | Deliver near-future demo to prospects within 8–10 weeks |
| BO-4 | Match existing clinic workflows to avoid retraining staff |
| BO-5 | Improve UI/UX and add modular sales (PulseCore PKG-A/B) |

---

## 3. Stakeholders

| Stakeholder | Role | Interest |
|-------------|------|----------|
| AAQSOLS management | Sponsor | Product ownership, revenue |
| Heart Clinic admin | Primary user | Daily operations |
| Reception staff | User | Registration, check-in, challan |
| Doctors | User | Consultation, prescriptions |
| Lab technician | User | Tests, sample collection |
| Pharmacy staff | User | Medicine dispensing |
| Panel/corporate clients | External | Billing integration |
| Future clinic customers | Customer | Buy AAQSOLS product |

---

## 4. Current state (LOOM system)

| Attribute | Detail |
|-----------|--------|
| Product name | LOOM |
| Clinic brand | The Heart Clinic |
| Deployment | On-premise `http://192.168.1.250:56` |
| Source code | Not available to AAQSOLS |
| Users (demo) | Mr. M Kabir (admin), Dr. M Abdus Salam Azad, Dr. Abdul Malik |
| Copyright | © 2026 LOOM |

---

## 5. Scope

### 5.1 In scope — Phase 1 (Demo MVP)

- Patient registration (CNIC-based, MR number)
- Patient Vault (search, list, actions)
- Patient check-in (walk-in, referral, diagnostics, doctor)
- Challan generation
- Department, doctor, service masters
- Doctor consultation (examination, diagnosis, investigations, medicines, advice)
- Medicine master (category, generic, strength, dosage, route)
- Basic statistics (staff performance)
- Role-based login (Admin, Reception, Doctor minimum)
- Local + inter-branch mode flag

### 5.2 In scope — Phase 2 (Full replica)

- Lab investigations + payment verify + sample collection
- Imaging and diagnostics module
- Inventory module
- Full statistics (pharmacy census, cash flow, reception cash flow, region-wise)
- Panel/corporate billing (split payment)
- EMR search, challan vault, patient monitoring
- Multi-branch with selective data sharing
- PDF report generation

### 5.3 Out of scope (initial)

- RIC-scale enterprise (60 departments) — separate PulseCore PKG-F track
- Mobile native apps (Phase 3)
- PITB integration (Phase 2+)

---

## 6. Business rules (from audio transcript)

| ID | Rule |
|----|------|
| BR-1 | **One CNIC = one patient registration** (duplicate CNIC blocked) |
| BR-2 | Patient types: Private, Panel, Regular, Entitled, Category, Discounted, FOC |
| BR-3 | Panel billing: full panel, 50/50 split, or patient zero + panel claim |
| BR-4 | Challan must close when services are entered before proceeding |
| BR-5 | Check-in types: Walk-In, Referral |
| BR-6 | Check-in destination: Department, Doctor, Investigations/Diagnostics |
| BR-7 | Prescribed by: Doctor, Self, Outdoor |
| BR-8 | Lab flow: order → pending payment → payment verify → sample collection → result entry |
| BR-9 | Medicine can be added on-the-fly during consultation if not in master |
| BR-10 | Multi-branch: lab reports and appointments may share; financial data may not |
| BR-11 | User roles: Executive (full), limited roles with restricted menus |

---

## 7. Assumptions

- Demo video represents production behaviour at The Heart Clinic
- Urdu audio narration accurately describes intended behaviour
- CNIC is primary patient identifier (Pakistan)
- Single clinic primary; multi-branch is future configuration
- Internet optional for on-premise deployment

---

## 8. Constraints

- No access to LOOM database schema or API
- Must clean-room implement from observed behaviour
- Demo MVP timeline: 8–10 weeks
- Budget: internal AAQSOLS development

---

## 9. Success metrics

| Metric | Target |
|--------|--------|
| Feature parity (MVP) | 80% of daily reception + doctor workflow |
| Demo readiness | Live 15-min demo without LOOM server |
| User acceptance | Heart clinic staff confirm "same workflow" |
| First external demo | Within 10 weeks of kickoff |
| Code ownership | 100% AAQSOLS |

---

## 10. Risks

| Risk | Mitigation |
|------|------------|
| Missing hidden features not in demo | Clinic staff review FRS; second video session |
| Transcript errors (Urdu ASR) | Validate with native speaker |
| Scope creep | Strict MVP in Phase 1 |
| LOOM legal/license terms | Legal review of purchase agreement |

---

## 11. Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Product Owner | | | |
| Technical Lead | | | |
| Clinic Representative | | | |

---

*Next: [02-FRS](02-FRS-Functional-Requirements.md)*

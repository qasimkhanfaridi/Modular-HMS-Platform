# 04 — Clinic to RIC Roadmap

Step-by-step plan: **start selling to small heart clinics**, prove modules, then scale to RIC enterprise.

---

## Overview Timeline

```
Year 1          Year 2              Year 3              Year 4
─────────────────────────────────────────────────────────────────
Clinics         Small Hospitals     Cardiac Hospitals   RIC Enterprise
(PKG-A/B)       (PKG-C/D)           (PKG-E)             (PKG-F)
  │                │                    │                   │
  └────────────────┴────────────────────┴───────────────────┘
                    Same codebase · Same modules · Zero migration
```

---

## Phase 1 — Heart Clinic Pilot (Month 1–6)

### Goal
Install **PKG-A** at 3–5 small heart clinics. Validate core modules.

### Target Clinics (Examples)
| Clinic Type | Location | Modules |
|-------------|----------|---------|
| Single cardiologist OPD | Rawalpindi | PKG-A |
| Echo + ECG diagnostic center | Islamabad | PKG-A + M09 |
| 2-doctor cardiac clinic | Lahore | PKG-A |

### Modules to Build & Ship First
1. **M00** Core Platform
2. **M01** Patient Registration
3. **M02** OPD (cardiology template)
4. **M05** Appointments
5. **M08** Cardiology General

### Success Criteria
- [ ] 3 clinics live within 6 months
- [ ] 50+ patients/day per clinic on system
- [ ] < 5 min registration time
- [ ] Clinic staff trained in 2 days
- [ ] Zero critical bugs for 30 days
- [ ] 1 clinic upgrades to PKG-B

### Infra Per Clinic
- 1 server (PKR 150–300K) OR cloud PKR 15K/month
- 2 PCs + printer
- **Total clinic investment: PKR 400K–800K**

---

## Phase 2 — Clinic Plus & Lab (Month 6–12)

### Goal
Upsell **PKG-B** to Phase 1 clinics + sell to 5 new clinics.

### Modules to Add
6. **M03** Pharmacy
7. **M04** Laboratory (lite)
8. **M07** Medical Records
9. **M09** Echocardiography
10. **M19** Reports & Analytics

### Success Criteria
- [ ] 8–10 total clinics on platform
- [ ] 2 on PKG-B
- [ ] Lab module processing 100+ tests/day combined
- [ ] Module upgrade completed in < 1 day per clinic

---

## Phase 3 — Small & General Hospitals (Year 2)

### Goal
Enter **non-heart** market with PKG-C and PKG-D.

### Target Customers
| Type | Package | Heart Modules? |
|------|---------|----------------|
| 30-bed private hospital | PKG-C | No — general config |
| DHQ tehsil hospital | PKG-C | Optional cardiac unit |
| 80-bed multi-specialty | PKG-D | Only if cardiology dept exists |
| Eye hospital | PKG-C (custom) | No M08/M09/M15 |
| Maternity home | PKG-C (custom) | Gynae template only |

### Modules to Add
11. **M10** Emergency
12. **M11** IPD & Beds
13. **M13** Radiology
14. **M16** Nursing
15. **M06** Billing
16. **M14** OT Surgery
17. **M17** HR
18. **M18** Finance & Procurement
19. **M20** Telemedicine

### Success Criteria
- [ ] 3 hospitals live (1 general, 1 cardiac-lite, 1 non-cardiac)
- [ ] Same M02 OPD works for cardiology AND general medicine
- [ ] 500+ total daily transactions across all customers

---

## Phase 4 — Cardiac Hospitals (Year 2–3)

### Goal
Deploy **PKG-E** at mid-size cardiac hospitals (RIC peers).

### Target
- Wazirabad Institute of Cardiology (WIC)
- Faisalabad Institute of Cardiology (FIC)
- Multan Institute of Cardiology (MIC) — expansion wing
- Private cardiac hospitals (100+ beds)

### Modules to Add
20. **M12** ICU / CCU / PICU
21. **M15** Cath Lab

### Success Criteria
- [ ] 1 cardiac hospital (100+ beds) fully live
- [ ] Cath Lab module: 10+ procedures/day
- [ ] ICU module: 20+ beds managed
- [ ] All Phase 1–3 modules reused without code rewrite

---

## Phase 5 — RIC Enterprise (Year 3–4)

### Goal
Full **PKG-F** at Rawalpindi Institute of Cardiology — **60+ departments**.

### Why RIC Comes Last
| Reason | Detail |
|--------|--------|
| Risk reduction | Modules battle-tested in 15+ smaller facilities |
| Proof for tender | RIC HMIS tender 2026 requires proven system |
| Staff confidence | RIC IT team sees working deployments elsewhere |
| Incremental budget | Phased PC-1 funding easier than one big project |
| Training model | Train-the-trainer from Phase 1 clinic champions |

### RIC Wave Deployment

#### Wave 1 (Month 1–2) — OPD Go-Live
- **Modules:** M00, M01, M02, M05, M07
- **Departments:** OPD (1800–3000 patients/day)
- **Parallel run:** 2 weeks with existing HMIS
- **Clinic proof:** Same modules running at 10+ clinics

#### Wave 2 (Month 3–4) — Diagnostics
- **Modules:** M03, M04, M19
- **Departments:** Pharmacy, Lab (7 sections), Home Delivery
- **Clinic proof:** Pharmacy + Lab live at PKG-B clinics

#### Wave 3 (Month 5–7) — Critical Care
- **Modules:** M10, M11, M12, M16
- **Departments:** Emergency (500/day), ICU, CCU, PICU, Nursing
- **Hospital proof:** PKG-E cardiac hospital reference

#### Wave 4 (Month 8–10) — Cardiac Specialty
- **Modules:** M08, M09, M13, M15
- **Departments:** Echo, Cath Lab, Radiology, Nuclear, ETT, Electrophysiology
- **Reference:** RIC Document 2 department map

#### Wave 5 (Month 11–13) — Surgical & Admin
- **Modules:** M14, M17, M18
- **Departments:** OT (4 theatres), Cardiac Surgery, HR, Finance, Purchase, Stores

#### Wave 6 (Month 14–16) — Enterprise Finish
- **Modules:** M20, M21
- **Departments:** Telemedicine, HFH/BBGH referral, Quality/ISO, all remaining admin units

---

## Module Build Priority (Development Order)

| Priority | Module | Reason |
|----------|--------|--------|
| P0 | M00, M01, M02, M05 | Clinic MVP — sell PKG-A |
| P1 | M08, M03, M04, M07, M09 | Clinic Plus — sell PKG-B |
| P2 | M19, M06, M10, M11 | Small hospital — sell PKG-C |
| P3 | M13, M16, M14, M17, M18 | General hospital — sell PKG-D |
| P4 | M12, M15, M20 | Cardiac hospital — sell PKG-E |
| P5 | M21 + RIC integrations | Enterprise — sell PKG-F |

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Clinic won't pay | PKG-A affordable; SaaS monthly option |
| RIC tender goes elsewhere | Enter as subcontractor; prove modules first |
| Module doesn't scale | Load test at Phase 3 hospital before RIC |
| Non-cardiac market differs | Specialty templates in M02 (config, not code) |
| Internet downtime at clinic | Offline mode in M00/M01/M02 |

---

## Revenue Projection (Conservative)

| Phase | Customers | Avg Revenue/Customer | Annual Revenue |
|-------|-----------|---------------------|----------------|
| Phase 1 | 5 clinics (PKG-A) | PKR 600K/year | PKR 3M |
| Phase 2 | 10 clinics (mix A/B) | PKR 900K/year | PKR 9M |
| Phase 3 | 3 hospitals (PKG-C/D) | PKR 3M/year | PKR 9M |
| Phase 4 | 1 cardiac hospital (PKG-E) | PKR 8M/year | PKR 8M |
| Phase 5 | RIC (PKG-F) | PKR 25M/year | PKR 25M |
| **Total Year 3** | | | **~PKR 54M/year recurring** |

*Excludes one-time implementation fees (typically 1.5× annual license)*

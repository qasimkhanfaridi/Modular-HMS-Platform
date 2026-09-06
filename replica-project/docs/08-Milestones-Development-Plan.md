# 08 — Development Milestones

**Project:** AAQSOLS PulseCore Heart Clinic HMS (LOOM replica MVP)  
**Version:** 1.0  
**Kickoff:** Week 0 (upon approval)  
**Demo target:** Week 10  
**Company:** AAQSOLS

---

## Overview

```
M0  Requirements sign-off     ✅ DONE
M1  Repo + DB foundation      ← YOU ARE HERE (next)
M2  Auth + app shell
M3  Patient registration + Vault
M4  Check-in + Challan
M5  Doctor consultation (EMR)
M6  Medicine master + Rx
M7  Staff Performance dashboard
M8  UI polish + demo data
M9  UAT + bug fixes
M10 Demo-ready release
```

**Total MVP duration:** 10 weeks (M1–M10)  
**Team assumption:** 1 backend + 1 frontend developer in parallel

---

## Milestone summary

| Milestone | Name | Week | Duration | Exit criteria |
|-----------|------|------|----------|---------------|
| **M0** | Requirements & docs | Pre-kickoff | — | BRD/FRS approved ✅ |
| **M1** | Repository & database | 1–2 | 2 weeks | Repo runs locally; DB migrated; seed script |
| **M2** | Auth & application shell | 2–3 | 1.5 weeks | Login + roles + sidebar layout |
| **M3** | Patient module | 3–4 | 2 weeks | Register patient; Vault list/search |
| **M4** | Check-in & challan | 4–5 | 2 weeks | Full check-in flow; printable challan |
| **M5** | Doctor consultation | 5–7 | 2 weeks | Doctor queue; save EMR visit |
| **M6** | Medicine master | 6–7 | 1 week | Medicine CRUD; Rx in consultation |
| **M7** | Reports dashboard | 7–8 | 1 week | Staff Performance with date filter |
| **M8** | Polish & demo prep | 8–9 | 1 week | AAQSOLS theme; demo seed data |
| **M9** | UAT & stabilization | 9–10 | 1 week | P0 bugs fixed; demo script tested |
| **M10** | Demo release | 10 | 3 days | Portable demo; stakeholder sign-off |

---

## M0 — Requirements sign-off ✅ COMPLETE

**Status:** Done (September 2026)

| Deliverable | Location |
|-------------|----------|
| BRD | `docs/01-BRD-Business-Requirements.md` |
| FRS (~90 requirements) | `docs/02-FRS-Functional-Requirements.md` |
| Video/audio mapping | `docs/03-Video-Audio-Feature-Mapping.md` |
| UI spec + flows | `docs/04`, `docs/05` |
| Proposal + roadmap | `docs/06`, `docs/07` |

**Gate to M1:** Stakeholder confirms P0 scope from FRS is acceptable.

---

## M1 — Repository & database foundation

**Weeks:** 1–2  
**Owner:** Backend lead + DevOps  
**Depends on:** M0 sign-off

### Objectives

- Create monorepo with backend, frontend, and database projects
- Define core schema aligned to MVP modules
- Local dev environment runs with one command (or documented steps)

### Deliverables

| # | Deliverable | Details |
|---|-------------|---------|
| 1 | Git repository | `AAQSOLS-HeartClinic-HMS` |
| 2 | Solution structure | `.NET 8 Web API` + `React (Vite/TS)` + `database/` |
| 3 | SQL Server schema | Tables below (v1) |
| 4 | EF Core migrations | Initial migration applied |
| 5 | Seed script | Roles, 3 demo users, 2 doctors, 10 services, 5 medicines |
| 6 | README | Setup, run, connection string |
| 7 | `.gitignore` + env template | No secrets in repo |

### Database tables (M1 scope)

| Table | Purpose |
|-------|---------|
| `Roles` | Admin, Reception, Doctor |
| `Users` | Login accounts linked to role |
| `Doctors` | Name, specialty, department, active flag |
| `Patients` | MR number, name, guardian, CNIC, gender, type, mobile, address, DOB |
| `ServiceGroups` | Grouping for check-in services |
| `Services` | Name, charges, delivery days, group FK |
| `CheckIns` | Patient, doctor, type, status, timestamps |
| `CheckInServices` | Line items: service, charges, delivery date |
| `Challans` | Check-in FK, subtotal, challan number, created by |
| `Consultations` | Check-in FK, doctor, status (Hold/Consult/Refer) |
| `ConsultationSections` | JSON or typed columns for findings, diagnosis, advice |
| `ConsultationDiagnostics` | Ordered tests (ECG, ETT, etc.) |
| `ConsultationMedicines` | Rx lines linked to medicine master |
| `MedicineCategories` | e.g. Cardiology |
| `Medicines` | Name, generic, dosage, route, strength, category FK |
| `AuditLogs` | Optional — user actions for demo |

### Technical decisions (M1)

| Decision | Choice |
|----------|--------|
| Backend | .NET 8 Web API |
| ORM | Entity Framework Core 8 |
| Frontend | React 18 + TypeScript + Vite |
| UI library | Tailwind + shadcn/ui (or existing AAQSOLS stack) |
| Database | SQL Server (LocalDB for dev) |
| API style | REST + JSON |
| Auth (M2 prep) | JWT — stub endpoint in M1 optional |

### Acceptance criteria

- [ ] `git clone` → `dotnet run` → API responds on `/health` or `/swagger`
- [ ] `npm run dev` → React app loads (placeholder page OK)
- [ ] Database created via migration; seed data visible in SSMS
- [ ] MR number sequence logic documented (format `5601-YY-NNNNNN`)
- [ ] CNIC unique constraint on `Patients` table
- [ ] README documents setup on Windows

### FRS traceability

Foundation for: AUTH-*, PAT-*, CHK-*, CON-*, MED-*, DOC-*, RPT-*

---

## M2 — Authentication & application shell

**Weeks:** 2–3  
**Owner:** Full stack  
**Depends on:** M1

### Deliverables

| # | Deliverable | FRS |
|---|-------------|-----|
| 1 | Login page (AAQSOLS branding) | AUTH-01 |
| 2 | JWT issue + refresh | AUTH-01 |
| 3 | Role-based route guards | AUTH-02 |
| 4 | Header: clinic name + user display | AUTH-03 |
| 5 | Sidebar navigation (role-filtered) | AUTH-02, AUTH-04 |
| 6 | Empty dashboard placeholder | — |
| 7 | 403 / logout handling | AUTH-01 |

### Menu structure (MVP)

```
Patient Management
  ├── Patient Vault          (Reception, Admin)
  ├── Add Patient            (Reception, Admin)
  └── Checked-In Status      (Reception, Admin) — placeholder OK

Doctor Management
  └── Consultation Queue     (Doctor, Admin)

Medicine
  └── Medicine List          (Admin; Doctor read-only later)

Statistics
  └── Staff Performance      (Admin)

Settings / Users             (Admin — optional M2)
```

### Acceptance criteria

- [ ] Admin, Reception, Doctor login with seeded credentials
- [ ] Each role sees different sidebar items
- [ ] Invalid credentials show error; no crash
- [ ] Session persists on page refresh (token in storage)

---

## M3 — Patient registration & Vault

**Weeks:** 3–4  
**Owner:** Full stack  
**Depends on:** M2

### Deliverables

| # | Deliverable | FRS |
|---|-------------|-----|
| 1 | Add Patient form | PAT-01, PAT-02 |
| 2 | CNIC duplicate validation | PAT-03, BR-1 |
| 3 | Auto MR number generation | PAT-05 |
| 4 | Patient type (Private/Panel) | PAT-04 |
| 5 | Patient Vault data table | PAT-06 |
| 6 | Search / filter on vault | PAT-06 |
| 7 | Action column (icons placeholder) | PAT-07 |
| 8 | Reset & Refresh | PAT-09 |

### Acceptance criteria

- [ ] New patient saves and appears in Vault with MR number
- [ ] Duplicate CNIC blocked with clear message
- [ ] Vault paginated (10/25/50 entries)
- [ ] Search by name, MR, CNIC works
- [ ] Patient type shown as `(Private)` in name column

---

## M4 — Check-in & challan

**Weeks:** 4–5  
**Owner:** Full stack  
**Depends on:** M3

### Deliverables

| # | Deliverable | FRS |
|---|-------------|-----|
| 1 | Check-in modal from Vault | CHK-01 |
| 2 | Walk-In / Referral | CHK-02 |
| 3 | Check-in to: Dept / Doctor / Diagnostics | CHK-03 |
| 4 | Prescribed by: Doctor / Self / Outdoor | CHK-05 |
| 5 | Doctor dropdown | CHK-06, DOC-01 |
| 6 | Service group + service picker | CHK-07, CHK-08 |
| 7 | Service line table + subtotal | CHK-09 |
| 8 | Submit creates check-in + challan | CHK-11, CHK-12 |
| 9 | Challan view / print | CHK-11 |
| 10 | SMS alert UI (no SMS send in MVP) | CHK-10 |

### Acceptance criteria

- [ ] Cannot submit check-in without at least one service (BR-4)
- [ ] Subtotal matches sum of service charges
- [ ] Challan printable (browser print CSS)
- [ ] Patient appears in Checked-In list after submit
- [ ] Holter Monitor (or equivalent) selectable from seeded services

---

## M5 — Doctor consultation (EMR)

**Weeks:** 5–7  
**Owner:** Full stack  
**Depends on:** M4

### Deliverables

| # | Deliverable | FRS |
|---|-------------|-----|
| 1 | Doctor queue — checked-in patients | CON-01 |
| 2 | Consultation layout (sidebar sections) | CON-02 |
| 3 | Exam Findings, Primary Diagnosis | CON-02, CON-12 |
| 4 | Diagnostics orders (ECG, ETT) | CON-03 |
| 5 | Instructions, Follow-up, Advice | CON-05, CON-06, CON-07 |
| 6 | Refer / Hold / Consult actions | CON-09 |
| 7 | Visit summary panel (right) | CON-13 |
| 8 | Delete line items | CON-14 |
| 9 | Advice history table | CON-07 |

### Acceptance criteria

- [ ] Doctor sees only their queue (or all checked-in — configurable)
- [ ] Consult saves all sections to DB
- [ ] Completed consult removes patient from active queue
- [ ] Advice history shows on return visit (same patient)
- [ ] Hold keeps patient in queue with status flag

---

## M6 — Medicine master & prescription

**Weeks:** 6–7 (parallel with M5 tail)  
**Owner:** Backend + frontend  
**Depends on:** M1, M5 (Rx picker)

### Deliverables

| # | Deliverable | FRS |
|---|-------------|-----|
| 1 | Medicine list page | MED-01, MED-02 |
| 2 | Add / edit medicine (Admin) | MED-04 |
| 3 | Category filter (Cardiology) | MED-01 |
| 4 | Rx picker in consultation | CON-04, MED-06 |
| 5 | Seed: Lipolite, Adrance-L, Valam-H | MED-06 |

### Acceptance criteria

- [ ] Admin can add medicine with category, generic, strength, route
- [ ] Doctor selects medicine from dropdown in consultation
- [ ] Prescribed medicines appear in visit summary
- [ ] Medicine list searchable

---

## M7 — Staff Performance dashboard

**Weeks:** 7–8  
**Owner:** Full stack  
**Depends on:** M3, M4 (data exists)

### Deliverables

| # | Deliverable | FRS |
|---|-------------|-----|
| 1 | Staff Performance page | RPT-01 |
| 2 | Date range filter | RPT-02 |
| 3 | Columns: User, Registered, OPD, Services, Doctor, Total | RPT-01 |
| 4 | Totals row | RPT-01 |
| 5 | Default landing for Admin (optional) | — |

### Acceptance criteria

- [ ] Report shows non-empty data with seeded check-ins
- [ ] Date range filters registrations and check-ins correctly
- [ ] Empty state message when no data
- [ ] Matches LOOM-style column layout (from video frame)

---

## M8 — UI polish & demo data

**Weeks:** 8–9  
**Owner:** Frontend + BA  
**Depends on:** M3–M7 feature-complete

### Deliverables

| # | Deliverable |
|---|-------------|
| 1 | AAQSOLS / PulseCore theme (colors, logo, footer) |
| 2 | Loading skeletons and error toasts |
| 3 | Demo seed script: 5 patients, 10 check-ins, 3 consultations |
| 4 | Responsive sidebar (tablet minimum) |
| 5 | "Coming soon" badges on non-MVP menu items |
| 6 | Print styles for challan |

### Acceptance criteria

- [ ] 15-minute demo flow runs without manual DB edits
- [ ] No "LOOM" branding anywhere
- [ ] UI looks modern vs LOOM video frames
- [ ] All P0 FRS items pass checklist review

---

## M9 — UAT & stabilization

**Weeks:** 9–10  
**Owner:** QA + dev team  
**Depends on:** M8

### Test scenarios

| # | Scenario | Role |
|---|----------|------|
| 1 | Login as each role | All |
| 2 | Register patient + duplicate CNIC fail | Reception |
| 3 | Check-in Holter + print challan | Reception |
| 4 | Doctor consult + Rx + advice | Doctor |
| 5 | Staff Performance date range | Admin |
| 6 | Medicine list browse | Admin |
| 7 | Full 15-min demo script end-to-end | Presenter |

### Acceptance criteria

- [ ] All P0 FRS requirements pass UAT
- [ ] Zero P0 bugs open
- [ ] P1 bugs documented for post-MVP
- [ ] Demo script rehearsed once internally

---

## M10 — Demo-ready release

**Week:** 10  
**Owner:** PM + dev  
**Depends on:** M9

### Deliverables

| # | Deliverable |
|---|-------------|
| 1 | Tagged release `v0.1.0-demo` |
| 2 | Demo deploy package (local installer or Docker) |
| 3 | Demo credentials sheet |
| 4 | One-page sales PDF |
| 5 | Backup screen recording of demo |
| 6 | Handoff doc: known limits vs LOOM |

### Acceptance criteria

- [ ] Demo runs on laptop without `192.168.1.250`
- [ ] Stakeholder sign-off for external demos
- [ ] Post-MVP backlog prioritized (Lab, Panel, Multi-branch)

---

## Post-MVP milestones (Phase 2)

| Milestone | Module | Est. weeks | Priority |
|-----------|--------|------------|----------|
| M11 | Lab payment → verify → sample | 3–4 | P2 |
| M12 | Panel / corporate billing | 2–3 | P2 |
| M13 | Lab Cash Flow report | 1–2 | P2 |
| M14 | Pharmacy Census report | 1 | P2 |
| M15 | Imaging / Holter tracking | 2–3 | P3 |
| M16 | Inventory & dispensing | 2–3 | P3 |
| M17 | Multi-branch (Inter Branch) | 3–4 | P3 |
| M18 | PulseCore PKG-A productization | 2 | P1 |

---

## Milestone tracker (copy & update weekly)

| Milestone | Target week | Status | Notes |
|-----------|-------------|--------|-------|
| M0 Requirements | Pre-kickoff | ✅ Done | Docs in `replica-project/docs/` |
| M1 Repo + DB | Week 1–2 | ⬜ Not started | **Next step** |
| M2 Auth + shell | Week 2–3 | ⬜ | |
| M3 Patient module | Week 3–4 | ⬜ | |
| M4 Check-in | Week 4–5 | ⬜ | |
| M5 Consultation | Week 5–7 | ⬜ | |
| M6 Medicine | Week 6–7 | ⬜ | |
| M7 Dashboard | Week 7–8 | ⬜ | |
| M8 Polish | Week 8–9 | ⬜ | |
| M9 UAT | Week 9–10 | ⬜ | |
| M10 Demo release | Week 10 | ⬜ | |

**Legend:** ⬜ Not started | 🔄 In progress | ✅ Done | ⚠️ Blocked

---

## M1 kickoff checklist (start here)

When you approve, we execute **M1** in this order:

1. [ ] Create Git repo `AAQSOLS-HeartClinic-HMS`
2. [ ] Initialize .NET 8 Web API project (`src/Api`)
3. [ ] Initialize React + TypeScript app (`src/Web`)
4. [ ] Add EF Core + SQL Server connection
5. [ ] Create entity models for all M1 tables
6. [ ] Run initial migration
7. [ ] Add seed data script
8. [ ] Add `/health` endpoint + Swagger
9. [ ] Write README with setup steps
10. [ ] First commit: `chore: M1 foundation — repo, schema, seed`

---

## Dependencies & risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| FRS scope creep | Delays M10 | Lock P0 only until demo |
| No LOOM source | Missing edge cases | Clinic validation in M9 |
| Single developer | 10 weeks → 16 weeks | Parallel BE/FE or reduce scope |
| SQL Server licensing | Dev friction | LocalDB / Docker SQL free tier |

---

## Related documents

- [02-FRS](02-FRS-Functional-Requirements.md) — requirement IDs referenced above
- [07-Demo-MVP-Roadmap](07-Demo-MVP-Roadmap.md) — demo script
- [06-Proposal](06-Proposal-Replica-Build.md) — budget and timeline

---

*AAQSOLS | Milestone plan v1.0 | September 2026*

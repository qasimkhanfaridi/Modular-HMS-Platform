# Milestone Tracker — PulseCore Heart Clinic HMS

**Project:** AAQSOLS LOOM replica MVP  
**Code repo:** https://github.com/qasimkhanfaridi/AAQSOLS-HeartClinic-HMS  
**Docs repo:** https://github.com/qasimkhanfaridi/Modular-HMS-Platform  
**Updated:** 7 September 2026

---

## Current status

| | |
|---|---|
| **Phase** | **MVP + Phase 2/3 extensions — demo-ready locally** |
| **Completed** | M0–M8 (core MVP + polish + extended features) |
| **In progress** | M9 — UAT & stabilization |
| **Next** | **M10 — Demo release tag** + remaining P2/P3 sidebar items |
| **Blocker** | None |
| **Deferred** | LOOM SQL export / ETL from `192.168.1.250` (schema ready) |

---

## Milestone progress

| ID | Milestone | Week | Status | Notes |
|----|-----------|------|--------|-------|
| M0 | Requirements sign-off | — | ✅ | BRD/FRS + video mapping complete |
| M1 | Repo + DB foundation | 1–2 | ✅ | GitHub pushed; EF migrations; LocalDB seed |
| M2 | Auth + app shell | 2–3 | ✅ | JWT; 3 roles; LOOM-style sidebar |
| M3 | Patient + Vault | 3–4 | ✅ | CNIC unique; MR number; search |
| M4 | Check-in + Challan | 4–5 | ✅ | Modal check-in; challan; service lines |
| M5 | Doctor consultation | 5–7 | ✅ | Queue; EMR sections; Rx; Refer/Hold/Consult |
| M6 | Medicine master + Rx | 6–7 | ✅ | Master list; Rx picker in consult |
| M7 | Staff Performance | 7–8 | ✅ | Date filter; totals row |
| M8 | UI polish + demo data | 8–9 | ✅ | LOOM UI polish; seed activity; multi-branch demo |
| M9 | UAT + bug fixes | 9–10 | 🔄 | Local smoke tests pass; formal UAT pending |
| M10 | Demo release | 10 | ⬜ | Tag `v0.1.0-demo` on code repo |

---

## Phase 2 / 3 extensions (beyond original M10 scope)

| Feature | Status | Code |
|---------|--------|------|
| Panel billing (Engro panel, split challan) | ✅ | Phase 2 |
| Lab payment → verify → sample | ✅ | Phase 2 |
| Lab / Services / Reception Cash Flow | ✅ | Phase 2 |
| Pharmacy Census | ✅ | Phase 2 |
| Multi-branch + Inter-branch vault | ✅ | Phase 3 |
| Region Wise + Average OPD reports | ✅ | Phase 3 |
| Imaging orders (Holter, Echo) | ✅ | Phase 3 |
| Challan Vault | ✅ | M9 |
| LOOM data import ETL | ⏸️ Deferred | Schema + strategy doc only |

---

## M9 tasks (current)

- [x] API health + login smoke test
- [x] End-to-end check-in → lab queue flow
- [x] Reports generate with seed data
- [x] GitHub repo published
- [ ] Internal 15-min demo rehearsal
- [ ] Tag `v0.1.0-demo` on code repo
- [ ] P0 bug list from clinic walkthrough

---

## M10 exit criteria

- [ ] Demo script runs without manual DB edits
- [ ] `v0.1.0-demo` git tag on `AAQSOLS-HeartClinic-HMS`
- [ ] README + milestone tracker aligned
- [ ] Zero open P0 bugs

---

## Weekly log

| Week | Milestone | Notes |
|------|-----------|-------|
| — | M0 | All docs + Word pack complete |
| 1 | M1–M2 | Monorepo scaffolded; auth + shell |
| 1 | M3–M7 | MVP screens wired to API |
| 1 | M8 | LOOM UI polish; full sidebar with Soon badges |
| 1 | Phase 2 | Panel billing, lab workflow, cash flow reports |
| 1 | Phase 3 | Multi-branch, region/OPD reports, imaging |
| 1 | — | Code pushed to GitHub; LOOM import deferred |

---

*Update this file at the end of each week.*

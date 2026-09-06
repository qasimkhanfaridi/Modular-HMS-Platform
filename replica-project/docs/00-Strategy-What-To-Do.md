# 00 — Strategy: What To Do (Recommended Approach)

**AAQSOLS | Heart Clinic HMS Replica | September 2026**

---

## Your situation (clear picture)

```
LOOM (purchased)          →  Clinic uses it daily, NO source code for AAQSOLS
     ↓
Video + Audio demo        →  Full functional evidence of what system does
     ↓
AAQSOLS replica build     →  Own codebase, own brand, improve later
     ↓
Near-future demo          →  Show clients YOUR product (PulseCore / AAQSOLS)
```

You **cannot** wait for LOOM source code. You **can** reverse-engineer requirements from demo and build fresh.

---

## Recommended strategy (3 phases)

### Phase A — Document everything (NOW — 2 weeks) ✅ In progress

| Task | Output |
|------|--------|
| Watch Loom video frame-by-frame | Screen inventory (doc 04) |
| Map audio transcript to screens | Video-audio mapping (doc 03) |
| Write BRD + FRS | docs 01, 02 |
| Define MVP for demo | doc 07 |
| Stakeholder proposal | doc 06 |

**Do NOT start coding until FRS is signed off.**

---

### Phase B — Build demo MVP (8–10 weeks)

Build **minimum replica** that matches demo for sales:

| Priority | Module | Why |
|----------|--------|-----|
| P0 | Auth + 3 roles | Admin, Reception, Doctor |
| P0 | Patient Registration | CNIC, MR number, vault |
| P0 | Check-in + Challan | Core clinic workflow |
| P1 | Doctor consultation | ECG, diagnosis, Rx basic |
| P1 | Service/department master | Holter, ETT, etc. |
| P2 | Medicine master | Cardiology drug list |
| P2 | Basic reports | Staff performance |

**Tech stack (recommended):**
- Backend: .NET 8 Web API (same as PulseCore plan)
- Frontend: React + TypeScript
- DB: SQL Server / PostgreSQL
- Deploy: Single server or Docker (demo laptop)

---

### Phase C — Full product + improvements (3–12 months)

After first demo wins:

| Improvement over LOOM | AAQSOLS advantage |
|----------------------|-------------------|
| Modern UI (mobile-friendly) | LOOM looks dated |
| Modular licensing | Sell PKG-A to other clinics |
| Cloud + on-prem option | LOOM is local only |
| Urdu/English toggle | Better UX |
| API integrations | PITB, lab analyzers |
| Multi-branch cloud | LOOM branch sharing is limited |

---

## What NOT to do

| Don't | Why |
|-------|-----|
| Copy LOOM code illegally | No source — build clean-room replica |
| Build everything at once | 20+ modules — start MVP |
| Skip documentation | Team needs BRD/FRS for consistent build |
| Promise RIC-scale first | Start heart clinic demo |
| Ignore audio transcript | Contains business rules (CNIC, panel billing) |

---

## Clean-room replica (legal approach)

1. **Requirements** derived from **observed behaviour** in demo (video/audio) — legal
2. **New codebase** written by AAQSOLS team — legal
3. **Different UI design** (modernize) — legal
4. **Same workflows** (industry standard for clinics) — legal

Document: *"Requirements trace to demo observation, not source code."*

---

## Team roles for replica project

| Role | Responsibility |
|------|----------------|
| Product owner | Sign off BRD/FRS, prioritize MVP |
| Business analyst | Complete video-audio mapping, UAT scripts |
| UI/UX designer | Wireframes from screen inventory |
| Backend dev (2) | API, database, business logic |
| Frontend dev (2) | React screens matching flows |
| QA | Test against FRS acceptance criteria |
| Demo presenter | Learn MVP, prepare client pitch |

---

## Decision: One product, two names

| Audience | Brand |
|----------|-------|
| Existing clinic (replacement) | AAQSOLS Heart Clinic HMS |
| New sales (modular) | PulseCore HMS PKG-A/B |
| Same codebase | One project, configurable modules |

---

## Immediate next steps (this week)

1. ✅ Read this document pack (all 7 docs)
2. ☐ Product owner reviews BRD + FRS
3. ☐ BA completes any missing screen captures from video
4. ☐ UI designer starts wireframes for P0 screens
5. ☐ Dev lead creates Git repo: `AAQSOLS-HeartClinic-HMS`
6. ☐ Set demo date target (e.g. 8 weeks from kickoff)

---

## Success criteria for near-future demo

Demo is ready when you can live-show:

- [ ] Register patient with CNIC → MR number generated
- [ ] Search patient in Vault
- [ ] Check-in patient → select service (e.g. Holter) → challan
- [ ] Doctor opens consultation → add ECG/diagnosis → save
- [ ] Show staff performance dashboard
- [ ] Login as 3 different roles
- [ ] Runs on laptop without `192.168.1.250`

**Duration:** 15-minute live demo script.

---

*Next: Read [01-BRD](01-BRD-Business-Requirements.md)*

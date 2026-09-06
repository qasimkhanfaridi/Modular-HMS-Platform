# AAQSOLS Heart Clinic HMS — Replica Project

**Product name (working):** PulseCore HMS / AAQSOLS Heart Clinic  
**Based on:** LOOM system demo (The Heart Clinic) — video + audio analysis  
**Status:** M0–M8 complete → **M9 UAT / M10 demo release next**  
**Code:** [AAQSOLS-HeartClinic-HMS](https://github.com/qasimkhanfaridi/AAQSOLS-HeartClinic-HMS)  
**Company:** AAQSOLS

---

## Situation

| Fact | Detail |
|------|--------|
| Existing system | LOOM — licensed/purchased, runs at clinic (`192.168.1.250:56`) |
| Source code | **Not available** to AAQSOLS |
| Demo materials | Loom video (20 min) + Hospital audio (21 min Urdu) |
| Goal | Build **replica** → demo to clients → improve over LOOM |

---

## Document Pack (read in order)

| # | Document | Purpose |
|---|----------|---------|
| 00 | [Strategy — What To Do](docs/00-Strategy-What-To-Do.md) | Recommended approach & phases |
| 01 | [BRD — Business Requirements](docs/01-BRD-Business-Requirements.md) | Business goals, scope, stakeholders |
| 02 | [FRS — Functional Requirements](docs/02-FRS-Functional-Requirements.md) | Every feature with acceptance criteria |
| 03 | [Video + Audio Mapping](docs/03-Video-Audio-Feature-Mapping.md) | Timestamp → screen → requirement |
| 04 | [Screen Inventory & UI Spec](docs/04-Screen-Inventory-UI-Spec.md) | All screens, fields, menus |
| 05 | [User Flows & Processes](docs/05-User-Flows-Processes.md) | End-to-end workflows |
| 06 | [Proposal — Replica Build](docs/06-Proposal-Replica-Build.md) | Client/stakeholder proposal |
| 07 | [Demo MVP Roadmap](docs/07-Demo-MVP-Roadmap.md) | What to build first for near-future demo |
| 08 | [Development Milestones](docs/08-Milestones-Development-Plan.md) | M0–M10 plan, DB tables, acceptance criteria |
| — | [Milestone Tracker](MILESTONE-TRACKER.md) | Weekly status (update as you go) |

---

## Demo source files

| File | Location |
|------|----------|
| Loom screen recording | `C:\Users\Faridi\Downloads\__ LOOM __... 2026-09-05 14-10-05.mp4` |
| Audio walkthrough | `C:\Users\Faridi\Downloads\Hospital.m4a.mp4` |
| Video frames | `..\demo-review-frames\frame_*.jpg` |
| Full transcript | `..\demo-review-frames\hospital-transcript-full.txt` |
| Transcript summary | `..\demo-review-frames\hospital-transcript-summary.md` |

---

## Near-future demo target (MVP)

Build **Phase 1 Demo** in 8–10 weeks:

1. Login + roles (Admin, Reception, Doctor)
2. Add Patient + Patient Vault
3. Check-in + Challan + service selection
4. Doctor consultation (basic)
5. Medicine master (list)
6. Staff performance dashboard (basic)

See **07-Demo-MVP-Roadmap.md** for full plan.

---

## Word documents (stakeholder sharing)

Generate all `.docx` files:

```powershell
python C:\Users\Faridi\Project\AAQSOLS\Modular-HMS-Platform\scripts\generate_replica_documents.py
```

Output folder: `replica-project\word\`

| File | Contents |
|------|----------|
| `AAQSOLS-Replica-Complete-Pack.docx` | All docs combined |
| `AAQSOLS-Replica-01-BRD.docx` | Business requirements |
| `AAQSOLS-Replica-06-Proposal.docx` | Build proposal |

---

*AAQSOLS | Replica from LOOM demo | September 2026*

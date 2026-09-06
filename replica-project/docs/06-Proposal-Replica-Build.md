# 06 — Proposal: LOOM Replica Build for AAQSOLS

**Document type:** Internal proposal / client-ready outline  
**Prepared by:** AAQSOLS  
**Date:** September 2026  
**Version:** 1.0

---

## Executive summary

AAQSOLS proposes building a **clean-room replica** of the existing LOOM Heart Clinic HMS, observed from demo video and audio walkthrough. We do **not** have LOOM source code. The replica will be branded **PulseCore Heart Clinic HMS** (PKG-A/B) and will serve as:

1. A **near-term demo** for prospects (heart clinics, small hospitals)
2. The **foundation** for the modular PulseCore HMS platform (clinic → RIC)
3. An **improved** product with modern UI, better UX, and modular architecture

---

## Problem statement

| Issue | Detail |
|-------|--------|
| No source code | LOOM runs on clinic server (`192.168.1.250`); codebase not available |
| Vendor lock-in | Clinic depends on third-party product with unknown roadmap |
| No scalability path | LOOM is single-clinic; AAQSOLS needs modular PKG-A → PKG-F |
| Demo gap | Sales team needs working demo without LOOM server access |

---

## Proposed solution

### Phase 1 — Documentation & analysis ✅ (Complete)

- BRD, FRS, video/audio mapping, screen inventory, flows
- Urdu audio transcribed and mapped to features
- 14 video frames extracted for UI reference

### Phase 2 — MVP demo build (8–10 weeks)

**Scope (P0 + selected P1):**

| Module | Features |
|--------|----------|
| Auth & roles | Login, Admin / Reception / Doctor |
| Patient Management | Vault, Add Patient, CNIC uniqueness |
| Check-in | Modal workflow, service selection, challan |
| Doctor consultation | EMR sections, Rx, diagnostics orders |
| Medicine master | Category, generic, dosage, route |
| Statistics | Staff Performance dashboard |
| Branding | AAQSOLS / PulseCore UI |

**Out of MVP:** Lab payment flow, panel billing, multi-branch, full reports suite

### Phase 3 — Full replica + improvements (12–16 weeks after MVP)

- Lab Investigations (payment → verify → sample → result)
- Panel / corporate billing
- Imaging module
- Inventory & pharmacy dispensing
- Cash flow & pharmacy census reports
- Multi-branch (Inter Branch toggle)
- API integrations (HL7/FHIR optional)

### Phase 4 — Modular platform alignment

Map replica modules to PulseCore M00–M21 and package tiers PKG-A through PKG-F.

---

## Technical approach

| Layer | Technology |
|-------|------------|
| Backend | .NET 8 Web API |
| Frontend | React 18 + TypeScript |
| Database | SQL Server |
| Auth | JWT + role-based access |
| Deployment | On-prem (clinic server) or Azure |
| Method | Clean-room — no LOOM code copied |

**Legal note:** Replica is built from **observed behaviour** in demo materials only. No reverse engineering of LOOM binaries or database.

---

## Deliverables

| # | Deliverable | Phase |
|---|-------------|-------|
| 1 | BRD + FRS + mapping docs | 1 ✅ |
| 2 | UI wireframes from video frames | 1–2 |
| 3 | MVP web application (demo-ready) | 2 |
| 4 | 15-minute demo script | 2 |
| 5 | Full feature parity + improvements | 3 |
| 6 | PulseCore module integration | 4 |

---

## Timeline

```
Week 1–2    Documentation finalization, DB schema, API skeleton
Week 3–4    Patient + Check-in modules
Week 5–6    Doctor consultation + Medicine master
Week 7–8    Dashboard, polish, demo data
Week 9–10   UAT, demo script, stakeholder review
```

**MVP demo target:** ~10 weeks from kickoff

---

## Team & effort (estimate)

| Role | MVP effort |
|------|------------|
| Backend developer | 6–8 weeks |
| Frontend developer | 6–8 weeks |
| BA / QA (part-time) | 2–3 weeks |
| PM / demo prep | 1 week |

**Total:** ~2 FTE for 8–10 weeks (can be 1 backend + 1 frontend in parallel)

---

## Investment estimate (internal planning)

| Item | Range (PKR) | Notes |
|------|-------------|-------|
| MVP development | 1.5M – 2.5M | 2 devs × 10 weeks |
| Infrastructure (demo) | 50K – 100K | VM / SQL Server license if needed |
| Full replica (Phase 3) | 2M – 3.5M | Additional modules |
| **MVP total** | **~1.6M – 2.6M** | Demo-ready product |

*Figures for internal planning; adjust for client proposals.*

---

## Risks & mitigations

| Risk | Mitigation |
|------|------------|
| Incomplete requirements from video only | Clinic visit / stakeholder interviews |
| LOOM features not visible in demo | Phased delivery; mark as P2/P3 |
| Scope creep | Strict MVP boundary (P0 only for demo) |
| Demo vs production gap | Label MVP as "functional demo"; roadmap for production |
| CNIC / billing rules wrong | Validate with clinic staff before build |

---

## Success criteria (MVP demo)

- [ ] Register patient with CNIC validation
- [ ] Check-in patient with Holter (or similar) service
- [ ] Print/view challan
- [ ] Doctor completes consultation with Rx + advice
- [ ] Admin views Staff Performance for date range
- [ ] Medicine list browsable
- [ ] Runs on laptop without `192.168.1.250`
- [ ] AAQSOLS branding throughout
- [ ] 15-minute scripted demo without errors

---

## Recommendation

**Proceed with Phase 2 MVP** using existing documentation pack. Do **not** wait for LOOM source code — optional retrieval from clinic server can accelerate Phase 3 only.

**Immediate next steps:**

1. Approve MVP scope and timeline
2. Create git repo `AAQSOLS-HeartClinic-HMS`
3. Set up .NET + React solution
4. Seed demo data (doctors, services, medicines)
5. Schedule weekly demo reviews

---

## Appendix

- [01-BRD](01-BRD-Business-Requirements.md)
- [02-FRS](02-FRS-Functional-Requirements.md)
- [03-Video-Audio-Feature-Mapping](03-Video-Audio-Feature-Mapping.md)
- [07-Demo-MVP-Roadmap](07-Demo-MVP-Roadmap.md)

---

*AAQSOLS — PulseCore HMS*

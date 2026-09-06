# 01 — Product Vision

**Company:** AAQSOLS | **Product:** PulseCore HMS

## Mission

Build Pakistan's first **truly modular** Hospital Management System that any facility can adopt — from a **2-room heart clinic** to a **600+ bed cardiac institute** — without rip-and-replace upgrades.

## Problem We Solve

| Customer Pain | Our Solution |
|---------------|--------------|
| Small clinics can't afford full HMS | PKG-A from PKR 15K/month |
| Existing HMS is all-or-nothing | Buy modules individually |
| Heart clinics need ECG/Echo workflows | Cardiology module (M08/M09) optional |
| General hospitals don't need Cath Lab | Skip M15, use M14 for general surgery |
| RIC-scale needs everything | PKG-F adds all modules incrementally |
| Upgrading means new system | Same platform, enable new module license |

## Target Markets

### Primary (Phase 1–2)
- Small **cardiology clinics** (Rawalpindi, Islamabad, Lahore)
- Single-specialty **heart OPD** centers
- Diagnostic centers (Echo + ECG + basic lab)

### Secondary (Phase 3)
- **General hospitals** (50–150 beds) — DHQ, tehsil headquarters
- **Polyclinics** — multi-specialty without cardiac focus
- **Dental, eye, maternity** clinics wanting HMS lite

### Anchor (Phase 4)
- **RIC** — Rawalpindi Institute of Cardiology (PKG-F)
- Other cardiac institutes: WIC, MIC, FIC, PIC Lahore

## Product Name Options (for market)

| Name | Positioning |
|------|-------------|
| **PulseCore HMS** | Heart-first, modular core |
| **ClinicFlow** | Small clinic entry brand |
| **MedStack HMS** | Technical / B2B brand |

## Differentiation vs Competitors

1. **Modular licensing** — pay per module, not per hospital size alone
2. **Heart clinic first** — pre-built cardiac workflows (ECG, Echo, risk scores)
3. **Same codebase** — clinic today = RIC tomorrow (no migration)
4. **Offline-capable** — small clinics with unreliable internet
5. **Urdu + English** — bilingual UI
6. **PITB-ready** — provincial reporting when customer needs it
7. **On-prem + hybrid** — data stays in Pakistan

## Business Model

| Revenue Stream | Description |
|----------------|-------------|
| Module license (monthly/annual) | Per module per facility |
| Implementation fee (one-time) | Setup, training, data migration |
| Infrastructure (optional) | Hardware bundle per tier |
| Support contract (annual) | 15–20% of license |
| Custom integration | Lab analyzer, PACS, PITB |
| Upsell | Module additions over time |

## Success Metrics (Year 1)

- 5 small heart clinics live on PKG-A
- 2 clinic upgrades to PKG-B
- 1 small hospital on PKG-C
- RIC pilot agreement for PKG-F Phase 1 modules
- 80% module reuse rate (same code across all tiers)

## Technology Stack (Unified Across All Tiers)

- **Backend:** .NET 8 microservices (one service per module)
- **Frontend:** React.js (module lazy-loading — clinic UI loads only active modules)
- **Database:** SQL Server (clinic: Express/single instance; enterprise: Always On)
- **API:** REST + optional HL7 FHIR for lab/radiology
- **Deployment:** Docker — single container stack for clinic, K8s optional for enterprise

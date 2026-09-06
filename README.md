# Modular HMS Platform — Clinic to Enterprise

**Product codename:** PulseCore HMS  
**Vendor:** AAQSOLS  
**Strategy:** Sell modular Hospital Management System packages starting from **small heart clinics**, scaling to **general hospitals**, culminating in **enterprise deployment (RIC-scale)**.

---

## Why Modular?

Each module runs **independently** but connects via a shared **Core Platform (M00)**. Customers buy only what they need today and add modules later without replacing the system.

```
┌─────────────────────────────────────────────────────────────┐
│                    M00 — Core Platform                       │
│         Auth · RBAC · API Gateway · Patient Index · Audit   │
└──────────────────────────┬──────────────────────────────────┘
                           │
     ┌─────────────────────┼─────────────────────┐
     ▼                     ▼                     ▼
┌─────────┐         ┌─────────┐         ┌─────────────┐
│ M01-M07 │         │ M08-M15 │         │  M16-M21    │
│  Core   │         │ Clinical│         │  Enterprise │
│ Clinical│         │ Specialty│        │  Admin/QI   │
└─────────┘         └─────────┘         └─────────────┘
```

---

## Deployment Packages (Buy & Install)

| Package | Target Customer | Modules | Start Here |
|---------|----------------|---------|------------|
| **PKG-A** | Small heart clinic (1–3 doctors) | 5 modules | ✅ **First sale** |
| **PKG-B** | Heart clinic plus (3–8 doctors) | 8 modules | Upgrade from A |
| **PKG-C** | Small hospital (20–50 beds) | 12 modules | Non-cardiac OK |
| **PKG-D** | General hospital (50–150 beds) | 16 modules | Any specialty |
| **PKG-E** | Cardiac / specialty hospital | 18 modules | WIC, MIC style |
| **PKG-F** | Enterprise (RIC-scale, 60+ depts) | All 22 modules | Final target |

---

## Folder Structure

```
Modular-HMS-Platform/
├── README.md                    ← You are here
├── docs/                        ← Strategy, pricing, roadmap, sales
├── modules/                     ← Each module = standalone product
│   ├── M00-core-platform/
│   ├── M01-patient-registration/
│   └── ... M21-quality-iso/
├── deployment-packages/         ← Ready-to-sell bundles (A through F)
├── infrastructure/              ← Infra cost per tier
├── customers/                   ← Target segments & RIC anchor plan
├── proposals/                   ← RIC & client proposal docs
└── templates/                   ← Sales & implementation templates
```

---

## Go-to-Market Path

1. **Phase 1** — Install **PKG-A** at 3–5 small heart clinics (Rawalpindi/Islamabad pilot)
2. **Phase 2** — Upsell **PKG-B/C** to growing clinics & small hospitals
3. **Phase 3** — Sell **PKG-D/E** to general & cardiac hospitals (Punjab, KP, AJK)
4. **Phase 4** — Deploy **PKG-F** at RIC using proven modules from Phase 1–3

---

## Quick Links

| Document | Purpose |
|----------|---------|
| [Product Vision](docs/01-Product-Vision.md) | Mission, market, differentiation |
| [Module Catalog](docs/02-Module-Catalog.md) | All 22 modules, dependencies, standalone use |
| [Deployment Tiers](docs/03-Deployment-Tiers.md) | PKG-A through PKG-F details |
| [Clinic → RIC Roadmap](docs/04-Clinic-to-RIC-Roadmap.md) | Step-by-step module rollout |
| [Pricing Packages](docs/05-Pricing-Packages.md) | License + infra + support pricing |
| [Multi-Specialty Config](docs/06-Multi-Specialty-Configuration.md) | Non-heart hospitals & clinics |
| [Sales Guide](docs/07-Sales-Guide.md) | How to pitch & close |

---

## Related RIC Documents

Original RIC proposal documents are in `C:\Users\Faridi\Project\AAQSOLS\`:
- RIC Document 1 — Complete HMS Proposal
- RIC Document 2 — Department Functionality Matrix
- RIC Document 3 — Modules, Workflows & Integration
- RIC Document 4 — Infrastructure Cost Estimate

RIC is the **anchor enterprise client (PKG-F)** — not the first installation.

---

*Version 1.0 | August 2026 | AAQSOLS*

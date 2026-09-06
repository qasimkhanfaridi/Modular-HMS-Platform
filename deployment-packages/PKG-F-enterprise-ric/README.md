# PKG-F — Enterprise (RIC Scale)

**Final destination package.** Deploy incrementally — never big-bang.

## Included Modules
**ALL** M00 through M21

## Target Customer Profile
| Field | Value |
|-------|-------|
| Facility | Tertiary cardiac institute |
| Anchor client | Rawalpindi Institute of Cardiology (RIC) |
| Beds | 272 → 742 (expansion) |
| Departments | 60+ |
| Users | 800+ |
| OPD/day | 3,000+ |
| Emergency/day | 500+ |
| Surgeries/year | 1,500–2,000 |

## Why RIC Is Last
- All modules proven in clinics and hospitals first
- Phased waves reduce risk
- Reference deployments for tender credibility
- Same code — zero migration from PKG-A modules

## Wave Deployment Plan
See `docs/04-Clinic-to-RIC-Roadmap.md` — Phase 5

| Wave | Months | Modules | Key Departments |
|------|--------|---------|-----------------|
| 1 | 1–2 | M00,M01,M02,M05,M07 | OPD, Medical Records |
| 2 | 3–4 | M03,M04,M19 | Pharmacy, Lab, Reports |
| 3 | 5–7 | M10,M11,M12,M16 | ER, ICU, CCU, Nursing |
| 4 | 8–10 | M08,M09,M13,M15 | Echo, Cath Lab, Radiology |
| 5 | 11–13 | M14,M17,M18 | OT, Surgery, Admin |
| 6 | 14–16 | M20,M21 | Telemedicine, ISO |

## Reference Documents
- `C:\Users\Faridi\Project\AAQSOLS\RIC Document 1 - Complete HMS Proposal.docx`
- `C:\Users\Faridi\Project\AAQSOLS\RIC Document 2 - Department Functionality Matrix.docx`
- `C:\Users\Faridi\Project\AAQSOLS\RIC Document 3 - Modules Workflows Integration.docx`
- `C:\Users\Faridi\Project\AAQSOLS\RIC Document 4 - Infrastructure Cost Estimate.docx`

## Infrastructure
See `infrastructure/tier-5-enterprise-infra.md`  
Estimated CapEx: PKR 52–68 Million (HA cluster)

## Pricing
See `docs/05-Pricing-Packages.md` — PKG-F section  
5-Year TCO: ~PKR 110 Million

## RIC-Specific Integrations
- PITB/SHC&MED provincial reporting
- CM Medicine Home Delivery Programme
- HFH & BBGH referral MoU
- Existing HMIS data migration
- ISO 2026 quality compliance (M21)

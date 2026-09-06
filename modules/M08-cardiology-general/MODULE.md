# M08 — Cardiology General (Heart-Specific)

**Flagship module for heart clinics. Optional for general hospitals.**

## Overview
Cardiac-specific clinical workflows: structured cardiac history, ECG data entry, risk score calculators, cardiac medication protocols, and referral pathways to echo/cath lab.

## Standalone Capability
**Yes** — a heart clinic can run M00 + M08 with minimal OPD for cardiac-only workflows. Best combined with M02 OPD.

## Dependencies
| Module | Required? | Reason |
|--------|-----------|--------|
| M00 Core | Yes | Platform |
| M02 OPD | Recommended | Consultation container |
| M01 Registration | Recommended | Patient context |

## Package Inclusion
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| ✅ | ✅ | Optional | Optional | ✅ | ✅ |

## Heart-Specific?
**Yes** — do NOT install for dental, eye, or general-only facilities.

## Key Features
1. **Cardiac History Template** — chest pain, dyspnea, palpitations, syncope, risk factors
2. **ECG Entry** — rate, rhythm, ST changes, blocks; upload ECG image/PDF
3. **Risk Calculators** — Framingham, ASCVD, CHA₂DS₂-VASc, HAS-BLED, GRACE
4. **Medication Protocols** — ACS pathway, heart failure meds, anticoagulation
5. **Referral Rules** — auto-suggest Echo, Cath Lab, ER based on inputs
6. **Follow-up Schedules** — post-MI, post-stent, chronic HF intervals
7. **Cardiac Exam** — JVP, murmurs, edema, peripheral pulses
8. **Device Tracking** — pacemaker/ICD patient flag

## Non-Heart Hospital Alternative
Disable M08. Use M02 OPD with "General Medicine" template instead. No functionality loss for non-cardiac facilities.

## User Roles
| Role | Permissions |
|------|-------------|
| Cardiologist | Full cardiac templates, risk scores, referrals |
| GP (with cardiac interest) | Basic cardiac history, ECG entry |
| Nurse | Vitals, pre-consultation cardiac questionnaire |

## API Endpoints
```
POST /api/v1/cardiology/consultation
GET  /api/v1/cardiology/risk-score/{type}
POST /api/v1/cardiology/ecg
GET  /api/v1/cardiology/protocols/{condition}
POST /api/v1/cardiology/referral
```

## Connected Modules
- **M09 Echo** — echo referral orders
- **M15 Cath Lab** — cath referral (PKG-E/F only)
- **M10 Emergency** — STEMI pathway trigger
- **M04 Lab** — cardiac enzyme orders
- **M03 Pharmacy** — cardiac medication Rx

## License Pricing
Included in PKG-A. À la carte: PKR 7,000/month.

## Sales Note
This module is the **primary differentiator** for selling to heart clinics. Lead every PKG-A demo with cardiac workflow.

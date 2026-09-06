# 06 — Multi-Specialty Configuration (Non-Heart Hospitals)

PulseCore HMS is **heart-clinic first** but fully configurable for **any hospital or clinic type**.

---

## Configuration Principle

> **Modules are universal. Templates are specialty-specific.**

- **M02 OPD** — same module, different consultation templates
- **M08 Cardiology** — only installed for heart facilities
- **M15 Cath Lab** — only for cardiac hospitals
- **M14 OT Surgery** — config for cardiac, general, ortho, gynae

---

## Specialty Presets

### Preset 1: Heart Clinic (Default — PKG-A)
```
Enabled:  M00, M01, M02, M05, M08, M09
Disabled: M15, M14 (general), M10
Templates: Cardiology OPD, ECG, Echo, Risk scores
```

### Preset 2: General OPD Clinic
```
Enabled:  M00, M01, M02, M05
Disabled: M08, M09, M15
Templates: General medicine, vitals, basic Rx
Use case: Family clinic, general physician
```

### Preset 3: Dental Clinic
```
Enabled:  M00, M01, M02, M05, M06
Disabled: M08, M09, M04 (optional), M15
Templates: Dental chart, procedure codes, X-ray referral
```

### Preset 4: Eye / Ophthalmology Clinic
```
Enabled:  M00, M01, M02, M05, M13 (lite)
Disabled: M08, M09, M15
Templates: Visual acuity, IOP, refraction, surgery referral
```

### Preset 5: Maternity / Gynae Clinic
```
Enabled:  M00, M01, M02, M05, M13 (ultrasound)
Disabled: M08, M15
Templates: ANC visits, ultrasound, delivery planning
```

### Preset 6: Diagnostic Lab Center
```
Enabled:  M00, M01, M04, M06, M19
Disabled: M02 (optional), M08
Templates: Walk-in lab, corporate panels, report delivery
Use case: Standalone lab with no doctor
```

### Preset 7: Pharmacy Only
```
Enabled:  M00, M01, M03, M06
Disabled: All clinical except registration
Use case: Retail pharmacy with patient records
```

### Preset 8: Small General Hospital (PKG-C)
```
Enabled:  M00–M07, M10, M11, M13, M16, M19
Disabled: M08, M09, M15 (unless cardiac unit)
Templates: Multi-specialty OPD, general ER, general wards
Departments: ER, OPD, Lab, Pharmacy, Radiology, IPD, Nursing
```

### Preset 9: Full General Hospital (PKG-D)
```
Enabled:  PKG-C + M14, M17, M18, M20
Disabled: M08, M09, M15
Templates: General surgery, ortho, peds, gynae, medicine
Add-on: Enable M08+M09 if hospital has cardiology department
```

### Preset 10: Cardiac Hospital (PKG-E)
```
Enabled:  All cardiac modules
Templates: Full cardiac pathways
Same as RIC minus enterprise admin (M21) and scale
```

---

## Department Template Engine (M02 OPD)

Each OPD installation includes a **template pack**. Customer selects at install:

| Template Pack | Specialties Included |
|---------------|---------------------|
| **Cardiac** | Cardiology, Echo referral, Risk assessment |
| **General** | Medicine, Peds, Gynae, Surgery referral |
| **Dental** | Dental procedures, oral chart |
| **Eye** | Ophthalmology exam |
| **Mixed Clinic** | Pick any 3 specialties |
| **Hospital Multi** | All specialties (config per department) |

Templates control:
- Consultation form fields
- Order sets (lab, imaging)
- Prescription defaults
- Referral pathways
- Report formats

**No custom code per specialty** — all configuration.

---

## What Changes Between Heart Clinic and General Hospital?

| Aspect | Heart Clinic | General Hospital |
|--------|-------------|------------------|
| M08 Cardiology | ✅ On | ❌ Off (unless dept exists) |
| M09 Echo | ✅ On | ❌ Off |
| M15 Cath Lab | ❌ Off | ❌ Off |
| M02 OPD template | Cardiac | General / multi |
| M04 Lab panels | Cardiac enzymes, lipid | Full pathology |
| M14 OT config | — | General, ortho, gynae |
| M10 ER triage | Basic | Full ESI |
| Branding | PulseCore Heart | PulseCore HMS |
| Price | PKG-A/B | PKG-C/D |

---

## Selling to Non-Heart Customers

### Pitch for General Hospital
*"Same system running in 10 heart clinics across Punjab — proven, stable, modular. "
"Start with OPD + Lab + Pharmacy. Add ER and IPD when ready. "
"No Cath Lab module to pay for if you don't need it."*

### Pitch for Small Clinic (Non-Heart)
*"Digital patient records and appointments from PKR 25,000/month. "
"Add lab or billing when you grow. Urdu interface. Works offline."*

### Cross-Sell Path
```
General Clinic (M00,M01,M02,M05)
    → adds M04 Lab
    → adds M03 Pharmacy
    → adds M06 Billing
    → grows to PKG-C Small Hospital
    → optionally adds M08 if cardiologist joins
```

---

## RIC vs Other Hospitals — Module Overlap

| Module | Heart Clinic | General Hospital | RIC |
|--------|-------------|------------------|-----|
| M00 Core | ✅ | ✅ | ✅ |
| M01 Registration | ✅ | ✅ | ✅ |
| M02 OPD | ✅ cardiac | ✅ general | ✅ both |
| M08 Cardiology | ✅ | ❌ | ✅ |
| M15 Cath Lab | ❌ | ❌ | ✅ |
| M21 ISO | ❌ | ❌ | ✅ |

**Code reuse: ~85%** between heart clinic and RIC.  
**Code reuse: ~70%** between general hospital and RIC.

---

## White-Label Option

Partners can rebrand for their market:

| Brand | Target |
|-------|--------|
| PulseCore Heart | Cardiac clinics |
| PulseCore HMS | General hospitals |
| Partner brand | Reseller white-label (PKG-C+) |

Core platform (M00) stays the same — only UI theme and template pack change.

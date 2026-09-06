# 03 — Deployment Packages (PKG-A to PKG-F)

Each package is a **pre-configured bundle** of modules + infrastructure + training.  
Customers can start with a package and add individual modules later.

---

## PKG-A — Heart Clinic Starter 🫀
**Tagline:** *"Digital heart clinic in 2 weeks"*

| Attribute | Detail |
|-----------|--------|
| **Target** | Small heart clinic, 1–3 doctors, 1–2 rooms |
| **Example** | "Dr. Khan Cardiology Clinic", Echo + ECG center |
| **Staff** | 1 doctor, 1 nurse, 1 receptionist |
| **Patients/day** | 20–80 |
| **Modules** | M00, M01, M02, M05, M08 |
| **Optional add-on** | M09 Echo, M03 Pharmacy, M04 Basic Lab |

### What's Included
- Patient registration & MR number
- OPD consultation (cardiology templates)
- Appointment booking & queue
- Cardiology workflows (ECG entry, risk scores, cardiac history)
- 3 user licenses (expandable)
- Basic reports (daily OPD count, patient list)

### What's NOT Included
- Inpatient, ICU, Emergency, Cath Lab, Surgery
- Full laboratory, radiology PACS
- HR, finance, procurement

### Infrastructure
- 1 mini PC server OR cloud-hosted
- 2 workstations + 1 printer
- See `infrastructure/tier-1-clinic-infra.md`

---

## PKG-B — Heart Clinic Plus 🫀+
**Tagline:** *"Full diagnostic heart clinic"*

| Attribute | Detail |
|-----------|--------|
| **Target** | Growing heart clinic, 3–8 doctors |
| **Example** | Multi-doctor cardiac OPD + echo lab + pharmacy |
| **Patients/day** | 80–200 |
| **Modules** | PKG-A + M03, M04, M06, M07, M09, M19 |

### Adds Over PKG-A
- Pharmacy dispensing & inventory
- Basic laboratory (LIS lite — 30 tests)
- Echocardiography structured reports
- Billing (for private fee-charging clinics)
- Full EMR / visit history
- Analytics dashboard

---

## PKG-C — Small Hospital 🏥
**Tagline:** *"Small hospital, complete core"*

| Attribute | Detail |
|-----------|--------|
| **Target** | 20–50 bed hospital (any specialty) |
| **Example** | Tehsil HQ hospital, private small hospital |
| **Patients/day** | 200–500 OPD |
| **Modules** | M00–M07, M10, M11, M13, M16, M19 |

### Specialty Configuration
| Hospital Type | Enable | Disable |
|---------------|--------|---------|
| General | M02 general templates | M08, M09, M15 |
| Cardiac-lite | M08, M09 | M15 |
| Maternity | Gynae OPD template | M08, M15 |

### Adds Over PKG-B
- Emergency department
- Inpatient bed management
- Radiology / RIS basic
- Nursing module

---

## PKG-D — General Hospital 🏥+
**Tagline:** *"Multi-department hospital"*

| Attribute | Detail |
|-----------|--------|
| **Target** | 50–150 bed general hospital |
| **Departments** | 10–25 |
| **Modules** | PKG-C + M14, M17, M18, M20 |

### Adds Over PKG-C
- OT & general surgery
- HR & admin
- Finance, purchase, stores
- Telemedicine & referral

### Non-Heart Focus
- No M08, M09, M15 unless cardiac unit exists
- M14 configured for general surgery, ortho, gynae

---

## PKG-E — Cardiac / Specialty Hospital ❤️
**Tagline:** *"Full cardiac hospital (pre-RIC)"*

| Attribute | Detail |
|-----------|--------|
| **Target** | 100–250 bed cardiac or specialty hospital |
| **Example** | WIC Wazirabad, smaller cardiac institutes |
| **Departments** | 25–40 |
| **Modules** | PKG-D + M08, M09, M12, M15 (full cardiac stack) |

### Adds Over PKG-D
- Full cardiology suite
- Echo lab with PACS link
- ICU / CCU / PICU
- Cath Lab management
- STEMI pathway, Primary PCI workflow

---

## PKG-F — Enterprise (RIC Scale) 🏛️
**Tagline:** *"Institute-grade — 60+ departments"*

| Attribute | Detail |
|-----------|--------|
| **Target** | RIC, large tertiary cardiac institutes |
| **Beds** | 250–750+ |
| **Departments** | 60+ |
| **Users** | 800+ |
| **Patients/day** | 3,000+ OPD, 500+ ER |
| **Modules** | **ALL** M00–M21 |

### RIC-Specific Configuration
- All 61 departments mapped (see RIC Document 2)
- PITB/SHC&MED integration
- Home delivery programme (Pharmacy module extension)
- HFH/BBGH referral MoU module
- ISO quality module (M21)
- HA infrastructure (dual servers, 99.9% SLA)

### Rollout at RIC (Not Big-Bang)
RIC receives PKG-F **incrementally** — same modules already proven in clinics:

| Wave | Modules | RIC Departments |
|------|---------|-----------------|
| Wave 1 | M00, M01, M02, M05, M07 | OPD, Medical Records |
| Wave 2 | M03, M04, M19 | Pharmacy, Lab, Reports |
| Wave 3 | M10, M11, M12, M16 | Emergency, ICU, CCU, PICU, Nursing |
| Wave 4 | M08, M09, M13, M15 | Echo, Cath Lab, Radiology, Nuclear |
| Wave 5 | M14, M17, M18 | OT, Surgery, HR, Finance |
| Wave 6 | M20, M21 | Telemedicine, Quality/ISO |

---

## Package Comparison Matrix

| Feature | A | B | C | D | E | F |
|---------|---|---|---|---|---|---|
| Patient Registration | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| OPD | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Appointments | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cardiology | ✅ | ✅ | opt | opt | ✅ | ✅ |
| Echo | ❌ | ✅ | opt | opt | ✅ | ✅ |
| Pharmacy | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Laboratory | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Billing | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| EMR | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Emergency | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| IPD / Beds | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| ICU/CCU | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Radiology | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| OT / Surgery | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Cath Lab | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| HR / Finance | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Telemedicine | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Quality / ISO | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Max Users | 5 | 15 | 50 | 150 | 300 | 1000+ |
| Departments | 1–2 | 3–5 | 5–15 | 10–25 | 25–40 | 60+ |

---

## Upgrade Path (Any Customer)

```
PKG-A  ──→  PKG-B  ──→  PKG-C  ──→  PKG-D  ──→  PKG-E  ──→  PKG-F
Clinic      Clinic+      Small       General     Cardiac      RIC
            (+modules)   Hospital    Hospital    Hospital     Enterprise
```

**Rule:** Upgrading never requires new software installation — only license activation + optional infra scale-up + training.

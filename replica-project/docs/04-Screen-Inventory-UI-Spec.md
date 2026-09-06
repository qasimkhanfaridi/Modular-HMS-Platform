# 04 — Screen Inventory & UI Specification

**Based on:** LOOM demo video frames  
**Clinic name in demo:** The Heart Clinic  
**AAQSOLS replica branding:** Configurable (default: AAQSOLS Heart Clinic)

---

## Global UI patterns

| Element | LOOM behaviour | AAQSOLS replica |
|---------|----------------|-----------------|
| Layout | Left sidebar + top header + main content | Same |
| Header left | Clinic logo + name | AAQSOLS logo |
| Header right | User name + avatar initial | Same |
| Sidebar | Collapsible menu groups | Same |
| Tables | DataTables style — search, pagination, show N entries | Same |
| Modals | Center overlay for check-in, forms | Same |
| Buttons | Purple/blue primary actions | Modernize colors (AAQSOLS brand) |
| Footer | © LOOM | © AAQSOLS |

---

## Screen 1 — Login

| Field | Type | Notes |
|-------|------|-------|
| Username/Email | text | |
| Password | password | |
| Login button | button | |

**Roles redirect to:** Dashboard or Patient Vault based on role.

---

## Screen 2 — Staff Performance (Dashboard / Statistics)

**URL pattern:** `/Stats/StaffPerformance` or home for admin

| Element | Type |
|---------|------|
| Date range picker | date range (dd-mm-yyyy) |
| Table columns | User Name, Registered, OPD, ER, IPD, Services, Doctor, Visited Total |
| Total row | sum footer |
| Empty state | "No data available in table" |

---

## Screen 3 — Patient Vault

**URL:** `/Patients/Vault`

| Element | Type |
|---------|------|
| Advance Search | button (purple) |
| Reset & Refresh | button (blue) |
| Add Patient | button (dark blue) |
| Local / Inter Branch | radio |
| Show N entries | dropdown |
| Search box | text (table filter) |
| Table | Name, MRNo, CNIC/Passport, Gender, Registered On, Action |
| Action icons | view, edit, user, print |

**Row example:** Mr. Nisar Ahmed (Private) | 5601-26-001212 | 37405-9227187-1 | Male | Sep 04, 2026

---

## Screen 4 — Add Patient

| Field | Required | Validation |
|-------|----------|------------|
| First Name | Yes | |
| Guardian Name | Yes | |
| Gender | Yes | Male/Female |
| CNIC / Passport | Yes | Unique — one per patient |
| Patient Type | Yes | Private, Panel, etc. |
| Mobile | No | |
| Address | No | |
| Date of Birth | No | |

**On save:** Generate MR number, redirect to Vault.

---

## Screen 5 — Check-In Modal

**Triggered from:** Vault → action icon

| Field | Type | Options |
|-------|------|---------|
| Title | label | "Check In {Patient Name} ({Type})" |
| Type | radio | Walk-In, Referral |
| Check In To | radio | Department, Doctor, Inves/Diagnostics |
| Package | dropdown | Select Package |
| Prescribed By | radio | Doctor, Self, Outdoor |
| Doctor | dropdown | Dr. Name \| Specialty |
| Service Group | dropdown | Select Group |
| Services | dropdown | e.g. 24-48 Hr. Holter Monitor |
| Service table | grid | Service Name, Charges, Delivery Date |
| Sub Total | calculated | |
| SMS Alert | radio | Patient, Organization, Both, None |
| Submit / Cancel | buttons | |

---

## Screen 6 — Doctor Consultation

**URL pattern:** Doctor queue → select patient

**Left sidebar sections:**
- Other Complaints
- Exam Findings
- Primary Diagnosis
- Diagnostics
- Investigations
- Medicines
- Instructions
- Follow Ups
- Advice *(active in demo)*
- Secondary Diagnosis

**Right panel:** Summary cards with delete icon per item

**Center (Advice tab example):** Historical table — Advice, Doctor, Time

**Bottom bar:**
- Refer to Category (checkbox)
- Refer | Hold | Consult (buttons)

---

## Screen 7 — Medicine Master

**URL:** `/Medicine`

**Sub-screens:** Category, Generic, Type, Strength, Dosage, Route, Disposable

| Column | Example |
|--------|---------|
| Category | Cardiology |
| Name | Tab Adrance-L (Empagliflozin + Linagliptin) 25mg/5mg |
| Generic | Empagliflozin + Linagliptin |
| Dosage | once daily |
| Route | mouth |
| Strength | 25mg/5mg |
| Stock | 0 |

---

## Screen 8 — Lab Cash Flow Report

**URL:** `/Accounts/Labcashflow`

| Filter | Type |
|--------|------|
| Service | dropdown |
| Department | dropdown |
| Sub Department(s) | dropdown |
| Doctor | dropdown |
| Misc Services | dropdown |
| Order Type | radio: All, OPD/Lab, OPD, LAB, ER/IPD |
| Patient Type | radio: All, Regular, Panel, Entitle, Category, Discounted, FOC |
| Report Type | radio: Detailed, Summary |
| Generate Report | button |
| Pdf | dropdown export |

---

## Screen 9 — Pharmacy Census

**URL:** `/Stats/PharmacyCensus`

| Filter | Type |
|--------|------|
| Date range | date |
| Pharmacy/Store | dropdown |
| Search | button |
| Table | Date, Males, Females, Total |

---

## Screen 10 — Add Medicine Form (from audio)

| Field | Options |
|-------|---------|
| Name | text |
| Generic | dropdown/search |
| Form/Type | Capsule, Injection, IV, Syrup, Inhaler, Insulin, Cream, Drops |
| Strength | text |
| Dosage | dropdown |
| Route | dropdown |
| Category | Cardiology, etc. |

---

## Navigation matrix by role

| Menu item | Admin | Reception | Doctor |
|-----------|-------|-----------|--------|
| Patient Vault | ✅ | ✅ | View |
| Add Patient | ✅ | ✅ | ❌ |
| Check-In | ✅ | ✅ | ❌ |
| Consultation | ✅ | ❌ | ✅ |
| Medicine master | ✅ | ❌ | View |
| Statistics | ✅ | Partial | ❌ |
| Lab Cash Flow | ✅ | ❌ | ❌ |

---

## AAQSOLS UI improvements (over LOOM)

| Area | LOOM | AAQSOLS replica |
|------|------|-----------------|
| Design | dated Bootstrap | Modern React + clean cards |
| Mobile | poor | Responsive sidebar |
| Loading | "Loading..." text | Skeleton loaders |
| Branding | LOOM footer | AAQSOLS |
| Dark mode | no | optional Phase 2 |

---

*Next: [05-User-Flows](05-User-Flows-Processes.md)*

# 02 — Functional Requirements Specification (FRS)

**Project:** AAQSOLS Heart Clinic HMS Replica  
**Version:** 1.0 | **Traceability:** LOOM demo video + audio

---

## Module 1 — Authentication & Users

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| AUTH-01 | System shall require login with email/username + password | P0 | Unauthenticated users redirected to login |
| AUTH-02 | Roles: Executive/Admin, Reception, Doctor (minimum) | P0 | Menu items differ per role |
| AUTH-03 | Display logged-in user name in header | P0 | e.g. "Mr. M Kabir", "Dr. M Abdus Salam Azad" |
| AUTH-04 | Executive role has full menu access | P1 | All sidebar modules visible |
| AUTH-05 | Limited roles restrict sensitive reports | P2 | Cash flow hidden from reception |

---

## Module 2 — Patient Management

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| PAT-01 | Add new patient with required fields | P0 | Form saves and generates MR number |
| PAT-02 | Fields: First name, Guardian name, Gender, CNIC/Passport | P0 | All visible in demo registration |
| PAT-03 | **One CNIC = one patient only** | P0 | Duplicate CNIC shows error (BR-1) |
| PAT-04 | Patient type: Private, Panel, etc. | P1 | Type shown in vault as "(Private)" |
| PAT-05 | MR number format e.g. `5601-26-001212` | P0 | Auto-generated sequential |
| PAT-06 | Patient Vault — searchable list | P0 | Columns: Name, MRNo, CNIC, Gender, Registered On, Action |
| PAT-07 | Vault actions: view, edit, user, print icons | P1 | Action column per row |
| PAT-08 | Advance Search button | P2 | Extended filter modal |
| PAT-09 | Reset & Refresh button | P1 | Clears filters, reloads |
| PAT-10 | Local vs Inter-Branch toggle | P2 | Radio buttons on vault |
| PAT-11 | EMR Search | P2 | Separate search across records |
| PAT-12 | Patient Monitoring | P3 | Sub-module in sidebar |
| PAT-13 | Checked-In Status | P1 | Shows current check-ins |
| PAT-14 | Challan Vault | P2 | Historical challans |
| PAT-15 | Diagnostics/Investigations Reports | P2 | Report list per patient |
| PAT-16 | Update Doctor Checkin Patient Info | P2 | Edit check-in metadata |

---

## Module 3 — Check-In & Challan

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| CHK-01 | Check-in patient from Vault | P0 | Modal opens with patient name |
| CHK-02 | Type: Walk-In / Referral | P0 | Radio selection |
| CHK-03 | Check-in to: Department / Doctor / Investigations-Diagnostics | P0 | Radio selection |
| CHK-04 | Package dropdown (optional) | P2 | Select Package |
| CHK-05 | Prescribed by: Doctor / Self / Outdoor | P0 | Radio selection |
| CHK-06 | Doctor dropdown with specialty e.g. "Dr. Abdul Malik \| Consultant Cardiologist" | P0 | Populated from doctor master |
| CHK-07 | Service Group dropdown | P1 | Groups services |
| CHK-08 | Services dropdown e.g. "24-48 Hr. Holter Monitor" | P0 | Adds to service table |
| CHK-09 | Service table: Service Name, Charges, Delivery Date | P0 | Line items with subtotal |
| CHK-10 | SMS Alert: Patient / Organization / Both / None | P2 | Radio selection |
| CHK-11 | Generate challan/receipt for patient | P0 | Printable challan |
| CHK-12 | Challan closes when services entered | P0 | BR-4 — cannot proceed without services |

---

## Module 4 — Doctor Management

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| DOC-01 | Doctor master: name, specialty, department | P0 | Used in check-in dropdown |
| DOC-02 | Doctor schedule / check-in settings | P2 | Referenced in audio |
| DOC-03 | Suspension module for doctors | P3 | Mentioned in audio |

---

## Module 5 — Doctor Consultation (EMR)

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| CON-01 | Consultation screen per checked-in patient | P0 | Doctor sees patient queue |
| CON-02 | Sections: Other Complaints, Exam Findings, Primary Diagnosis | P0 | Sidebar navigation |
| CON-03 | Diagnostics / Investigations orders | P0 | e.g. ECG, ETT |
| CON-04 | Medicines prescription | P0 | Link to medicine master |
| CON-05 | Instructions (diet/lifestyle) | P1 | e.g. "Do Not Use Salt" |
| CON-06 | Follow Ups | P1 | e.g. "Come after 2 weeks" |
| CON-07 | Advice (free text) | P1 | Historical advice table |
| CON-08 | Secondary Diagnosis | P2 | Additional diagnosis |
| CON-09 | Actions: Refer, Hold, Consult | P0 | Three buttons at bottom |
| CON-10 | Refer to Category checkbox | P2 | Optional referral |
| CON-11 | Add items not in master on-the-fly | P1 | BR-9 |
| CON-12 | Primary diagnosis dropdown + free text | P1 | Structured + custom |
| CON-13 | Right panel summary of current visit | P1 | Shows diagnostics, meds, etc. |
| CON-14 | Delete line items (trash icon) | P1 | Per section |

---

## Module 6 — Medicine Master

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| MED-01 | Medicine list with categories | P1 | Category: Cardiology |
| MED-02 | Fields: Name, Generic, Dosage schedule, Route, Strength | P1 | As demo table |
| MED-03 | Sub-menus: Category, Generic, Type, Strength, Dosage, Route, Disposable | P2 | Sidebar sub-items |
| MED-04 | Add medicine with form types: Capsule, Injection, IV, Syrup, Inhaler, Insulin | P2 | From audio |
| MED-05 | Medicine linked to inventory (optional) | P3 | Separate inventory module |
| MED-06 | Examples: Lipolite, Adrance-L, Valam-H | P1 | Seed data for demo |

---

## Module 7 — Lab Investigations

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| LAB-01 | Lab test master with codes | P2 | Per-test pricing |
| LAB-02 | Order tests from check-in or consultation | P2 | Flow to lab queue |
| LAB-03 | Pending payments queue | P2 | Payment before sample |
| LAB-04 | Payment verify step | P2 | BR-8 |
| LAB-05 | Sample collection stage | P2 | After payment verified |
| LAB-06 | Result entry fields per test | P2 | Manual entry |
| LAB-07 | Lab cash flow report | P2 | Filters: service, dept, doctor, order type, patient type |

---

## Module 8 — Imaging & Others

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| IMG-01 | Imaging service catalog | P3 | Holter, Echo, etc. as services |
| IMG-02 | Order from check-in diagnostics path | P2 | Inves/Diagnostics check-in |

---

## Module 9 — Inventory

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| INV-01 | Inventory tracking separate from medicine admin | P3 | Mentioned in audio |
| INV-02 | Entry types for stock in/out | P3 | Admin vs inventory |

---

## Module 10 — Statistics & Reports

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| RPT-01 | Staff Performance report | P1 | Users × Registered, OPD, ER, IPD, Services, Doctor, Visited Total |
| RPT-02 | Date range filter | P1 | From-to date picker |
| RPT-03 | Pharmacy Census report | P2 | Date, Males, Females, Total |
| RPT-04 | Services Cash Flow | P2 | Multi-filter report |
| RPT-05 | Reception Cash Flow | P2 | Reception collections |
| RPT-06 | Staff Performance Details | P3 | Drill-down |
| RPT-07 | Region Wise Report | P3 | Geographic |
| RPT-08 | Average OPD Stats | P3 | Analytics |
| RPT-09 | Export to PDF | P2 | Pdf dropdown on reports |
| RPT-10 | Report types: Detailed / Summary | P2 | Radio on filter form |
| RPT-11 | Order type filter: All, OPD/Lab, OPD, LAB, ER/IPD | P2 | Lab cash flow |
| RPT-12 | Patient type filter on reports | P2 | All, Regular, Panel, etc. |

---

## Module 11 — Multi-Branch (Phase 2)

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| BRN-01 | Multiple branches under one organization | P3 | Executive creates branches |
| BRN-02 | Share: lab reports, appointments (configurable) | P3 | From audio |
| BRN-03 | Do NOT share: financial data across branches | P3 | Branch isolation |
| BRN-04 | Inter-branch patient vault view | P3 | Toggle on vault |

---

## Module 12 — Panel / Corporate Billing (Phase 2)

| ID | Requirement | Priority | Acceptance criteria |
|----|-------------|----------|---------------------|
| PNL-01 | Panel master with integrated services | P2 | Panel-specific pricing |
| PNL-02 | Auto-apply panel rates on check-in | P2 | Based on patient panel |
| PNL-03 | Split billing: patient portion + panel claim | P2 | BR-3 |
| PNL-04 | Panel billing reports | P2 | Claim tracking |

---

## Non-functional requirements

| ID | Requirement |
|----|-------------|
| NFR-01 | Web browser access (Chrome, Edge) |
| NFR-02 | Response time < 3 seconds for lists |
| NFR-03 | Support 50 concurrent users (full product) |
| NFR-04 | Urdu + English UI labels (Phase 2) |
| NFR-05 | Audit log for patient record changes |
| NFR-06 | Daily database backup |

---

*Traceability: See [03-Video-Audio-Feature-Mapping](03-Video-Audio-Feature-Mapping.md)*

# 07 — Demo MVP Roadmap & 15-Minute Demo Script

**Goal:** Working demo for prospects without LOOM server  
**Target:** 8–10 weeks from kickoff  
**Brand:** AAQSOLS PulseCore Heart Clinic HMS

---

## MVP module breakdown

### Sprint 1 (Weeks 1–2) — Foundation

| Task | Output |
|------|--------|
| Repo setup | `AAQSOLS-HeartClinic-HMS` monorepo |
| DB schema | Patients, Users, Roles, Services, CheckIns, Consultations |
| API auth | JWT login, 3 roles |
| React shell | Sidebar, header, routing |
| Seed data | 2 doctors, 10 services, 5 medicines |

**Exit:** Login works; empty dashboard loads

---

### Sprint 2 (Weeks 3–4) — Patient & check-in

| Task | FRS IDs |
|------|---------|
| Patient Vault list + search | PAT-06, PAT-07 |
| Add Patient form + CNIC unique | PAT-01–05 |
| MR number generation | PAT-04 |
| Check-in modal | CHK-01–12 |
| Challan view/print | CHK-10 |

**Exit:** Reception can register → check-in → print challan

---

### Sprint 3 (Weeks 5–6) — Doctor & medicine

| Task | FRS IDs |
|------|---------|
| Doctor queue (checked-in patients) | CON-01 |
| Consultation UI (sections) | CON-02–14 |
| Save consultation | CON-12 |
| Medicine master CRUD | MED-01–06 |
| Rx picker in consultation | CON-08 |

**Exit:** Doctor completes consult with medicines + advice

---

### Sprint 4 (Weeks 7–8) — Dashboard & polish

| Task | FRS IDs |
|------|---------|
| Staff Performance report | RPT-01 |
| Date range filter | RPT-02 |
| UI polish (AAQSOLS theme) | — |
| Demo data script | — |
| Error handling / loading states | — |

**Exit:** Admin dashboard shows staff metrics

---

### Sprint 5 (Weeks 9–10) — Demo prep

| Task | Output |
|------|--------|
| UAT with clinic scenarios | Bug list |
| Fix P0 bugs | Stable build |
| Demo script rehearsal | 15-min flow |
| Deploy demo VM / local installer | Portable demo |
| One-pager sales sheet | PDF |

**Exit:** Demo-ready for client meetings

---

## Post-MVP backlog (Phase 3)

| Priority | Module | Weeks est. |
|----------|--------|------------|
| P2 | Lab payment → verify → sample | 3–4 |
| P2 | Panel billing | 2–3 |
| P2 | Lab Cash Flow report | 1–2 |
| P2 | Pharmacy Census | 1 |
| P3 | Imaging / Holter tracking | 2–3 |
| P3 | Inventory | 2–3 |
| P3 | Multi-branch | 3–4 |

---

## 15-minute demo script

**Audience:** Heart clinic owner / administrator  
**Presenter:** AAQSOLS sales + dev support  
**Environment:** Laptop, local or cloud URL

---

### Minute 0:00 — Intro (1 min)

> "This is **PulseCore Heart Clinic HMS** by AAQSOLS — a modern hospital management system built for cardiology clinics. We'll walk through a typical patient day: registration, check-in, doctor consultation, and reporting."

**Show:** Login screen (AAQSOLS branding)

---

### Minute 1:00 — Admin dashboard (1.5 min)

**Login as:** Admin  
**Navigate:** Statistics → Staff Performance  
**Set:** Date range (last 7 days)

> "Management sees staff activity at a glance — registrations, OPD, services ordered — the same metrics your team needs for performance review."

**Show:** Table with sample data (non-empty for demo)

---

### Minute 2:30 — Patient registration (2 min)

**Login as:** Reception (or switch user)  
**Navigate:** Patient Management → Add Patient

**Enter:**
- Name: Demo Patient
- Guardian: Demo Guardian
- CNIC: 35202-1234567-1
- Type: Private
- Gender: Male

> "One CNIC, one patient — the system prevents duplicates automatically."

**Show:** Save → MR number appears → patient in Vault

**Optional:** Try duplicate CNIC → show validation error

---

### Minute 4:30 — Check-in (2.5 min)

**From Vault:** Click check-in on Demo Patient

**Configure:**
- Walk-In
- Check In To: Inves/Diagnostics
- Doctor: Dr. Abdul Malik
- Service: 24-48 Hr. Holter Monitor

> "Reception selects services, doctor, and package. Subtotal and delivery date calculate automatically. SMS alert can notify the patient."

**Submit → Show challan**

> "Challan is printable — this is your billing document before services are delivered."

---

### Minute 7:00 — Doctor consultation (3 min)

**Login as:** Doctor  
**Open:** Checked-in Demo Patient

**Enter:**
- Exam Findings: "BP 140/90, regular pulse"
- Primary Diagnosis: "Hypertension — monitoring required"
- Diagnostics: ECG
- Medicine: Tab Adrance-L (from master)
- Advice: "Low salt diet, daily BP log"
- Follow-up: 2 weeks

**Click:** Consult

> "Full EMR in one screen — findings, diagnosis, labs, prescriptions, instructions. Everything is stored for the next visit."

**Show:** Advice history table populated

---

### Minute 10:00 — Medicine master (1.5 min)

**Login as:** Admin  
**Navigate:** Medicine → list

> "Your pharmacy catalog is centralized — category, generic, strength, route. Doctors pick from this list during consultation."

**Show:** Cardiology medicines, search/filter

---

### Minute 11:30 — Differentiators (1.5 min)

> "Compared to legacy systems:
> - Modern, fast UI
> - Modular — start with clinic package, grow to multi-branch
> - Your data, your server — or cloud
> - Built by AAQSOLS for Pakistani healthcare workflows — CNIC, panel billing, challan"

**Show:** Sidebar module list (even if some are "coming soon")

---

### Minute 13:00 — Roadmap & close (2 min)

> "Today's demo covers core clinic operations. On our roadmap for the next release:
> - Full lab workflow with payment verification
> - Panel and corporate billing
> - Pharmacy dispensing and inventory
> - Multi-branch sync
>
> We can deploy a pilot at your clinic in [X weeks]. Questions?"

**Handout:** One-pager + proposal summary

---

## Demo environment checklist

| Item | Status |
|------|--------|
| Demo users (admin, reception, doctor) | Pre-seeded |
| Sample patients (3–5) | Pre-seeded |
| Doctors (2+) | Pre-seeded |
| Services including Holter | Pre-seeded |
| Medicines (10+) | Pre-seeded |
| Staff Performance has data | Pre-seeded check-ins |
| Offline fallback | Local SQL + localhost |
| Backup video | Screen recording if live fails |

---

## Demo user credentials (template)

| Role | Username | Password |
|------|----------|----------|
| Admin | admin@aaqsols.demo | Demo@123 |
| Reception | reception@aaqsols.demo | Demo@123 |
| Doctor | doctor@aaqsols.demo | Demo@123 |

*Change before any external demo.*

---

## What to say if asked about LOOM

> "We studied industry-standard heart clinic workflows and built PulseCore from the ground up for AAQSOLS clients. Our system covers the same operational needs — patient vault, check-in, EMR, lab, pharmacy, reporting — with a modern architecture you can own and extend."

**Do not:** Claim LOOM compatibility or migration unless explicitly built.

---

*Back to [README](../README.md)*

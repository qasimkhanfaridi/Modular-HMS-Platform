# 03 — Video + Audio Feature Mapping

**Sources:**
- **Video:** `__ LOOM __... 2026-09-05 14-10-05.mp4` (~20 min)
- **Audio:** `Hospital.m4a.mp4` (~21 min Urdu)
- **Frames:** `demo-review-frames/frame_*.jpg`

---

## Mapping legend

| Column | Meaning |
|--------|---------|
| Time (Video) | Approximate timestamp in Loom recording |
| Time (Audio) | Timestamp in Urdu transcript `[MM:SS]` |
| Screen | What is visible |
| Audio topic | What narrator explains |
| FRS IDs | Linked requirements |

---

## Master mapping table

| Video time | Audio time | Screen / feature | Narrator explains (English) | FRS IDs |
|------------|------------|------------------|----------------------------|---------|
| 0:00 | 00:03–00:47 | Staff Performance dashboard | Doctor module; patient appointment module; registration fields; CNIC one patient rule | RPT-01, PAT-01–03, DOC-01 |
| 0:00 | 01:49–02:07 | (Setup screens) | Department & service setup; doctor names; reception entry; challan to patient | CHK-01–11, DOC-01 |
| 4:30 | 04:09–04:54 | Lab / Pharmacy modules | Challan closes on service entry; lab & pharmacy entries; counter patient flow | CHK-12, LAB-01 |
| 4:30 | 04:57–05:10 | Cash flow / logs | Daily cash log; what happened today | RPT-04, RPT-05 |
| 5:00 | 05:33–06:30 | Reports / Panel | Multi-filter reports; panel vs private; panel billing split; patient to doctor | PNL-01–04, RPT-09–12 |
| 6:00 | 06:32–07:46 | Doctor queue / consultation | Patient enters doctor area; attendant; prescription; guidelines | CON-01–14 |
| 7:30 | 07:19–07:43 | Medicine module | Add to medicine class; permutations; generic combinations | MED-01–06 |
| 9:00 | 09:32–10:30 | Doctor consultation UI | Exam findings page; primary diagnosis; investigations; medicines; add if not in master | CON-02–14, MED-04 |
| 11:30 | 11:50–12:05 | Lab payment flow | Test order; pending payments; verify payment; sample collection | LAB-02–06 |
| 12:00 | 12:39–12:54 | Lab test list | Per-test pricing; LFT etc.; backup test entry | LAB-01, LAB-06 |
| 13:30 | 13:30–14:58 | Medicine form / Inventory | Basic fields; medicine ledger; dosage forms (capsule, injection, insulin) | MED-04, INV-01 |
| 17:30 | 17:35–17:59 | Statistics menu | Statistics module; cash flow; region-wise; pharmacy census mentioned | RPT-01–08 |
| 18:00 | 17:59–18:45 | User roles / Multi-branch | 2–3 users; executive vs limited; multi-branch; shared lab reports | AUTH-02–05, BRN-01–04 |
| 3:00 | — | **Patient Vault** (video) | MR list, CNIC, actions, Add Patient | PAT-05–10 |
| 3:00 | — | **Check-in modal** (video) | Walk-in, Holter service, Dr. Abdul Malik | CHK-01–10 |
| 10:00 | — | **Medicine list** (video) | Cardiology drugs table | MED-01–02 |
| 15:00 | — | **Lab Cash Flow** (video) | Report filters, Generate Report, PDF | RPT-04, LAB-07 |
| 18:00 | — | **Consultation** (video) | ECG, ETT, Advice, Refer/Hold/Consult | CON-01–14 |
| 21:00 | — | **Pharmacy Census** (video) | Date filter, Males/Females/Total | RPT-03 |

---

## Video frame index

| Frame file | ~Video time | Screen captured |
|------------|-------------|-----------------|
| frame_0001.jpg | 0:00 | Staff Performance dashboard |
| frame_0003.jpg | 3:00 | Check-in modal — Mr. Nisar Ahmed, Holter Monitor |
| frame_0005.jpg | 7:30 | Lab Cash Flow report filters |
| frame_0006.jpg | 9:00 | Patient Vault — Dr. Azad logged in |
| frame_0008.jpg | 12:00 | Doctor consultation — Advice, Refer/Hold/Consult |
| frame_0010.jpg | 15:00 | Medicine master list |
| frame_0014.jpg | 21:00 | Pharmacy Census report |

---

## Audio-only segments (no matching video frame)

| Audio time | Topic | FRS IDs |
|------------|-------|---------|
| 00:25–00:47 | CNIC validation, guardian name, gender | PAT-02, PAT-03 |
| 05:57–06:29 | Panel subscription billing rules | PNL-02–04 |
| 14:22–14:58 | Medicine dosage forms inventory | MED-04, INV-01 |
| 18:12–19:31 | Multi-branch data sharing rules | BRN-01–04 |
| 19:42–19:59 | Small clinic vs multi-lab setup | BRN-04 |

---

## Sidebar menu (complete — from video)

```
Patient Management
  ├── Add Patient
  ├── Patient's Vault
  ├── Patient Monitory
  ├── Checked In Status
  ├── Diagnostics/ Investigations Reports
  ├── EMR Search
  ├── Challan Vault
  └── Update Doctor Checkin Patient Info
Doctor Management
Imaging And Others
Lab Investigations
Medicine
  ├── Medicine
  ├── Category / Generic / Type / Strength / Dosage / Route / Disposable
Inventory
Statistics
  ├── Pharmacy Census Report
  ├── Services Cash Flow
  ├── Reception Cash Flow
  ├── Staff Performance Details
  ├── Region Wise Report
  └── Average OPD Stats
```

---

## Requirements coverage summary

| Source | Requirements identified |
|--------|------------------------|
| Video only | 45 |
| Audio only | 28 |
| Both confirmed | 62 |
| **Total FRS items** | **~90** |
| **MVP (P0)** | **25** |

---

*Next: [04-Screen-Inventory](04-Screen-Inventory-UI-Spec.md)*

# 05 — User Flows & Business Processes

**AAQSOLS Heart Clinic HMS Replica**

---

## Flow 1 — New patient registration (P0)

```
Reception login
    → Patient Management → Add Patient
    → Fill: Name, Guardian, Gender, CNIC, Type
    → System validates CNIC unique
    → Save → MR number generated (e.g. 5601-26-001213)
    → Patient appears in Vault
```

**Business rules:** BR-1 (one CNIC), PAT-01 to PAT-05  
**Audio ref:** 00:30–00:47  
**Video ref:** Patient Vault screen

---

## Flow 2 — Patient check-in with service (P0)

```
Reception → Patient Vault → Find patient → Check-In action
    → Modal: Walk-In | Referral
    → Check In To: Inves/Diagnostics (or Doctor/Department)
    → Select Doctor: Dr. Abdul Malik
    → Select Service: 24-48 Hr. Holter Monitor
    → Service added to table (Charges, Delivery Date)
    → Subtotal calculated
    → SMS alert option
    → Submit → Challan generated & printable
    → Patient status: Checked In
```

**Business rules:** BR-4 (challan closes on services), CHK-01 to CHK-12  
**Audio ref:** 01:49–02:07, 04:09  
**Video ref:** Check-in modal frame

---

## Flow 3 — Doctor consultation (P0)

```
Doctor login
    → Doctor queue / Checked-In patients
    → Select patient
    → Consultation screen opens
    → Enter: Exam Findings, Primary Diagnosis
    → Order Diagnostics: ECG, ETT
    → Add Medicines (from master or new)
    → Add Instructions, Follow-up, Advice
    → Action: Consult (complete) | Hold | Refer
    → Record saved to EMR
```

**Business rules:** CON-01 to CON-14, BR-9  
**Audio ref:** 09:32–10:30  
**Video ref:** Consultation frame (Advice tab)

---

## Flow 4 — Lab test with payment (P2)

```
Service ordered (from check-in or consultation)
    → Lab Investigations → Pending Payments
    → Patient pays at counter
    → Staff: Payment Verify
    → Sample Collection queue
    → Sample collected
    → Result entry per test
    → Result available in Diagnostics Reports
```

**Business rules:** BR-8, LAB-02 to LAB-06  
**Audio ref:** 11:50–12:05

---

## Flow 5 — Panel patient billing (P2)

```
Register patient as Panel type
    → Link to Panel master (corporate)
    → Check-in → services auto-priced at panel rates
    → Billing split:
        Option A: 100% panel
        Option B: 50% patient + 50% panel
        Option C: 0 patient + panel claim
    → Reports track panel claims
```

**Business rules:** BR-2, BR-3, PNL-01 to PNL-04  
**Audio ref:** 05:33–06:29

---

## Flow 6 — Staff performance report (P1)

```
Admin login → Statistics → Staff Performance (or default dashboard)
    → Select date range
    → Table shows per-user metrics
    → Export optional
```

**Video ref:** frame_0001.jpg

---

## Flow 7 — Medicine master setup (P1)

```
Admin → Medicine → Add
    → Category: Cardiology
    → Name, Generic, Form, Strength, Dosage, Route
    → Save → Available in consultation Rx
```

**Audio ref:** 13:30–14:58  
**Video ref:** Medicine list frame

---

## End-to-end daily clinic flow

```
                    ┌─────────────────┐
                    │ Patient arrives │
                    └────────┬────────┘
                             ▼
              ┌──────────────────────────┐
              │ Already registered?        │
              └──┬─────────────────────┬───┘
            No │                       │ Yes
                 ▼                       ▼
         ┌─────────────┐         ┌─────────────┐
         │ Add Patient │         │ Find Vault  │
         └──────┬──────┘         └──────┬──────┘
                └──────────┬─────────────┘
                           ▼
                  ┌────────────────┐
                  │ Check-In       │
                  │ + Select Service│
                  └────────┬───────┘
                           ▼
                  ┌────────────────┐
                  │ Challan/Payment │
                  └────────┬───────┘
                           ▼
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
     ┌──────────┐  ┌──────────┐  ┌──────────┐
     │ Doctor   │  │ Lab      │  │ Imaging  │
     │ Consult  │  │ Tests    │  │ Holter   │
     └────┬─────┘  └────┬─────┘  └────┬─────┘
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                 ┌─────────────┐
                 │ Pharmacy /  │
                 │ Dispense    │
                 └──────┬──────┘
                        ▼
                 ┌─────────────┐
                 │ Follow-up   │
                 │ scheduled   │
                 └─────────────┘
```

---

## Process comparison: LOOM vs AAQSOLS replica

| Process | LOOM | Replica MVP | Full replica |
|---------|------|-------------|--------------|
| Registration | ✅ | ✅ P0 | ✅ |
| Check-in | ✅ | ✅ P0 | ✅ |
| Consultation | ✅ | ✅ P0 | ✅ |
| Lab payment flow | ✅ | ❌ | ✅ P2 |
| Panel billing | ✅ | ❌ | ✅ P2 |
| Multi-branch | ✅ | ❌ | ✅ P3 |
| Reports | ✅ | Partial P1 | ✅ |

---

*Next: [06-Proposal](06-Proposal-Replica-Build.md)*

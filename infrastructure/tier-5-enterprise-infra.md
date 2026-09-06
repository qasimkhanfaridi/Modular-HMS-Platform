# Tier 5 — Enterprise Infrastructure (PKG-F / RIC)

Full specification — see also `C:\Users\Faridi\Project\AAQSOLS\RIC Document 4 - Infrastructure Cost Estimate.docx`

## Recommended HA Cluster

| Component | Specification | Qty | Cost (PKR) |
|-----------|---------------|-----|------------|
| App Server Primary | 32 core, 128GB, NVMe RAID | 1 | 4,500,000 |
| App Server Secondary | Same (failover) | 1 | 4,500,000 |
| DB Server Primary | 32 core, 256GB, NVMe RAID10 | 1 | 6,500,000 |
| DB Server Mirror | Always On AG | 1 | 6,500,000 |
| Redis Cluster | 16 core, 64GB × 2 | 2 | 4,000,000 |
| Storage SAN/NAS | 20TB usable | 1 | 4,500,000 |
| Backup Storage | 20TB immutable | 1 | 2,500,000 |
| Network (core + access + firewall) | 10 Gbps backbone | 1 | 4,700,000 |
| UPS + Rack + Cooling | 20 KVA, 42U | 1 | 2,600,000 |
| End-user devices | 80 PCs, scanners, tablets | 1 | 9,485,000 |

## Software Licensing

| Software | Cost (PKR) |
|----------|------------|
| SQL Server Standard 16-core | 8,836,800 |
| Windows Server Datacenter | 2,400,000 |
| Backup, AV, SSL, monitoring | 1,580,000 |

## Total Summary

| | Amount |
|--|--------|
| **CapEx (Recommended HA)** | **PKR 52 – 68 Million** |
| **Annual OpEx** | **PKR 8 – 12 Million** |
| **5-Year TCO** | **~PKR 110 Million** |

## Scaling from Clinic to Enterprise

| Stage | Infrastructure | Investment |
|-------|---------------|------------|
| Clinic (PKG-A) | 1 PC | PKR 450K |
| Clinic Plus (PKG-B) | Mini server | PKR 735K |
| Small Hospital (PKG-C) | 1 server + storage | PKR 2.5M |
| General Hospital (PKG-D) | 2 servers + SAN | PKR 8M |
| Cardiac Hospital (PKG-E) | HA pair + SAN | PKR 25M |
| Enterprise RIC (PKG-F) | Full HA cluster | PKR 55–68M |

**Key point:** Software modules don't change — only hardware scales.

## RIC-Specific Notes
- Existing generator backup assumed
- Existing internet connectivity (9281111-9 exchange)
- Integration with existing HMIS during parallel run
- PITB reporting requires outbound API connectivity
- DICOM storage grows ~50–200 GB/month — plan 20TB+

# Tier 1 — Small Clinic Infrastructure (PKG-A / PKG-B)

## Option A: Single PC Server (Budget)

| Item | Spec | Qty | Cost (PKR) |
|------|------|-----|------------|
| Server PC | Intel i7, 32GB RAM, 1TB SSD, Win 11 Pro | 1 | 180,000 |
| Workstation | Intel i5, 16GB, 512GB SSD | 2 | 170,000 |
| MR/Receipt Printer | Thermal + A4 laser | 2 | 45,000 |
| UPS | 1 KVA desktop | 2 | 30,000 |
| Network switch | 8-port unmanaged | 1 | 8,000 |
| Cabling & install | — | 1 | 15,000 |
| **Total** | | | **~448,000** |

## Option B: Cloud-Hosted (SaaS — No Local Server)

| Item | Spec | Cost (PKR) |
|------|------|------------|
| Cloud VM (our hosting) | 4 vCPU, 16GB RAM | 15,000/month |
| Workstation PCs | 2× as above | 170,000 one-time |
| Printers | 2× as above | 45,000 one-time |
| Internet | 20 Mbps min | Customer existing |
| **Year 1 Total** | | **~615,000** |

## Option C: Mini Server (Recommended for Clinic Plus)

| Item | Spec | Qty | Cost (PKR) |
|------|------|-----|------------|
| Dell T150 / HPE ML30 | Xeon, 64GB, 2TB RAID1 | 1 | 350,000 |
| Workstations | 3× i5 | 3 | 255,000 |
| Barcode scanner | Lab/pharmacy | 1 | 25,000 |
| Printers | 3× | 3 | 60,000 |
| UPS | 2 KVA | 1 | 45,000 |
| **Total** | | | **~735,000** |

## Software (Included in License)
- SQL Server Express (free, up to 10GB — sufficient for clinic)
- Docker Desktop / Windows containers
- PulseCore HMS modules (licensed separately)

## Network Requirements
- Minimum 10 Mbps internet (for updates, SMS, backup)
- Offline mode works without internet for core OPD
- Local network: 100 Mbps between PCs and server

## Room Requirements
- 1 desk for server/PC (ventilated)
- Power: dedicated circuit recommended
- No special cooling needed for Option A

## Maintenance (Annual)
| Item | Cost (PKR/yr) |
|------|---------------|
| Hardware warranty | 30,000 |
| UPS battery | 10,000 |
| Cloud (if Option B) | 180,000 |
| **Total** | **40,000–180,000** |

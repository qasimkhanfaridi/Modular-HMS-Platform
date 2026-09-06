# M00 — Core Platform

**Mandatory for all deployments. Cannot be disabled.**

## Overview
Central platform providing authentication, authorization, module licensing, API gateway, audit logging, tenant configuration, and shared patient index lookup.

## Standalone Capability
Partial — provides user management and security but no clinical features alone. Every deployment starts here.

## Dependencies
None — this is the root module.

## Package Inclusion
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## Key Features
1. **JWT Authentication** — login, refresh tokens, session management
2. **RBAC** — role-based access per module and department
3. **Module Licensing** — enable/disable modules via license key without reinstall
4. **API Gateway** — routes requests to microservices
5. **Audit Trail** — every action logged (user, timestamp, entity, IP)
6. **Tenant Config** — hospital name, logo, specialty preset, language (Urdu/English)
7. **Offline Sync** — queue operations when internet down, sync on reconnect
8. **Notification Hub** — SMS, email, in-app alerts
9. **User Management** — create/disable users, assign roles
10. **Health Monitor** — service status dashboard for IT

## User Roles
| Role | Permissions |
|------|-------------|
| Super Admin | Full system config, module licensing |
| Admin | User management, reports, settings |
| IT Support | Service monitor, logs, backup triggers |
| All clinical roles | Authenticated via M00, permissions per module |

## Microservice
- **Service name:** `pulsecore-core`
- **Port:** 5000
- **Database schema:** `core`

## API Endpoints
```
POST /api/v1/auth/login
POST /api/v1/auth/refresh
GET  /api/v1/users
POST /api/v1/users
GET  /api/v1/roles
GET  /api/v1/modules          # list licensed modules
POST /api/v1/modules/activate # activate new module license
GET  /api/v1/audit            # audit log query
GET  /api/v1/config           # tenant settings
PUT  /api/v1/config
GET  /api/v1/health           # service health check
```

## Infrastructure
| Tier | Spec |
|------|------|
| Clinic | Runs on same PC as other modules |
| Enterprise | Dedicated auth cluster, Redis session store |

## License
Included in all package prices — no separate charge.

## Technical Notes
- All other modules register with M00 on startup
- Module container only starts if license is active
- Supports multi-facility (future): one core, multiple hospitals

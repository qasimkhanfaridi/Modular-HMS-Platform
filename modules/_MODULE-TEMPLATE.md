# Module Specification Template

Copy this file when creating a new module.

## Module ID: Mxx
## Module Name: 
## Version: 1.0

### Overview
Brief description of what this module does.

### Standalone Capability
Can this module run without other modules (besides M00)? Yes/No.
What value does it provide alone?

### Dependencies
| Module | Required? | Reason |
|--------|-----------|--------|
| M00 Core | Yes | Auth, API, licensing |

### Package Inclusion
| PKG-A | PKG-B | PKG-C | PKG-D | PKG-E | PKG-F |
|-------|-------|-------|-------|-------|-------|
| | | | | | |

### Heart-Specific?
Yes/No — if yes, disable for general hospitals.

### Key Features
1. 
2. 
3. 

### User Roles
| Role | Permissions |
|------|-------------|
| | |

### API Endpoints (Microservice)
```
GET  /api/v1/...
POST /api/v1/...
```

### Database Tables
- `table_name` — description

### UI Screens
1. 
2. 

### Integration Points
| System | Protocol | Direction |
|--------|----------|-----------|
| | | |

### Infrastructure Requirements
| Tier | Additional Resources |
|------|---------------------|
| Clinic | |
| Enterprise | |

### License Pricing
| Monthly | Annual |
|---------|--------|
| PKR | PKR |

### Implementation Effort
| Clinic | Hospital | Enterprise |
|--------|----------|------------|
| days | days | days |

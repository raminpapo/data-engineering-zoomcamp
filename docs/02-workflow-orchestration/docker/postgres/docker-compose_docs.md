# docker-compose.yml

**Path**: `02-workflow-orchestration/docker/postgres/docker-compose.yml`
**Size**: 319 bytes
**Lines**: 15

## Source Code

```yaml
version: "3.8"
services:
  postgres:
    image: postgres
    container_name: postgres-db
    environment:
      POSTGRES_USER: kestra
      POSTGRES_PASSWORD: k3str4
      POSTGRES_DB: postgres-zoomcamp
    ports:
      - "5432:5432"
    volumes:
      - postgres-data:/var/lib/postgresql/data
volumes:
  postgres-data:
```

## Analysis

File type: `.yml`

---
*Generated: 2025-11-15T20:48:44.547639*

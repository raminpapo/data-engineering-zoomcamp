# docker-compose.yaml

**Path**: `01-docker-terraform/2_docker_sql/docker-compose.yaml`
**Size**: 427 bytes
**Lines**: 19

## Source Code

```yaml
services:
  pgdatabase:
    image: postgres:13
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=root
      - POSTGRES_DB=ny_taxi
    volumes:
      - "./ny_taxi_postgres_data:/var/lib/postgresql/data:rw"
    ports:
      - "5432:5432"
  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=root
    ports:
      - "8080:80"
    
```

## Analysis

File type: `.yaml`

---
*Generated: 2025-11-15T20:48:44.082647*

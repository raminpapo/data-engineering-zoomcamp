# docker-compose.yaml

**Path**: `04-analytics-engineering/docker_setup/docker-compose.yaml`
**Size**: 297 bytes
**Lines**: 12

## Source Code

```yaml
version: '3'
services:
  dbt-bq-dtc:
    build:
      context: .
      target: dbt-bigquery
    image: dbt/bigquery
    volumes:
      - .:/usr/app
      - ~/.dbt/:/root/.dbt/
      - ~/.google/credentials/google_credentials.json:/.google/credentials/google_credentials.json
    network_mode: host
```

## Analysis

File type: `.yaml`

---
*Generated: 2025-11-15T20:48:44.352992*

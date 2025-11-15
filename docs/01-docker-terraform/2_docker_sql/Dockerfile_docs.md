# Dockerfile

**Path**: `01-docker-terraform/2_docker_sql/Dockerfile`
**Size**: 179 bytes
**Lines**: 9

## Source Code

```
FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY ingest_data.py ingest_data.py 

ENTRYPOINT [ "python", "ingest_data.py" ]
```

## Analysis

File type: ``

---
*Generated: 2025-11-15T20:48:44.081168*

# entrypoint.sh

**Path**: `cohorts/2022/week_2_data_ingestion/airflow/scripts/entrypoint.sh`
**Size**: 364 bytes
**Lines**: 11

## Source Code

```bash
#!/usr/bin/env bash
export GOOGLE_APPLICATION_CREDENTIALS=${GOOGLE_APPLICATION_CREDENTIALS}
export AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT=${AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT}

airflow db upgrade

airflow users create -r Admin -u admin -p admin -e admin@example.com -f admin -l airflow
# "$_AIRFLOW_WWW_USER_USERNAME" -p "$_AIRFLOW_WWW_USER_PASSWORD"

airflow webserver

```

## Analysis

File type: `.sh`

---
*Generated: 2025-11-15T20:48:44.161638*

# Keywords: data_ingestion_gcs_dag.py

**File**: `cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py`

## Keyword Index

### BashOperator

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: from airflow.operators.bash import BashOperator

### BigQueryCreateExternalTableOperator

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: .providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator

### DAG

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: from airflow import DAG

### PythonOperator

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: from airflow.operators.python import PythonOperator

### airflow

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: from airflow import DAG

### days_ago

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: from airflow.utils.dates import days_ago

### format_to_parquet

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: def format_to_parquet(src_file):

### google

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: from google.cloud import storage

### logging

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: import logging

### pyarrow

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: import pyarrow.csv as pv

### storage

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: from google.cloud import storage

### upload_to_gcs

- **Defined in**: [cohorts/2022/week_2_data_ingestion/airflow/dags/data_ingestion_gcs_dag.py](./data_ingestion_gcs_dag.py_docs.md)
- **Context**: def upload_to_gcs(bucket, object_name, local_file):


---
*Total keywords: 12*

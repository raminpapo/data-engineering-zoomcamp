# web_to_gcs.sh

**Path**: `cohorts/2022/week_2_data_ingestion/airflow/extras/web_to_gcs.sh`
**Size**: 312 bytes
**Lines**: 9

## Source Code

```bash
dataset_url=${dataset_url}
dataset_file=${dataset_file}
path_to_local_file=${path_to_local_file}
path_to_creds=${path_to_creds}

curl -sS "$dataset_url" > $path_to_local_file/$dataset_file
gcloud auth activate-service-account --key-file=$path_to_creds
gsutil -m cp $path_to_local_file/$dataset_file gs://$BUCKET

```

## Analysis

File type: `.sh`

---
*Generated: 2025-11-15T20:48:44.151796*

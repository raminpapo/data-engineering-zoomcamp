# 05_gcp_setup.yaml

**Path**: `02-workflow-orchestration/flows/05_gcp_setup.yaml`
**Size**: 602 bytes
**Lines**: 23

## Source Code

```yaml
id: 05_gcp_setup
namespace: zoomcamp

tasks:
  - id: create_gcs_bucket
    type: io.kestra.plugin.gcp.gcs.CreateBucket
    ifExists: SKIP
    storageClass: REGIONAL
    name: "{{kv('GCP_BUCKET_NAME')}}" # make sure it's globally unique!

  - id: create_bq_dataset
    type: io.kestra.plugin.gcp.bigquery.CreateDataset
    name: "{{kv('GCP_DATASET')}}"
    ifExists: SKIP

pluginDefaults:
  - type: io.kestra.plugin.gcp
    values:
      serviceAccount: "{{kv('GCP_CREDS')}}"
      projectId: "{{kv('GCP_PROJECT_ID')}}"
      location: "{{kv('GCP_LOCATION')}}"
      bucket: "{{kv('GCP_BUCKET_NAME')}}"

```

## Analysis

File type: `.yaml`

---
*Generated: 2025-11-15T20:48:44.537758*

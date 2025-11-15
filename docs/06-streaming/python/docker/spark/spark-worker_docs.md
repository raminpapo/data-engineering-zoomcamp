# spark-worker.Dockerfile

**Path**: `06-streaming/python/docker/spark/spark-worker.Dockerfile`
**Size**: 224 bytes
**Lines**: 9

## Source Code

```
FROM spark-base

# -- Runtime

ARG spark_worker_web_ui=8081

EXPOSE ${spark_worker_web_ui}
CMD bin/spark-class org.apache.spark.deploy.worker.Worker spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT} >> logs/spark-worker.out

```

## Analysis

File type: `.Dockerfile`

---
*Generated: 2025-11-15T20:48:44.447748*

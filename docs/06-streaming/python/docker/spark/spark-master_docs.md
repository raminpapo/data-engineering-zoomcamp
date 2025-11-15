# spark-master.Dockerfile

**Path**: `06-streaming/python/docker/spark/spark-master.Dockerfile`
**Size**: 194 bytes
**Lines**: 8

## Source Code

```
FROM spark-base

# -- Runtime

ARG spark_master_web_ui=8080

EXPOSE ${spark_master_web_ui} ${SPARK_MASTER_PORT}
CMD bin/spark-class org.apache.spark.deploy.master.Master >> logs/spark-master.out
```

## Analysis

File type: `.Dockerfile`

---
*Generated: 2025-11-15T20:48:44.452201*

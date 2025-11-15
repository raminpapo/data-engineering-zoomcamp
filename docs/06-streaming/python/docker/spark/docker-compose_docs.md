# docker-compose.yml

**Path**: `06-streaming/python/docker/spark/docker-compose.yml`
**Size**: 1,108 bytes
**Lines**: 53

## Source Code

```yaml
version: "3.6"
volumes:
  shared-workspace:
    name: "hadoop-distributed-file-system"
    driver: local
networks:
  default:
    name: kafka-spark-network
    external: true

services:
  jupyterlab:
    image: jupyterlab
    container_name: jupyterlab
    ports:
      - 8888:8888
    volumes:
      - shared-workspace:/opt/workspace
  spark-master:
    image: spark-master
    container_name: spark-master
    environment:
      SPARK_LOCAL_IP: 'spark-master'
    ports:
      - 8080:8080
      - 7077:7077
    volumes:
      - shared-workspace:/opt/workspace
  spark-worker-1:
    image: spark-worker
    container_name: spark-worker-1
    environment:
      - SPARK_WORKER_CORES=1
      - SPARK_WORKER_MEMORY=4g
    ports:
      - 8083:8081
    volumes:
      - shared-workspace:/opt/workspace
    depends_on:
      - spark-master
  spark-worker-2:
    image: spark-worker
    container_name: spark-worker-2
    environment:
      - SPARK_WORKER_CORES=1
      - SPARK_WORKER_MEMORY=4g
    ports:
      - 8084:8081
    volumes:
      - shared-workspace:/opt/workspace
    depends_on:
      - spark-master

```

## Analysis

File type: `.yml`

---
*Generated: 2025-11-15T20:48:44.449188*

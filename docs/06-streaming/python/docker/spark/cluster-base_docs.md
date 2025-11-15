# cluster-base.Dockerfile

**Path**: `06-streaming/python/docker/spark/cluster-base.Dockerfile`
**Size**: 600 bytes
**Lines**: 21

## Source Code

```
# Reference from offical Apache Spark repository Dockerfile for Kubernetes
# https://github.com/apache/spark/blob/master/resource-managers/kubernetes/docker/src/main/dockerfiles/spark/Dockerfile
ARG java_image_tag=17-jre
FROM eclipse-temurin:${java_image_tag}

# -- Layer: OS + Python

ARG shared_workspace=/opt/workspace

RUN mkdir -p ${shared_workspace} && \
    apt-get update -y && \
    apt-get install -y python3 && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*

ENV SHARED_WORKSPACE=${shared_workspace}

# -- Runtime

VOLUME ${shared_workspace}
CMD ["bash"]
```

## Analysis

File type: `.Dockerfile`

---
*Generated: 2025-11-15T20:48:44.444934*

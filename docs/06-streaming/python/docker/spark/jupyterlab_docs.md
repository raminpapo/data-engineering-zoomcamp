# jupyterlab.Dockerfile

**Path**: `06-streaming/python/docker/spark/jupyterlab.Dockerfile`
**Size**: 389 bytes
**Lines**: 17

## Source Code

```
FROM cluster-base

# -- Layer: JupyterLab

ARG spark_version=3.3.1
ARG jupyterlab_version=3.6.1

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install wget pyspark==${spark_version} jupyterlab==${jupyterlab_version}

# -- Runtime

EXPOSE 8888
WORKDIR ${SHARED_WORKSPACE}
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=

```

## Analysis

File type: `.Dockerfile`

---
*Generated: 2025-11-15T20:48:44.450838*

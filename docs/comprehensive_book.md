# Data Engineering Zoomcamp - Complete Book

**Generated**: 2025-11-15T20:48:45.030982
**Files**: 298

## Introduction

This book contains documentation for all files in the repository.

## Contents


## .

- `.gitignore`
- `README.md`
- `after-sign-up.md`
- `asking-questions.md`
- `awesome-data-engineering.md`
- `certificates.md`
- `dataset.md`
- `learning-in-public.md`
- `repo_book_gen.py`
- `repo_book_gen_fast.py`

## 01-docker-terraform

- `README.md`

## 01-docker-terraform/1_terraform_gcp

- `1_terraform_overview.md`
- `2_gcp_overview.md`
- `README.md`
- `windows.md`

## 01-docker-terraform/1_terraform_gcp/terraform

- `README.md`

## 01-docker-terraform/1_terraform_gcp/terraform/terraform_basic

- `main.tf`

## 01-docker-terraform/1_terraform_gcp/terraform/terraform_with_variables

- `main.tf`
- `variables.tf`

## 01-docker-terraform/2_docker_sql

- `.gitignore`
- `Dockerfile`
- `README.md`
- `data-loading-parquet.ipynb`
- `data-loading-parquet.py`
- `docker-compose.yaml`
- `ingest_data.py`
- `pg-test-connection.ipynb`
- `pipeline.py`
- `upload-data.ipynb`

## 02-workflow-orchestration

- `README.md`

## 02-workflow-orchestration/docker/combined

- `docker-compose.yml`

## 02-workflow-orchestration/docker/kestra

- `docker-compose.yml`

## 02-workflow-orchestration/docker/postgres

- `docker-compose.yml`

## 02-workflow-orchestration/flows

- `01_getting_started_data_pipeline.yaml`
- `02_postgres_taxi.yaml`
- `02_postgres_taxi_scheduled.yaml`
- `03_postgres_dbt.yaml`
- `04_gcp_kv.yaml`
- `05_gcp_setup.yaml`
- `06_gcp_taxi.yaml`
- `06_gcp_taxi_scheduled.yaml`
- `07_gcp_dbt.yaml`

## 02-workflow-orchestration/images

- `homework.png`

## 03-data-warehouse

- `README.md`
- `big_query.sql`
- `big_query_hw.sql`
- `big_query_ml.sql`
- `extract_model.md`

## 03-data-warehouse/extras

- `README.md`
- `web_to_gcs.py`

## 04-analytics-engineering

- `README.md`
- `SQL_refresher.md`
- `dbt_cloud_setup.md`

## 04-analytics-engineering/docker_setup

- `Dockerfile`
- `README.md`
- `docker-compose.yaml`

## 04-analytics-engineering/taxi_rides_ny

- `.gitignore`
- `.gitkeep`
- `README.md`
- `dbt_project.yml`
- `package-lock.yml`
- `packages.yml`

## 04-analytics-engineering/taxi_rides_ny/analyses

- `.gitkeep`
- `hack-load-data.sql`

## 04-analytics-engineering/taxi_rides_ny/macros

- `.gitkeep`
- `get_payment_type_description.sql`
- `macros_properties.yml`

## 04-analytics-engineering/taxi_rides_ny/models/core

- `dim_zones.sql`
- `dm_monthly_zone_revenue.sql`
- `fact_trips.sql`
- `schema.yml`

## 04-analytics-engineering/taxi_rides_ny/models/staging

- `schema.yml`
- `stg_green_tripdata.sql`
- `stg_yellow_tripdata.sql`

## 04-analytics-engineering/taxi_rides_ny/seeds

- `.gitkeep`
- `seeds_properties.yml`
- `taxi_zone_lookup.csv`

## 04-analytics-engineering/taxi_rides_ny/snapshots

- `.gitkeep`

## 05-batch

- `.gitignore`
- `README.md`

## 05-batch/code

- `03_test.ipynb`
- `04_pyspark.ipynb`
- `05_taxi_schema.ipynb`
- `06_spark_sql.ipynb`
- `06_spark_sql.py`
- `06_spark_sql_big_query.py`
- `07_groupby_join.ipynb`
- `08_rdds.ipynb`
- `09_spark_gcs.ipynb`
- `cloud.md`
- `download_data.sh`
- `homework.ipynb`

## 05-batch/setup

- `hadoop-yarn.md`
- `linux.md`
- `macos.md`
- `pyspark.md`
- `windows.md`

## 05-batch/setup/config

- `core-site.xml`
- `spark-defaults.conf`
- `spark.dockerfile`

## 06-streaming

- `.gitignore`
- `README.md`

## 06-streaming/java/kafka_examples

- `.gitignore`
- `build.gradle`
- `gradlew`
- `gradlew.bat`
- `settings.gradle`

## 06-streaming/java/kafka_examples/build/generated-main-avro-java/schemaregistry

- `RideRecord.java`
- `RideRecordCompatible.java`
- `RideRecordNoneCompatible.java`

## 06-streaming/java/kafka_examples/gradle/wrapper

- `gradle-wrapper.jar`
- `gradle-wrapper.properties`

## 06-streaming/java/kafka_examples/src/main/avro

- `rides.avsc`
- `rides_compatible.avsc`
- `rides_non_compatible.avsc`

## 06-streaming/java/kafka_examples/src/main/java/org/example

- `AvroProducer.java`
- `JsonConsumer.java`
- `JsonKStream.java`
- `JsonKStreamJoins.java`
- `JsonKStreamWindow.java`
- `JsonProducer.java`
- `JsonProducerPickupLocation.java`
- `Secrets.java`
- `Topics.java`

## 06-streaming/java/kafka_examples/src/main/java/org/example/customserdes

- `CustomSerdes.java`

## 06-streaming/java/kafka_examples/src/main/java/org/example/data

- `PickupLocation.java`
- `Ride.java`
- `VendorInfo.java`

## 06-streaming/java/kafka_examples/src/main/resources

- `rides.csv`

## 06-streaming/java/kafka_examples/src/test/java/org/example

- `JsonKStreamJoinsTest.java`
- `JsonKStreamTest.java`

## 06-streaming/java/kafka_examples/src/test/java/org/example/helper

- `DataGeneratorHelper.java`

## 06-streaming/ksqldb

- `commands.md`

## 06-streaming/pyflink

- `.gitignore`
- `Dockerfile.flink`
- `LICENSE`
- `Makefile`
- `README.md`
- `docker-compose.yml`
- `homework.md`
- `requirements.txt`

## 06-streaming/pyflink/src/job

- `aggregation_job.py`
- `start_job.py`
- `taxi_job.py`

## 06-streaming/pyflink/src/producers

- `load_taxi_data.py`
- `producer.py`

## 06-streaming/python

- `README.md`
- `requirements.txt`

## 06-streaming/python/avro_example

- `consumer.py`
- `producer.py`
- `ride_record.py`
- `ride_record_key.py`
- `settings.py`

## 06-streaming/python/docker

- `README.md`
- `docker-compose.yml`

## 06-streaming/python/docker/kafka

- `docker-compose.yml`

## 06-streaming/python/docker/spark

- `build.sh`
- `cluster-base.Dockerfile`
- `docker-compose.yml`
- `jupyterlab.Dockerfile`
- `spark-base.Dockerfile`
- `spark-master.Dockerfile`
- `spark-worker.Dockerfile`

## 06-streaming/python/json_example

- `consumer.py`
- `producer.py`
- `ride.py`
- `settings.py`

## 06-streaming/python/redpanda_example

- `README.md`
- `consumer.py`
- `docker-compose.yaml`
- `producer.py`
- `ride.py`
- `settings.py`

## 06-streaming/python/resources

- `rides.csv`

## 06-streaming/python/resources/schemas

- `taxi_ride_key.avsc`
- `taxi_ride_value.avsc`

## 06-streaming/python/streams-example/faust

- `branch_price.py`
- `producer_taxi_json.py`
- `stream.py`
- `stream_count_vendor_trips.py`
- `taxi_rides.py`
- `windowing.py`

## 06-streaming/python/streams-example/pyspark

- `README.md`
- `consumer.py`
- `producer.py`
- `settings.py`
- `spark-submit.sh`
- `streaming-notebook.ipynb`
- `streaming.py`

## 06-streaming/python/streams-example/redpanda

- `README.md`
- `consumer.py`
- `docker-compose.yaml`
- `producer.py`
- `settings.py`
- `spark-submit.sh`
- `streaming-notebook.ipynb`
- `streaming.py`

## cohorts/2022

- `README.md`
- `project.md`

## cohorts/2022/week_1_basics_n_setup

- `homework.md`

## cohorts/2022/week_2_data_ingestion

- `README.md`

## cohorts/2022/week_2_data_ingestion/airflow

- `.env_example`
- `1_setup_official.md`
- `2_setup_nofrills.md`
- `Dockerfile`
- `README.md`
- `docker-compose-nofrills.yml`
- `docker-compose.yaml`
- `docker-compose_2.3.4.yaml`
- `requirements.txt`

## cohorts/2022/week_2_data_ingestion/airflow/dags

- `data_ingestion_gcs_dag.py`

## cohorts/2022/week_2_data_ingestion/airflow/dags_local

- `data_ingestion_local.py`
- `ingest_script.py`

## cohorts/2022/week_2_data_ingestion/airflow/extras

- `data_ingestion_gcs_dag_ex2.py`
- `web_to_gcs.sh`

## cohorts/2022/week_2_data_ingestion/airflow/scripts

- `entrypoint.sh`

## cohorts/2022/week_2_data_ingestion/homework

- `homework.md`
- `solution.py`

## cohorts/2022/week_2_data_ingestion/transfer_service

- `README.md`

## cohorts/2022/week_3_data_warehouse/airflow

- `.env_example`
- `1_setup_official.md`
- `2_setup_nofrills.md`
- `README.md`
- `docker-compose-nofrills.yml`
- `docker-compose.yaml`

## cohorts/2022/week_3_data_warehouse/airflow/dags

- `gcs_to_bq_dag.py`

## cohorts/2022/week_3_data_warehouse/airflow/scripts

- `entrypoint.sh`

## cohorts/2022/week_5_batch_processing

- `homework.md`

## cohorts/2022/week_6_stream_processing

- `homework.md`

## cohorts/2023

- `README.md`
- `leaderboard.md`
- `project.md`

## cohorts/2023/week_1_docker_sql

- `homework.md`

## cohorts/2023/week_1_terraform

- `homework.md`

## cohorts/2023/week_2_workflow_orchestration

- `README.md`
- `homework.md`

## cohorts/2023/week_3_data_warehouse

- `homework.md`

## cohorts/2023/week_4_analytics_engineering

- `homework.md`

## cohorts/2023/week_5_batch_processing

- `homework.md`

## cohorts/2023/week_6_stream_processing

- `client.properties`
- `homework.md`
- `producer_confluent.py`
- `settings.py`
- `spark-submit.sh`
- `streaming_confluent.py`

## cohorts/2023/workshops

- `piperider.md`

## cohorts/2024

- `README.md`
- `leaderboard.md`
- `project.md`

## cohorts/2024/01-docker-terraform

- `homework.md`
- `solutions.md`

## cohorts/2024/02-workflow-orchestration

- `README.md`
- `homework.md`

## cohorts/2024/03-data-warehouse

- `homework.md`

## cohorts/2024/04-analytics-engineering

- `homework.md`

## cohorts/2024/05-batch

- `homework.md`

## cohorts/2024/06-streaming

- `docker-compose.yml`
- `homework.md`

## cohorts/2024/workshops

- `dlt.md`
- `rising-wave.md`

## cohorts/2024/workshops/dlt_resources

- `data_ingestion_workshop.md`
- `homework_solution.ipynb`
- `homework_starter.ipynb`
- `incremental_loading.png`
- `workshop.ipynb`

## cohorts/2025

- `README.md`
- `project.md`

## cohorts/2025/01-docker-terraform

- `homework.md`
- `solution.md`

## cohorts/2025/02-workflow-orchestration

- `homework.md`
- `solution.md`

## cohorts/2025/03-data-warehouse

- `DLT_upload_to_GCP.ipynb`
- `homework.md`
- `load_yellow_taxi_data.py`

## cohorts/2025/04-analytics-engineering

- `homework.md`
- `homework_q2.png`

## cohorts/2025/05-batch

- `homework.md`

## cohorts/2025/05-batch/homework

- `solution.ipynb`

## cohorts/2025/06-streaming

- `homework.md`

## cohorts/2025/06-streaming/homework

- `homework.ipynb`

## cohorts/2025/workshops

- `dynamic_load_dlt.py`

## cohorts/2025/workshops/dlt

- `README.md`
- `data_ingestion_workshop.md`
- `dlt_homework.md`

## cohorts/2025/workshops/dlt/img

- `Rest_API.png`
- `dlt.png`
- `pipes.jpg`

## images

- `dlthub.png`
- `kestra.svg`
- `mage.svg`
- `piperider.png`
- `rising-wave.png`

## images/architecture

- `arch_v3_workshops.jpg`
- `arch_v4_workshops.jpg`
- `photo1700757552.jpeg`

## images/aws

- `iam.png`

## projects

- `README.md`
- `datasets.md`

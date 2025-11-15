# core-site.xml

**Path**: `05-batch/setup/config/core-site.xml`
**Size**: 661 bytes
**Lines**: 21

## Source Code

```
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<configuration>
  <property>
    <name>fs.AbstractFileSystem.gs.impl</name>
    <value>com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS</value>
  </property>
  <property>
    <name>fs.gs.impl</name>
    <value>com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem</value>
  </property>
  <property>
    <name>fs.gs.auth.service.account.json.keyfile</name>
    <value>/home/alexey/.google/credentials/google_credentials.json</value>
  </property>
  <property>
    <name>fs.gs.auth.service.account.enable</name>
    <value>true</value>
  </property>
</configuration>
```

## Analysis

File type: `.xml`

---
*Generated: 2025-11-15T20:48:44.564582*

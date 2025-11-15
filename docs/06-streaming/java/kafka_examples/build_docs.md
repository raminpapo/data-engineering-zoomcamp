# build.gradle

**Path**: `06-streaming/java/kafka_examples/build.gradle`
**Size**: 1,053 bytes
**Lines**: 37

## Source Code

```
plugins {
    id 'java'
    id "com.github.davidmc24.gradle.plugin.avro" version "1.5.0"
}


group 'org.example'
version '1.0-SNAPSHOT'

repositories {
    mavenCentral()
    maven {
        url "https://packages.confluent.io/maven"
    }
}

dependencies {
    implementation 'org.apache.kafka:kafka-clients:3.3.1'
    implementation 'com.opencsv:opencsv:5.7.1'
    implementation 'io.confluent:kafka-json-serializer:7.3.1'
    implementation 'org.apache.kafka:kafka-streams:3.3.1'
    implementation 'io.confluent:kafka-avro-serializer:7.3.1'
    implementation 'io.confluent:kafka-schema-registry-client:7.3.1'
    implementation 'io.confluent:kafka-streams-avro-serde:7.3.1'
    implementation "org.apache.avro:avro:1.11.0"
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.8.1'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.8.1'
    testImplementation 'org.apache.kafka:kafka-streams-test-utils:3.3.1'
}

sourceSets.main.java.srcDirs = ['build/generated-main-avro-java','src/main/java']

test {
    useJUnitPlatform()
}


```

## Analysis

File type: `.gradle`

---
*Generated: 2025-11-15T20:48:44.459255*

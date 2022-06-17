# Jaegertracing with Elastic storage

## Overview

This is an example on how to set up Jaegertracing with Elasticsearch

## How to run

```shell
# in the same dir as docker-compose.yaml
docker-compose up
```
then go to http://localhost:5601 to view kibana and to http://localhost:16686 to view jaeger dashboard

## Trace structure in elastic

Jaeger saves two data types in elastic: services and traces

### Service example

A new document is created for each new span type (operation) and service:

```json
{
  "serviceName": "my-helloworld-service",
  "operationName": "do_roll"
}
```

### Trace example

```json
{
  "traceID": "627d10b63c90e9c731099da011a0bfe7",
  "spanID": "d34477055889e04c",
  "flags": 1,
  "operationName": "do_roll",
  "references": [],
  "startTime": 1655501501844706,
  "startTimeMillis": 1655501501844,
  "duration": 0,
  "tags": [
    {
      "key": "roll.value",
      "type": "int64",
      "value": "3"
    },
    {
      "key": "telemetry.sdk.language",
      "type": "string",
      "value": "python"
    },
    {
      "key": "telemetry.sdk.name",
      "type": "string",
      "value": "opentelemetry"
    },
    {
      "key": "telemetry.sdk.version",
      "type": "string",
      "value": "1.11.1"
    },
    {
      "key": "service.name",
      "type": "string",
      "value": "my-helloworld-service"
    },
    {
      "key": "span.kind",
      "type": "string",
      "value": "internal"
    },
    {
      "key": "otel.library.name",
      "type": "string",
      "value": "__main__"
    },
    {
      "key": "otel.library.version",
      "type": "string",
      "value": ""
    },
    {
      "key": "otel.scope.name",
      "type": "string",
      "value": "__main__"
    },
    {
      "key": "otel.scope.version",
      "type": "string",
      "value": ""
    },
    {
      "key": "internal.span.format",
      "type": "string",
      "value": "proto"
    }
  ],
  "logs": [],
  "process": {
    "serviceName": "my-helloworld-service",
    "tags": []
  }
}
```
# Jaegertracing with Elastic storage

## How to run

```shell
# in the same dir as docker-compose.yaml
docker-compose up
```
then go to http://localhost:5601 to view kibana and to http://localhost:16686 to view jaeger dashboard

## Trace structure in elastic
```json
{
  "_index": "jaeger_-jaeger-span-2022-06-17",
  "_type": "_doc",
  "_id": "JODwcYEBjUYyNQ2yScdw",
  "_version": 1,
  "_score": 1,
  "_source": {
    "traceID": "76a6179050846406",
    "spanID": "6b85a85cdb4a6421",
    "flags": 1,
    "operationName": "FindTraces",
    "references": [
      {
        "refType": "CHILD_OF",
        "traceID": "76a6179050846406",
        "spanID": "76a6179050846406"
      }
    ],
    "startTime": 1655473981310306,
    "startTimeMillis": 1655473981310,
    "duration": 33512,
    "tags": [
      {
        "key": "internal.span.format",
        "type": "string",
        "value": "proto"
      }
    ],
    "logs": [],
    "process": {
      "serviceName": "jaeger-query",
      "tags": [
        {
          "key": "jaeger.version",
          "type": "string",
          "value": "Go-2.30.0"
        },
        {
          "key": "hostname",
          "type": "string",
          "value": "d744869a5038"
        },
        {
          "key": "ip",
          "type": "string",
          "value": "172.21.0.2"
        },
        {
          "key": "client-uuid",
          "type": "string",
          "value": "69e6731753ffaf54"
        }
      ]
    }
  },
  "fields": {
    "traceID": "76a6179050846406",
    "duration": 33512,
    "spanID": "6b85a85cdb4a6421",
    "startTimeMillis": "2022-06-17T13:53:01.310Z",
    "references": [
      {
        "spanID":  "76a6179050846406",
        "traceID": "76a6179050846406",
        "refType": "CHILD_OF"
      }
    ],
    "process.tags": [
      {
        "type": "string",
        "value": "Go-2.30.0",
        "key": "jaeger.version"
      },
      {
        "type": "string",
        "value": "d744869a5038",
        "key": "hostname"
      },
      {
        "type": "string",
        "value": "172.21.0.2",
        "key": "ip"
      },
      {
        "type": "string",
        "value": "69e6731753ffaf54",
        "key": "client-uuid"
      }
    ],
    "process.serviceName": "jaeger-query",
    "flags": [
      1
    ],
    "startTime": 1655473981310306,
    "operationName": "FindTraces",
    "tags": [
      {
        "type": "string",
        "value": "proto",
        "key": "internal.span.format"
      }
    ]
  }
}
```
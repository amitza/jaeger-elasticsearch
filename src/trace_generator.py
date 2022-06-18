import random
import string
import time
import uuid
from datetime import datetime

from elasticsearch import Elasticsearch


class TraceGenerator(object):
    service_index_prefix: str = 'jaeger_-jaeger-service-'
    span_index_prefix: str = 'jaeger_-jaeger-span-'

    def __init__(self, host: str, port: int):
        self.client: Elasticsearch = Elasticsearch(hosts=f'{host}:{port}')

    @staticmethod
    def _generate_span_id() -> str:
        return format(random.getrandbits(64), "016x")

    @staticmethod
    def _generate_trace_id() -> str:
        return format(random.getrandbits(128), "032x")

    @staticmethod
    def _mock_service_doc(service: str, operation: str) -> dict:
        return {
            "serviceName": service,
            "operationName": operation
        }

    @staticmethod
    def _mock_trace_doc(service: str, operation: str) -> dict:
        print(f'new span from {int(time.time())}')
        now: datetime = datetime.now()
        mili = now.microsecond
        return {
            "traceID": TraceGenerator._generate_trace_id(),
            "spanID": TraceGenerator._generate_span_id(),
            "operationName": operation,
            "startTime": 1655593978886242,  # mili,
            "startTimeMillis": 1655593978886,  # mili,
            "duration": random.randint(0, 10),
            "process": {
                "serviceName": service,
            }
        }

    def new_trace(self, service: str, operation: str) -> None:
        now: datetime = datetime.now()
        suffix: str = now.strftime("%Y-%m-18")

        print(self.client.index(index=f'{self.service_index_prefix}{suffix}',
                                document=self._mock_service_doc(service=service, operation=operation)))

        print(self.client.index(index=f'{self.span_index_prefix}{suffix}',
                                document=self._mock_trace_doc(service=service, operation=operation)))


if __name__ == '__main__':
    trace_gen = TraceGenerator(host='localhost', port=9200)
    trace_gen.new_trace(service='zafi', operation='zafi_action')

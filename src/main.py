import datetime
import logging
import random
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Resource can be required for some backends, e.g. Jaeger
# If resource wouldn't be set - traces wouldn't appear in Jaeger
resource = Resource(attributes={
    "service.name": "service"
})

trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

span_processor = BatchSpanProcessor(otlp_exporter)

trace.get_tracer_provider().add_span_processor(span_processor)

logging.info(f'Starting application')

while 1:
    logging.info(f'Current {datetime.datetime.now()}')
    with tracer.start_as_current_span("do_roll") as span:
        res = random.randint(1, 6)
        span.set_attribute("roll.value", res)
        with tracer.start_span('child span') as child_span:
            res = random.randint(1, 6)
            child_span.set_attribute("roll.value", res)

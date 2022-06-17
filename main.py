import random
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider, Tracer, Span
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from opentelemetry import trace

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "my-helloworld-service"})
    )
)
# Acquire a tracer. There's one set up for you globally,
# and it's also used by opentelemetry-instrument.
tracer: Tracer = trace.get_tracer(__name__)

jaeger_exporter = JaegerExporter(
    agent_host_name='localhost',
    agent_port=6831,
)

# Create a BatchSpanProcessor and add the exporter to it
span_processor = BatchSpanProcessor(jaeger_exporter)

# add to the tracer
trace.get_tracer_provider().add_span_processor(span_processor)

with tracer.start_as_current_span("do_roll") as span:
    span: Span = span
    res = random.randint(1, 6)
    span.set_attribute("roll.value", res)
    with tracer.start_span('child span') as child_span:
        res = random.randint(1, 6)
        child_span.set_attribute("roll.value", res)

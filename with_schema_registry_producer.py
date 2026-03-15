import uuid
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

# Define the schema
value_schema_str = """
{
  "namespace": "orders",
  "type": "record",
  "name": "Order",
  "fields": [
    {"name": "order_id", "type": "string"},
    {"name": "user", "type": "string"},
    {"name": "item", "type": "string"},
    {"name": "quantity", "type": "int"}
  ]
}
"""

value_schema = avro.loads(value_schema_str)

producer_config = {
    "bootstrap.servers": "localhost:9092",
    "schema.registry.url": "http://localhost:8081"
}

producer = AvroProducer(producer_config, default_value_schema=value_schema)

order = {
    "order_id": str(uuid.uuid4()),
    "user": "lara",
    "item": "frozen yogurt",
    "quantity": 10
}

producer.produce(topic="orders", value=order)

producer.flush()
print(f"✅ Produced order: {order}")

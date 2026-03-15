from confluent_kafka.avro import AvroConsumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "schema.registry.url": "http://localhost:8081",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest"
}

consumer = AvroConsumer(consumer_config)
consumer.subscribe(["orders"])

print("🟢 Consumer is running and subscribed to 'orders' topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        order = msg.value()
        print(f"📦 Received order: {order['quantity']} x {order['item']} from {order['user']}")
except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")
finally:
    consumer.close()

# kafka-course

[Kafka Course](https://gitlab.com/twn-youtube/kafka-crash-course)

### Install confluent-kafka dependency
`pip3 install confluent-kafka`

### Validate that the topic was created in kafka container
`docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092`

### Describe that topic and see its partitions
`docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic new_orders`

#### View all events in a topic
`docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning`

##

### Apache Kafka Schema Registry – Basic Info

**Apache Kafka** is a distributed streaming platform used for building real-time data pipelines and event-driven applications. While Kafka handles high-throughput messaging, it doesn’t enforce strict data formats. This is where Schema Registry comes in.

**Schema Registry** is a separate service that manages schemas for Kafka messages (usually in Avro, JSON Schema, or Protobuf formats). It ensures that producers and consumers of Kafka topics can agree on the structure of data, preventing serialization errors and enabling data evolution.

**Key Features:**
1. Centralized Schema Management: Stores all schemas for Kafka topics in one place.
2. Compatibility Checks: Ensures backward or forward compatibility of schemas to prevent breaking changes.
3. Integration with Kafka Producers/Consumers: Automatically serializes and deserializes messages according to the registered schema.
4. Supports Multiple Formats: Commonly Avro, JSON Schema, and Protobuf.

**Benefits:**
- Data Quality & Consistency: Prevents malformed data from entering Kafka topics.
- Easier Schema Evolution: You can update schemas safely without breaking existing consumers.
- Interoperability: Producers and consumers written in different languages can use the same schema definitions.

**Typical Workflow:**
1. Producer registers the schema with Schema Registry.
2. Producer serializes the message using the schema and sends it to Kafka.
3. Consumer retrieves the schema from Schema Registry and deserializes the message.

# Kafka REST API

## Installation
If you are installing from a remote repository pre-configured in *pip*, run: `pip install kafka-rest-api`.
If you are installing from a *wheel* file in the local directory, run: `pip install {filename}.whl`, and replace `{filename}` with the name of the *.whl* file.

## Getting Started
Interactions with a Kafka cluster can be performed on a Producer/Consumer paradigm. As such there are two classes that
can be imported and used to publish and subscribe to topics in Kafka: **Producer** and **Consumer**.

## Configuration
When using this package to access Merck API Gateway in Dev environment, make sure to define the following environment variables:
- **KAFKA_REST_API_URL**: Target Kafka REST API URL.
- **X_API_KEY**: The authorization token to validate API requests to API Gateway.

This variables can be passed to **Producer** and **Consumer** classes as a dictionary, for example:
```python
auth_headers = {"x-api-key": "<YOUR_X_API_KEY>"}
```

If *KAFKA_REST_API_URL* is not defined as an environment variable, you can provide the API URL
directly to the *Producer* or *Consumer* classes, like:
```python
producer = Producer(kafka_rest_api_url="<YOUR_REST_API_URL>")
consumer = Consumer(kafka_rest_api_url="<YOUR_REST_API_URL>")
```

### Producer
In the snippet below we use the topic *pke* as example. The pattern for the producer is the following:
```python
from kafka_rest import Producer
producer = Producer(auth_headers=auth_headers)
keys = producer.produce(producer_messages, "pke")
```

The `Producer.produce` method automatically generates each message unique key (UUID) for you. 
You can optionally provide your unique keys as well. For more information, please consult this method's docstring.

### Consumer
To import the consumer:
```python
from kafka_rest import Consumer
```

You can choose one the following patterns to define the *Consumer*:
- Pattern 1 - Instantiation via context manager:
```python
    with Consumer(topics=["pke-response"], auth_headers=auth_headers) as consumer:
        new_data = consumer.consume_all(keys)
```
- Pattern 2 - Step-by-step instantiation:
```python
    consumer = Consumer(auth_headers=auth_headers)
    consumer.create()
    consumer.subscribe(topics=["pke-response"])
    consumed_data = consumer.consume_all(keys)  # or consumer.create().subscribe().consume_all(keys)
    consumer.delete()
```
- Pattern 3 - Consumer with iterator:
```python
    with Consumer(topics=["pke-response"], auth_headers=auth_headers) as consumer:
        for iter_data in consumer.consume(keys):
            print("Iterator Data:", iter_data)
```

- Produce files as inputs and consume outputs.
```python
    messages = []
    for name in file_names:
        with open(f"snippet/{name}", "rb") as f:
            messages.append({"name": name, "bytes": f.read(), "type": "application/pdf"})

    producer = Producer(auth_headers=auth_headers)
    new_keys = producer.produce_files(messages, topic_for_files)

    with Consumer(topics=f"{topic_for_files}-response", auth_headers=auth_headers) as consumer:
        for i, iter_data in enumerate(consumer.consume(new_keys, interval_sec=1)):
            if iter_data:
                print(f"Output: {iter_data}")
```

For a complete snippet, please check the example in the file `kafka_rest/kafka_rest.py` in this repo.
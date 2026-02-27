from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

customers = [
    {"customer_id": 1, "customer_name": "cus_a"},
    {"customer_id": 2, "customer_name": "cus_b"},
    {"customer_id": 3, "customer_name": "cus_c"}
]

for customer in customers:
    producer.send("customer-landing", customer)

producer.flush()

print("Sent to customer-landing")
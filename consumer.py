from kafka import KafkaConsumer
import json
import csv

consumer = KafkaConsumer(
    'customer-transform',
    bootstrap_servers='localhost:9092'
)

with open('customer_output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["customer_id", "customer_name", "last_update"])

    for message in consumer:
        decoded = message.value.decode('utf-8')
        data = json.loads(decoded)

        writer.writerow([
            data["customer_id"],
            data["customer_name"],
            data["last_update"]
        ])

        f.flush()
        print("Saved:", data)
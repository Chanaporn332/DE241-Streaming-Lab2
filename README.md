# DE241 Streaming Pipeline Lab2

This project demonstrates a simple streaming pipeline using:

- Apache Kafka
- Zookeeper
- Python Producer
- Faust Transform
- Python Consumer
- Docker Compose

## How to Run
1. Start services:
   docker-compose up -d
2. Run producer:
   python producer.py
3. Run Faust worker:
   faust -A transform worker -l info
4. Run consumer:
   python consumer.py
Output will be written to customer_output.csv
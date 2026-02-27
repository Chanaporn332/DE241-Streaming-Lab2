import faust
import json
from datetime import datetime

app = faust.App(
    'customer_stream_app',
    broker='kafka://localhost:9092',
    value_serializer='raw'
)

customer_landing_topic = app.topic('customer-landing')
customer_transform_topic = app.topic('customer-transform')

@app.agent(customer_landing_topic)
async def process(stream):
    async for event in stream:
        data = json.loads(event)
        data['last_update'] = str(datetime.now())

        await customer_transform_topic.send(
            value=json.dumps(data).encode('utf-8')
        )

if __name__ == '__main__':
    app.main()
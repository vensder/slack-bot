from datetime import datetime
from time import time


def hello(data, web_client):

    if 'utc' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        utc_now = datetime.utcnow()
        event_ts = data['event_ts']
        epoch_time = time()

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hello <@{user}>! UTC: {utc_now}, event ts: {event_ts}, epoch time: {epoch_time}",
            thread_ts=thread_ts
        )

def hello(data, web_client):

    if '' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hello <@{user}>!",
            thread_ts=thread_ts
        )
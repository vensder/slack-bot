import slack
import yaml


with open('conf/conf.yaml', 'r') as conf_yaml:
    bot_conf = yaml.load(conf_yaml)

slack_token = bot_conf['slack']['slack_token']


@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    print(data)
    print("="*80)
    web_client = payload['web_client']
    #rtm_client = payload['rtm_client']
    if 'hello' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hello <@{user}>!",
            thread_ts=thread_ts
        )

rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()

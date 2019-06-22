import slack
import yaml

from hello import hello

with open('conf/conf.yaml', 'r') as conf_yaml:
    bot_conf = yaml.load(conf_yaml)

slack_token = bot_conf['slack']['slack_token']
bot_id = bot_conf['slack']['bot_id']


@slack.RTMClient.run_on(event='hello')
def hello_event(**payload):
    web_client = payload['web_client']
    bots_info = web_client.bots_info(bot=bot_id)
    print('hello event')
    bot_user_id = bots_info['bot']['user_id']
    print(bot_user_id)
    users_info = web_client.users_info(user=bot_user_id)
    print(users_info)


@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    print(data)
    print("="*80)
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if 'text' in data and 'user' in data:
        hello.hello(data, web_client)


rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()

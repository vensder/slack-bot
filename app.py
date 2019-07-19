#!/usr/bin/env python3

import slack
import yaml

from plugins import hello, ip_calc, ssl_expiry

with open('conf/conf.yaml', 'r') as conf_yaml:
    bot_conf = yaml.safe_load(conf_yaml)

slack_token = bot_conf['slack']['slack_token']
bot_user_id = ''


@slack.RTMClient.run_on(event='hello')
def hello_event(**payload):
    global bot_user_id
    web_client = payload['web_client']
    print('hello event')
    response = web_client.auth_test()
    bot_user_id = response.data['user_id']
    users_info = web_client.users_info(user=bot_user_id)
    print(bot_user_id)
    print(users_info)


@slack.RTMClient.run_on(event='message')
def load_plugins(**payload):
    global bot_user_id
    data = payload['data']
    print(data)
    print("="*80)
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if ('text' in data) and ('user' in data) and (f"<@{bot_user_id}>" in data['text']):
        hello.hello(data, web_client)
        ip_calc.ip_calc(data, web_client, bot_user_id)
        ssl_expiry.ssl_expiry(data, web_client, bot_user_id)


rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()

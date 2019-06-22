import slack
import yaml

#import hello
from hello import hello

with open('conf/conf.yaml', 'r') as conf_yaml:
    bot_conf = yaml.load(conf_yaml)

slack_token = bot_conf['slack']['slack_token']


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
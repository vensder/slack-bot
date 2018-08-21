import time
from slackclient import SlackClient
import yaml


users_ids_dict = dict()
users_names_dict= dict()

with open('conf/conf.yaml', 'r') as conf_yaml:
    bot_conf = yaml.load(conf_yaml)

slack_token = bot_conf['slack']['slack_token']

sc = SlackClient(slack_token)

if sc.rtm_connect(with_team_state=False, auto_reconnect=True):
    while sc.server.connected is True:
        for item in sc.rtm_read():
            print(item)
            if 'user' in item:
                print('user:', item['user'])
                user = sc.api_call("users.info", user=item['user'])
                users_ids_dict[item['user']] = {'name': user['user']['name'],
                                            'tz': user['user']['tz'],
                                            'tz_offset': user['user']['tz_offset']}
                users_names_dict[user['user']['name']] = {'id': item['user'],
                                            'tz': user['user']['tz'],
                                            'tz_offset': user['user']['tz_offset']}
                print(users_ids_dict)
                print(users_names_dict)
#                print(user['user']['name'])
                '''
                    'user': 
                        {'tz_offset': 10800, 
                        'tz_label': 'Moscow Time',
                        'is_ultra_restricted': False, 
                        'name': 'vensder', 
                        'profile': 
                            {
                            }, 
                        'real_name': 'Foo Bar', 
                        'is_bot': False, 
                        'is_restricted': False, 
                        'color': '9f69e7', 
                        'id': 'FOOBARFOO', 
                        'is_owner': True, 
                        'is_admin': True, 
                        'is_primary_owner': True, 
                        'is_app_user': False, 
                        'deleted': False, 
                        'tz': 'Europe/Moscow', 
                        'team_id': 'BAARFOO', 
                        'updated': 1534759036},
                'ok': True}'''

        time.sleep(1)
else:
    print("Connection Failed")
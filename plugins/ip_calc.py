import ipcalc

except_phrase = 'Try something like this: ```@ipcalc 10.0.0.0/24```'
outputs = []

def ip_calc(data, web_client, bot_user_id):

    if '@ipcalc' in data['text'] and except_phrase not in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        output_string = ''

        #network = ipcalc.Network('10.0.0.0/24')
        print(data['text'])
        network_string = data['text'].replace('@ipcalc', '').replace(f"<@{bot_user_id}>", '').strip() #text.lstrip('ipcalc ').strip('abcdefghijklmnopqrstuvwxyz ')
        print(network_string)
        network = ipcalc.Network(network_string)

        output_string += '```'
        output_string += str(network.network()) + '/' + str(network.mask) + ' (network/mask)\n'
        output_string += str(network.host_first()) + ' (first host)\n' # IP('172.16.42.1')
        output_string += str(network.host_last()) + ' (last host)\n' # IP('172.16.42.2')
        output_string += str(network.netmask()) + ' (netmask)\n' # 30
        output_string += str(network.size()) + ' (size)\n'  # 4
        output_string += str(network.info()) + ' (network type)\n' # 'PRIVATE'
        output_string += '```'


        web_client.chat_postMessage(
            channel=channel_id,
            text=output_string,
            thread_ts=thread_ts
        )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import ipcalc

# outputs = []

# def process_message(data):
    
#     if 'text' in data and data['text']:
#         try:
#             text = data['text']
#             channel = data['channel']
#             except_phrase = 'Try something like this: ```@ipcalc 10.0.0.0/24```'

#             if '@ipcalc' in text and except_phrase not in text:
                
#                 output_string = ''
#                 emoji = ':spider_web:'
#                 except_emoji = ':exclamation:'
#                 bot_name = 'ip calculator'
                
#                 network = ipcalc.Network('10.0.0.0/24')
#                 network_string = text.replace('@ipcalc', '').strip() #text.lstrip('ipcalc ').strip('abcdefghijklmnopqrstuvwxyz ')
                
#                 try:
#                     network = ipcalc.Network(network_string)
#                 except Exception as e:
#                     outputs.append([channel, str(e) + '. ' + except_phrase, bot_name, except_emoji ])
#                     print('Exception in ipcalculator: ', e)
#                     print('network: ', network_string)
                
#                 try:
#                     output_string += '```'
#                     output_string += str(network.network()) + '/' + str(network.mask) + ' (network/mask)\n'
#                     output_string += str(network.host_first()) + ' (first host)\n' # IP('172.16.42.1')
#                     output_string += str(network.host_last()) + ' (last host)\n' # IP('172.16.42.2')
#                     output_string += str(network.netmask()) + ' (netmask)\n' # 30
#                     output_string += str(network.size()) + ' (size)\n'  # 4
#                     output_string += str(network.info()) + ' (network type)\n' # 'PRIVATE'
#                     output_string += '```'

#                     outputs.append([channel, output_string, bot_name, emoji ])

#                 except Exception as e:
#                     outputs.append([channel, str(e) + '. ' + except_phrase, bot_name, except_emoji ])
#                     print('Exception in ipcalculator: ',e)
#                     print('network: ', network_string)


#         except KeyError as e:
#             print('KeyError Exception in ipcalculator.py: ', e)
#             print(data)
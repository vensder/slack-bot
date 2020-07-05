import ipcalc

except_phrase = 'Try something like this: ```!ipcalc 10.0.0.0/24```'
outputs = []

network_template = """
```
Network: {}/{}
HostMin: {}
HostMax: {}
Netmask: {}
NetSize: {}
NetType: {}
```
"""


def ip_calc(data, web_client, bot_user_id):

    if '!ipcalc' in data['text'] and except_phrase not in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        emoji = ':heavy_check_mark:'

        print(data['text'])
        network_string = data['text'].replace(
            '!ipcalc', '').replace(f"<@{bot_user_id}>", '').strip()
        print(network_string)

        try:
            network = ipcalc.Network(network_string)
            output_string = network_template.format(
                str(network.network()), str(network.mask),
                str(network.host_first()),
                str(network.host_last()),
                str(network.netmask()),
                str(network.size()),
                str(network.info())
            )

        except Exception as e:
            emoji = ':exclamation:'
            output_string = str(e)
            print('Exception in ipcalculator: ', e)
            print('network: ', network_string)

        web_client.chat_postMessage(
            icon_emoji=emoji,
            channel=channel_id,
            text=output_string,
            thread_ts=thread_ts
        )

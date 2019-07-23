import socket
import ssl
import datetime
import re
import OpenSSL                                                                                                                                              

trigger_phrase = '@ssl date'


def get_ssl_expiry_datetime_v2(hostname):
    ssl_date_fmt = r'%Y%m%d%H%M%SZ'        
    cert = ssl.get_server_certificate((hostname, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    return datetime.datetime.strptime(x509.get_notAfter().decode("utf-8"), ssl_date_fmt)    


def get_ssl_expiry_datetime(hostname):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 3 second timeout
    conn.settimeout(3.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    # parse the string from the certificate into a Python datetime object
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt) # 2016-04-19 23:59:59 # <class 'datetime.datetime'>


def ssl_expiry(data, web_client, bot_user_id):
    print('started ssl expiry')
    
    if trigger_phrase in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        output_string = ''

        text = data['text']
        
        mask = re.compile(r'([A-Za-z0-9-]+\.)+\w+') # domain pattern
        if mask.search(text):
            search_domain = mask.search(text)
            domain = search_domain.group()
            
            print(domain); print(type(domain))
            
            try:
                expiry_datetime = get_ssl_expiry_datetime(domain)
                now = datetime.datetime.now()
                delta = expiry_datetime - now
                
                emoji = ':white_check_mark:'
                if delta.days < 30:
                    emoji = ':warning:'
                output_string = emoji + 'Certificate for domain ' + domain + ' will expire in ' + str(delta.days) + ' days (' + str(expiry_datetime) + ')'
                print(output_string)

                web_client.chat_postMessage(
                    channel=channel_id,
                    text=output_string,
                    thread_ts=thread_ts
                )
                
            except Exception as e:
                emoji = ':exclamation:'
                output_string = emoji + 'SSL checker' + str(e) + ': ' + domain
                web_client.chat_postMessage(
                    channel=channel_id,
                    text=output_string,
                    thread_ts=thread_ts
                )                        
                print('Exception in ssl plugin: ',e)
                print('network: ', domain)
                
            
                try:
                    expiry_datetime = get_ssl_expiry_datetime_v2(domain)
                    now = datetime.datetime.now()
                    delta = expiry_datetime - now
                    
                    emoji = ':white_check_mark:'
                    if delta.days < 30:
                        emoji = ':warning:'
                    output_string = emoji + 'Certificate for domain ' + domain + ' will expire in ' + str(delta.days) + ' days (' + str(expiry_datetime) + ')'
                    print(output_string)

                    web_client.chat_postMessage(
                        channel=channel_id,
                        text=output_string,
                        thread_ts=thread_ts
                    )
                    
                except Exception as e:
                    emoji = ':exclamation:'
                    output_string = emoji + 'SSL checker' + str(e) + ': ' + domain
                    web_client.chat_postMessage(
                        channel=channel_id,
                        text=output_string,
                        thread_ts=thread_ts
                    )                        
                    print('Exception in ssl plugin: ',e)
                    print('network: ', domain)
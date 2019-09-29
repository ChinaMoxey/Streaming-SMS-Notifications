import requests
from twilio.rest import Client

client = Client('ACe5aa69f71c6bf6bebe576b1f70f7e0ec', '09e85de94263a338049d8d98db398265')

endpoint = "https://api.twitch.tv/helix/streams?"
headers = {"Client-ID": "enp5mqv5b6ch985adf2c1wqenehyfe"}
params = {"user_login": "Blacktut"}
response = requests.get(endpoint, params=params, headers=headers)
json_response = response.json()
streams = json_response.get('data', [])
is_active = lambda stream:stream.get('type') == 'live'
streams_active = filter(is_active, streams)
at_least_one_stream_active = any(streams_active)

last_messages_sent = client.messages.list(limit=1)
if last_messages_sent:
	 last_message_id = last_messages_sent[0].sid
	 last_message_data = client.messages(last_message_id).fetch()
	 last_message_content = last_message_data.body
	 online_notified= 'LIVE' in last_message_content
	 offline_notified= not online_notified

else:
	online_notified, offline_notified = False, False

online_notified, offline_notified = False, False
if at_least_one_stream_active and not online_notified:
	print("File Test")
	client.messages.create(body='Your streamer is Live !!!',from_='+12055462716',to='+13478337658')
if not at_least_one_stream_active and not offline_notified:
	client.messages.create(body='Offline !!!',from_= '+12055462716',to= '+13478337658')

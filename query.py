#requests is the go package in python to make http request
#https://2.python-requests.org/en/master
import requests

#This is one of the route where Twitch expose data
endpoint = "https://api.twitch.tv/helix/streams?"

#Passing the api key through the header
headers = {"Client-ID": "enp5mqv5b6ch985adf2c1wqenehyfe"}

# The previously set endpoint needs some parameter, here, the Twitcher we want to follow

params = {"user_login": "BlackTut"}


#Making the actual request
response = requests.get(endpoint, params=params,
headers=headers)
print(response.json())

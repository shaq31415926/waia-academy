import os
import requests

os.system("clear")  # use cls if windows

# ask the user for input
print("Welcome to my Horoscope Generator")
user_sign = input("What is your star sign?:")
user_sign = user_sign.lower()

# make a request to ohmanda for the user star sign
horoscope_url = "https://ohmanda.com/api/horoscope/"

# if you see response 200 that means you were able to make a connection to the ohmanda api for your users sign
print(requests.get(url=horoscope_url + user_sign))

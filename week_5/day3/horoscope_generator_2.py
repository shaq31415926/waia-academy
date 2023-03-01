import os
import requests

os.system("clear")

print("-"*50)
print("Welcome to my Horoscope Generator")
print("-"*50)
user_sign = input("What is your star sign?:")
user_sign = user_sign.lower() # lowercase the input

horoscope_url = "https://ohmanda.com/api/horoscope/"

# try some code, and if it does not return anything the except statement will print a message
try:
    # code that gets the user sign from the horoscope api
    # .json wraps this into a dictionary so we can select the horoscope key
    horoscope = requests.get(url = horoscope_url + user_sign).json()["horoscope"]

    # code that formats the output but keep it simple and use the commented out version
    print("-"*100, "\n", horoscope, "\n", "-"*100)
    # print("Your horoscope is:", horoscope)
except:
    print("Please double check the star sign you entered")
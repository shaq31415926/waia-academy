import os
import requests

os.system("clear")  # use cls if windows

# ask the user for input
print("Welcome to my Horoscope Generator")
user_sign = input("What is your star sign?:")
user_sign = user_sign.lower()

# make a request to ohmanda for the user star sign
horoscope_url = "https://ohmanda.com/api/horoscope/"

try:
    # code that gets the user sign from the horoscope api
    # .json() wraps this into a dictionary so we can fetch the horoscope
    horoscope_dict = requests.get(url=horoscope_url + user_sign).json()
    horoscope = horoscope_dict["horoscope"]
    print("Your horoscope is", horoscope)
except:
    print("Please double check your star sign")

# print("--Don't do the next part!----")
# the_date = pd.to_datetime(horoscope_dict["date"])
# the_date = horoscope_dict["date"]
# print the horoscope
# print(f"Your horoscope for {the_date.strftime('%A')} is: {horoscope}")
# print(f"Your horoscope for {the_date} is: {horoscope}")

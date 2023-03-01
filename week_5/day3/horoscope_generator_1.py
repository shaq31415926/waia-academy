while True:
# user enters their horoscope
    print("-"*50)
    user_sign = input("What is your star sign?:")
    user_sign  = user_sign.lower() # lowercase the input
    print("-"*50)

    # create a dict that contains stair signs and horoscopes
    horoscopes_dict = {"scorpio": "If this whole Mercury-retrograde business has left you longing for a little alone time, you may be grateful for Saturday’s cosmic news report! Serious Saturn shifts into reverse in Aquarius and your fourth house of domesticity, which can give you the wherewithal to RSVP “no thank you” to invitations that leave you underwhelmed. As the zodiac’s most private sign, you need to keep a little wall around your home and personal life, and a good way to accomplish that is by making Chateau Scorpio your safe and isolated sanctuary. But is it comfortable? Does your physical space accommodate your homey needs? With Saturn in reverse, you may be RE-considering a whole list of things you want to RE-do, like rearrange furniture, change some room layouts or maybe just don the painter’s coveralls and start rolling! But there’s no winging it with Saturn in the director’s chair. You need a well-thought-out game plan, and the good news is, you’ve got five months to create it. The clock starts…now!",
                       "pisces": "....",
                       "taurus": "...",
                       "libra": ".....",
                       "aries": "....",
                       "sagitarius": "..",
                       "capricorn": "....",
                       "virgo": "...",
                       "leo": ".....",
                       "cancer": "....",
                       "gemini": "..",
                       "aquarius": ".."
                    }

    # if hororscope is not a registered horoscope then error
    known_sign = list(horoscopes_dict.keys())

    if user_sign in known_sign:
        print(horoscopes_dict[user_sign])
        break # we no longer loop through the code if the sign is found
    else:
        print("We do not recognise your horoscope. Please check the spellings")
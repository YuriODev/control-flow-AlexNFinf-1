# Your solution to Exercise 18
remember_name = input("Do you remember their name?")
if remember_name == "yes":
    ex = input("Is it an ex? ")
    if ex == "yes":
        drunk = input("Are you drunk? ")
        if drunk == "yes":
            rekindle = input("Do you want to rekindle with them? ")
            if rekindle == "yes":
                print("Say hi.")
            elif rekindle == "no":
                print("Don't say hi.")
        elif drunk == "no":
            rihanna = input("Are you ina  convertible with Brad Pitt and / or Rihanna?")
            if rihanna == "yes":
                print("Say hi.")
            elif rihanna == "no":
                print("Don't say hi.")
            
    elif ex == "no":
        friend_ex = input("Is it a friend's ex? ")
        if friend_ex == "yes":
            print("Don't say hi.")
        elif friend_ex == "no":
            print("Say hi.")
            enemy = input("An enemy or frenemy? ")
            if enemy == "yes":
                convertible = input("Are you in a convertible with Brad Pitt and / or Rihanna? ")
                if convertible == "yes":
                    print("Say hi.")
                elif convertible == "no":
                    print("Don't say hi.")
            elif enemy == "no":
                bank = input("Are you robbing a bank? ")
                if bank == "yes":
                    print("Don't say hi.")
                elif bank == "no":
                    bathrobe = input("Are you in a bathrobe? ")
                    if bathrobe == "yes":
                        print("Don't say hi.")
                    elif bathrobe == "no":
                        print("Say hi.")
                # if drunk == "yes":
                # if rihanna == "yes":
                #     print("Say hi.")
                # elif rihanna == "no":
                #     bank = input("Are you robbing a bank? ")
                #     if bank == "yes":
                #         print("Don't Say hi.")
                #     elif bank == "no":
                #         bathrobe = input("Are you in a bathrobe? ")
                #         if bathrobe == "yes":
                #             print("Don't Say hi.")
                #         elif bathrobe == "no":
                #             print("Say hi.")
        # if drunk == "yes":
        #     rekindle = input("Do you want to rekindle with them? ")
        #     if rekindle == "yes":
        #         print("Say hi.")
        #     elif rekindle == "no":
        #         print("Don't Say hi.")





# SORTED


elif remember_name == "no":
    flee = input("Is there time to flee? ")
    if flee == "yes":
        print("Run for it.")
    elif flee == "no":
        call = input("Could you pretend to get a call on your cell? ")
        if call == "yes":
            print("Hello, doctor. What are my test results?")
        elif call == "no":
            sunglasses = input("Are you wearing sunglasses? ")
            if sunglasses == "yes":
                print("Keep walking")
            elif sunglasses == "no":
                print("Address the person using an amusing nickname such as 'Sarge,' 'Slugger' or 'Master Blaster'")

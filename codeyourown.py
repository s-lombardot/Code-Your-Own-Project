
import pickle

from os import path


def save (object, file):

    """Serialize a dictionary to a file."""

    with open(file, "wb") as f:

        pickle.dump(object, f)


def load(file):

    """Load a dictionary from a serialized file.

     Or return None if the file doesn't exist."""

    if path.exists(file):

        with open(file, "rb") as f:

            return pickle.load(f)

    return None

print()


print()


USERS_FILE = "scores.pkl"

big_date = load(USERS_FILE)

if big_date is None:
    big_date = {}
else:
    print ("Welcome back. Here's the previosly saved data")
    print (big_date)

print()


date = {}
print("Welcome to the Senior Project Organization Tool, or SPOT.")
info = "yes"
info = input("\nDo you know how this works? ")
info = info.lower()

    
while info != "yes" : 

    if info == "no":
        print("\nDon't worry! It's super simple. This program will help to organize all of your senior project events. You will be asked what category your event falls in, as well as how long it took you, you'll be asked to provide a BRIEF description, and finally the date that you did it. All your previous answers will be saved so dont worry!")
        input("Are you ready now?")
        print("Either way it doesn't matter because here we go.\n")
        info = ("yes")
        
    elif info == "goat":
        print ("\nNice try marc, trust me, we put goat into every single thing possible. now just be normal")
        info = input("\nNow, do you know how this works? ")
        info = info.lower()
    else: 
        info = input("invalid input, please try yes, no, or goat")
        
if info == "yes": 

        print("Great! So, what was category would this event fall under? planning, research, activity, presentation \n\n(WARNING, you can technically put this under any category, such as goat for example, and it will not explode. But it will also make your organization a lot messier so just use one of the examples please and thank you)")
    
    
category = input ("Category: ")

date["Category"] = category


print ()

print ("Next give a very short description of the activity")
descrip = input ("Description: ")

date["Description"] = descrip


print ("Great, and how many hours did it take you?")
hours = input ("Hours: ")
date["Hours"] = hours
print()

print("Finally, simply input the date the event took place. Please input the date in a mm/dd/yy format, for example: 06/12/23")
day = input("Date: ") 
big_date[day] = date


print (big_date)
save (big_date, USERS_FILE)
    

import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def dictionary(w):
    w = w.lower()           #checks for random input caps
    if w in data:
        return (data[w])
    elif w.title() in data:     #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:     #checks for acronyms like USA
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:            #finds closest match if exists
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":                                           #process user input
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."    
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

print("     English Dictionary")

def lookitup():                 #moded code into new function
    word = input("Enter your word: ")
    output = dictionary(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

while True:                 #recursive section
    lookitup()
    a = input('Do you want to find information about another word?(Press Y to continue)')
    if a.upper() != 'Y':
        break
 
print("Dictionary is closed.")
        






import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title in data:
        return data[word.title()]
    elif word.upper in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())):
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: "  % get_close_matches(word, data.keys())[0])
        if yn == c("Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The word does not exist, please double check"
        else:
            return "We did not understand your input" 

    else:
        return "The word does not exist, please double check"


word = input("Enter word: ")
output = (translate(word))
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)


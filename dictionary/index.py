import json
from difflib import get_close_matches
data = json.load(open('data.json', 'r'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input('Did you mean %s instead? Y/N' %
                   get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "word not found, please double check it."
        else:
            return "we didn't understand your entry."

    else:
        return "word not found, please double check it."


word = input('Enter word: ')

output = translate(word)

if type(output) == list:
    for item in output:
        print(' - '+item)
else:
    print(output)

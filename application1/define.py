import sys,json
from difflib import get_close_matches

with open("data.json") as f:
    data = json.load(f) # load json files

if len(sys.argv) >= 2:
    word = ' '.join(sys.argv[1:])
else:
    word = input('Give the word to define \n')

def define(word):

    word = word
    word2 = get_close_matches(word,data.keys(),cutoff=0.8)

    if word in data:
        a = ''
        for definition in range(len(data[word])):
            a += data[word][definition] + '\n'
        return a
    if word in data:
        a = ''
        for definition in range(len(data[word])):
            a += data[word][definition] + '\n'
        return a
    elif len(word2) != 0:
        a = input('Did you mean {}?\n'.format(word2[0]))

        if a.lower()[0] == 'y':
            return data[word2[0]]

        elif a.lower()[0] != 'y' and len(word2) > 1:
            b = input('Did you mean {}?\n'.format(word2[1]))

            if b.lower()[0] == 'y':
                return data[word2[1]]
            else:
                return "The word doesn't exist"

    else:
        return "The word doesn't exist"

print(define(word))

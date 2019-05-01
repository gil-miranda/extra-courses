import json
from difflib import get_close_matches

data = json.load(open('data/data.json'))

def closest_match(s):
    print('Did you mean %s instead?' % s)
    ans = input('y: yes or n: no \n')
    if ans.lower() == 'y':
        return data[s]
    else:
        return 'The word doesn\'t exist, please double check it.'

def translate(w):
    if not w.istitle() and not w.isupper():
        w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return closest_match(get_close_matches(w, data.keys())[0])
    else:
        return 'The word doesn\'t exist, please double check it.'

word = input('Enter word: ')
output = translate(word)

if type(output) == list:
    for (i,j) in zip(output,range(1,len(output)+1)):
        print('%d. %s' %(j,i))
else:
    print(output)

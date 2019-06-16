from difflib import SequenceMatcher, get_close_matches
import re

def words(text):
    return re.findall(r'\w+', text.lower())

wordSet = set(words(open('big.txt').read()))
print(wordSet)
# newList = []
# for word in wordList:
#     if len(word)>1:
#         newList.append(word)
print('Type "exit" to end the Spell Checker.')
while(True):
    str1 = input('Enter a Word:')
    correction = get_close_matches(str1, wordSet, n=2,cutoff=0.5)
    if str1=='exit' or str1=='Exit':
        break
    elif correction[0] == str1:
        print('Your word is correct!')
    else:
        print('Did you mean: {}?'.format(correction))
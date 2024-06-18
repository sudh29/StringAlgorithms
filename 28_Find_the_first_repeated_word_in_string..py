from collections import Counter 
 
def firstRepeat(input): 
    words = input.split(' ')
    dict = Counter(words)
    for key in words: 
        if dict[key]>1: 
            print(key) 
            return
    print(key) 
    return

input = 'Ravi had been saying that he had been there'
firstRepeat(input) 

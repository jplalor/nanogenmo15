
#markov chain to generate new Sherlock Holmes text for NaNoGenMo15
#John Lalor

import random, os

corpus_path = os.environ['CORPUSFILE']
infile = open(corpus_path,'r')

corpus = [x.split() for x in infile.read().replace('\r\n',' ').split('SPLITSPLIT')]

char_dict = {}
count = 0

for work in corpus:
    for i in range(len(work)-1):
        c = work[i]
        next_char = work[i+1]
        if c not in char_dict:
            char_dict[c] = {'count':0}
        if next_char not in char_dict[c]:
            char_dict[c][next_char] = 1
        else:
            char_dict[c][next_char] += 1
        char_dict[c]['count'] += 1

current_char = '*'

while current_char != '#':
    print current_char,
    d = char_dict[current_char]
    
    #build an array of possible characters so I can pick one randomly
    pointer = 0
    vals = []
    for k in d:
        if k == 'count':
            continue
        numchars = d[k]
        vals += [k]*numchars
    current_char = random.choice(vals)



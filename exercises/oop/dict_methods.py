from string import ascii_lowercase
double_alphabet = {}

for c in ascii_lowercase:
    double_alphabet[c] = c*2
    
print(double_alphabet)

test = {'first': 1, 'second':2, 'third':3}

print(test.pop('third'))
test['third'] = 3
print(test.get('third'))
test['third'] = 3

import math

x = 81
e = 1/(1 + math.exp(-x))
print(round(e,2))

c = 7*math.sin(math.radians(105))/math.sin(math.radians(35))
print(round(c,1)) 
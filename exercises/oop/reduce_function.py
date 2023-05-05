# reduces iterable to a single cumulative value

import functools

letters = ["h","e","l","l","o"]
# ["he","l","l","o"]
# ["hel","l","o"]
# ["hell","o"]
# ["hello"]
word = functools.reduce(lambda x, y: x + y,letters)

print(word)

factorial = [5,4,3,2,1]
# [20,3,2,1]
# [60,2,1]
# [120,1]
# [120]
result = functools.reduce(lambda x, y: x * y, factorial)

print(result)
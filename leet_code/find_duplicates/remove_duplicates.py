#!/usr/bin/env python3

list_with_duplicates = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

uniq_hash = {}
dups = []
for char in list_with_duplicates:
    if char not in uniq_hash:
        uniq_hash[char] = 1
    else:
        dups.append(char)
        
print(list(uniq_hash.keys()))
    
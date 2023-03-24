#!/usr/bin/env python3

list_with_duplicates = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

uniq = {}
duplicates = []
for c in list_with_duplicates:
    if c not in uniq:
        uniq[c] = 1
    else:
        duplicates.append(c)
        
print(f"Duplicates are {duplicates}")
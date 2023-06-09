#!/usr/bin/env python3
alist = [1, 5, 9, 10, 13]
blist = [0, 1, 3, 4, 7, 10, 11, 13, 15]

merged_list = []

a = 0  # index for alist
b = 0  # index for blist
while a <= len(alist) - 1 and b <= len(blist) - 1:
    print(f"index a: {a}, index b: {b}")

    if alist[a] < blist[b]:
        merged_list.append(alist[a])
        a += 1
    elif alist[a] > blist[b]:
        merged_list.append(blist[b])
        b += 1
    else:                      
        # values at indices a and b are equal
        merged_list.append(alist[a])
        merged_list.append(blist[b])
        a += 1
        b += 1
    print(f"interim merged_list: {merged_list}")

print(
    f"v1 index a: {a}, index b: {b}, len of alist: {len(alist)}, len of blist: {len(blist)}")
if a <= len(alist) - 1:
    # print(f"{alist[a:]}")
    merged_list.extend(alist[a:])
elif b <= len(blist) - 1:
    # print(f"{blist[b:]}")
    merged_list.extend(blist[b:])

print(f"final merged list: {merged_list}")

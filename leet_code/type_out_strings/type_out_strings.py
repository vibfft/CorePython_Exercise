
def type_out_strings(alist: str, blist: str) -> bool:

    a = 0
    b = 0
    new_alist = []
    new_blist = []
    while a <= len(alist) - 1 and b <= len(blist) - 1:

        print(f"list a: {new_alist} index: {a}")
        print(f"list b: {new_blist} index: {b}")
        if alist[a] != '#':
            new_alist.append(alist[a])
            a += 1
        elif alist[a] == '#':
            new_alist.pop()
            a += 1

        if blist[b] != '#':
            new_blist.append(blist[b])
            b += 1
        elif blist[b] == '#':
            new_blist.pop()
            b += 1

    final_a_str = ""
    final_b_str = ""
    for i in new_alist:
        final_a_str += i
    for j in new_blist:
        final_b_str += j

    if final_a_str == final_b_str:
        return True
    else:
        return False

def main():

    print(type_out_strings("abc#c", "az#c"))
    print(type_out_strings("ab#c", "az#c"))

if __name__ == '__main__':
    main()

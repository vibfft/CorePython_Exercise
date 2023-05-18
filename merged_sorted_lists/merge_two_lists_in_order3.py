class MergeLists(object):

    def merge_sorted_lists(alist: list, blist: list) -> list:

        a = 0
        b = 0
        al = len(alist) - 1
        bl = len(blist) - 1
        merged_list = []

        # if one of the lists break out, if one list is done
        while b <= bl and a <= al:
            print(f"v3 after while: a => {a}, {al} b => {b}")
            if alist[a] < blist[b]:
                merged_list.append(alist[a])
                a += 1
            
            elif alist[a] > blist[b]:
                merged_list.append(blist[b])
                b += 1

            else:
                merged_list.append(alist[a])
                a += 1
                b += 1
            print(f"Inside while loop: a {a}, b {b}")

        print(f"out of while loop: a {a}, b {b}")
        print(f"out of while loop: merged_list {merged_list}")
        if a <= len(alist) - 1:
            merged_list.extend(alist[a:])
        elif b <= len(blist) - 1:
            merged_list.extend(blist[b:])

        return merged_list

def main() -> None:
        
    alist = [1, 5, 9, 10, 13]
    blist = [0, 1, 3, 4, 7, 10, 11, 13, 15]
    
    print(f"Merged List: {MergeLists.merge_sorted_lists(alist, blist)}")

if __name__ == '__main__':
    main()


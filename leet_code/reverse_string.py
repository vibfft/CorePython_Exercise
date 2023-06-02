def reverse_string(s: list) -> None:
    p1 = 0
    p2 = len(s) - 1
    
    print(s)
    while p1 < p2:
        tmp = s[p1]
        s[p1] = s[p2]
        s[p2] = tmp
        p1 += 1
        p2 -= 1
    
    print(s)
    
def main() -> None:
    
    reverse_string(['h','e','l','l','o'])
    
if __name__ == '__main__':
    main()
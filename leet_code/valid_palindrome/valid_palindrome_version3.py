def is_palindrome(s: str) -> bool:
    
    c_str = ""
    for c in s:
        if c.isalpha():
            c_str += c.lower()
    
    print(f" cleaned_str: {c_str}")
    p1 = 0
    p2 = len(c_str) - 1
    
    while p1 < p2:
        if c_str[p1] == c_str[p2]:
            p1 += 1
            p2 -= 1
        else:
            return False
    return True        
    

def main() -> None:
    
    s_a = "A man, a plan, a canal: panama"
    s_b = "aba"
    s_c = "abacaba"
    s_d = "ccc"
    s_e = "cccdcc"
    s_f = "0P"
    
    for s in [s_a, s_b, s_c, s_d, s_e, s_f]:
        print(is_palindrome(s))
    
if __name__ == '__main__':
    main()
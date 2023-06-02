def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    elif len(s) == 1 and len(t) == 1 and s[0] == t[0]:
        return True
    
    s_hash = {}
    t_hash = {}
    
    for c in s:
        if c not in s_hash:
            s_hash[c] = 1
        else:
            s_hash[c] += 1
            
    for c in t:
         if c not in t_hash:
            t_hash[c] = 1
         else:
            t_hash[c] += 1
     
    return s_hash == t_hash           

def main() -> None:
    
    s = "anagram"
    t = "nagaram"
    print(is_anagram(s, t))
    
    s1 = "rat"
    t1 = "car"
    print(is_anagram(s1, t1))
    
if __name__ == '__main__':
    main()
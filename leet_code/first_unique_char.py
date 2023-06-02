def first_unique_char(s: str) -> int:
    
    uniq_hash = {}
    
    for i, c in enumerate(s):
        if c not in uniq_hash:
            uniq_hash[c] = []
            uniq_hash[c].append(i)
        else:
            uniq_hash[c].append(i)
    
    print(f"hash: {uniq_hash}")
    
    uniq_arry = []
    for k, v in uniq_hash.items():
        if len(v) == 1:
            uniq_arry.append(v[0])
            
    print(uniq_arry)
    if not len(uniq_arry):
        return -1
    return uniq_arry[0]
    
def main() -> None:
    
    s_a = "leetcode"
    s_b = "loveleetcode"
    s_c = "aabb"
    
    for s in [s_a, s_b, s_c]:
        print(first_unique_char(s))
    
if __name__ == '__main__':
    main()
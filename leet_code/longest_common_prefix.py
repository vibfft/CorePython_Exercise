def longest_common_prefix(strs: list) -> str:
    size = len(strs)
    if size == 0:
        return ""
    if size == 1:
        return strs[0]
    
    strs.sort()
    
    end = min(len(strs[0]), len(strs[size - 1]))
    
    i = 0
    while (i < end and strs[0][i] == strs[size - 1][i]):
        i += 1
    common = strs[0][0:i]
    
    return common

def main() -> None:
    
    strs_one = ["flower", "flow", "flight"]
    strs_two = ["dog", "racecar", "car"]
    
    for s in [strs_one, strs_two]:
        print(longest_common_prefix(s))
        
if __name__ == '__main__':
    main()
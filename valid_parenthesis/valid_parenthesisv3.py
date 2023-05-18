#!/usr/bin/env python3

# ""     True
# {([])} True
# {([]   False
# {[(])} False
# {[]()} True
def valid_parenthesis(paren_str: str) -> bool:

    left = 0
    right = len(paren_str) - 1
    
    open_paren = ['{', '(', '[']
    close_paren = ['}', ')', ']']
    all_paren = {'}':'{', ']':'[', ')':'('}
    
    s = []
    
    if not paren_str:
        return True
    elif paren_str[0] in close_paren:
        return False
    elif paren_str[-1] in open_paren:
        return False
    
    while left <= right:
        if paren_str[left] in open_paren:
            s.append(paren_str[left])
            left += 1
        else:
            if all_paren[paren_str[left]] in s:
                s.pop()
                left += 1
            else:
                return False
        #print(f"left {left}")
    if not len(s):
        return True
    return False    
            
def main() -> None:
    brackets = ["", "{([])}", "{([]", "{[(])}", "{[]()}"]

    for each_b in brackets:
        print(f"{each_b}: {valid_parenthesis(each_b)}")

if __name__ == '__main__':
    main()

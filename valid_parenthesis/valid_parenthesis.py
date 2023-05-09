#!/usr/bin/env python3

# ""     True
# {([])} True
# {([]   False
# {[(])} False
# {[]()} True
def valid_parenthesis(paren_str: str) -> bool:

    lst = list()
    paren_dict = {'}':'{', ')': '(', ']': '['}
    close_paren = paren_dict.keys()
    open_paren = paren_dict.values()

    print(f"paren: {close_paren}")
    if not paren_str:                  # empty string is True
        return True
    elif paren_str[0] in close_paren:  # starts with close paren e.g. }
        return False
    elif paren_str[-1] in open_paren:  # ends with open paren e.g. {
        return False
    
    for each_b in paren_str:
        if each_b in open_paren:
            lst.append(each_b)
        elif each_b in close_paren:
            if lst.pop() == paren_dict[each_b]:  # do open parens match?
                continue
            else:
                return False
    if not len(lst):  # {([]   False
        return True
    
    return False
    
            
def main() -> None:
    brackets = ["", "{([])}", "{([]", "{[(])}", "{[]()}"]

    for each_b in brackets:
        print(f"{each_b}: {valid_parenthesis(each_b)}")

if __name__ == '__main__':
    main()

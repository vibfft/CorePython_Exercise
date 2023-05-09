class ValidParenthesis(object):

    def valid_parenthesis(paren_str: str) -> bool:

        paren_stack = []
        open_paren  = ['(', '[', '{']
        close_paren = [')', ']', '}']
        paren_dict = {')':'(', ']':'[', '}':'{'}
        if not len(paren_str):
            return True
        elif paren_str[0] in close_paren:
            return False
        else:

            for each_paren in paren_str:
                # print(f"inside paren_stack: {paren_stack}")
                if each_paren in open_paren:
                    paren_stack.append(each_paren)
                elif each_paren in close_paren and paren_dict[each_paren] in paren_stack:
                    paren_stack.pop()
                else:
                    # print(f"before return paren_stack: {paren_stack}")
                    return False
        # print(f"paren_stack: {paren_stack}")
        if not len(paren_stack):
            return True
        return False

def main() -> None:

    for paren_str in ['', '}', '{}', '{{}', '{{{]}}}', '[[[[{{{()()[]()}}}]]]]', '[[[()[()])]]]']:
        print(f"Valid Paren: {ValidParenthesis.valid_parenthesis(paren_str)}")

if __name__ == '__main__':
    main()
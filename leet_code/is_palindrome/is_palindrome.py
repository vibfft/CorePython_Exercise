class IsPalindrome(object):

    def is_palindrome_iter(pal_str: str) -> bool:

        left = 0 # pointer 1
        right = len(pal_str) - 1 # pointer 2

        while left <= right:

            if pal_str[left] == pal_str[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True
def is_palindrome_rec(pal_str: str) -> bool:
         
        if not len(pal_str):
            return True
        elif len(pal_str) == 1:
            return True
        elif pal_str[0] == pal_str[-1]:
            return is_palindrome_rec(pal_str[1:-1])
        else:
             return False
    
def main() -> None:

    for pal_str in ['', 'a', 'aba', 'abba', 'abbbaa', 'abbbbbbbba', 'carac']:
        print(f"Is Palindrome: {is_palindrome_rec(pal_str)}")

if __name__ == '__main__':
        main()
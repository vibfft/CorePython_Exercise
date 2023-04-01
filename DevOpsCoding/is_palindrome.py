def is_palindrome(input_str: str) -> bool:

    if len(input_str) == 0 or len(input_str) == 1:
        return True

    else:
        if input_str[0] == input_str[-1]:
            return is_palindrome(input_str[1:-1])
        else:
            return False

print(is_palindrome('aabbaaa'))
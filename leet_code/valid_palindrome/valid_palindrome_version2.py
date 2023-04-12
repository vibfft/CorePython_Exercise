def valid_palindrome(input_string: str) -> bool:
    
    left = 0
    right = len(input_string) - 1
    
    while left < right:
        if input_string[left] == input_string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def main() -> None:
    
    for i, each_input in enumerate(['aba', 'abba', '', ' ', 'a', 'aabbaa', 'ababc', 'racecar','raceacar']):
        print(f"{i}: {each_input}")
        if valid_palindrome(each_input):
            print("is palindrome")
        else:
            print("not a palindrome")
if __name__ == '__main__':
    main()
            
    
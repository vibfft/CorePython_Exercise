def valid_palindrome( word_string: str) -> bool:
    
    accum = ""
    for each_char in word_string:
        if each_char.isalpha():
            accum += each_char.lower()
    # print(accum)
    
    beg = 0
    end = len(accum) - 1
    while True:
        if len(accum) == 0 or len(accum) == 1:
            print("is a palindrome")
            return True
        
        if accum[beg] == accum[end]:
            beg += 1
            end -= 1
            
            if len(accum) % 2 == 0:
                print(f"even length => b: {beg}, {accum[beg]}, e: {end}, {accum[end]}")
                if (beg - end) == 1:
                    print("is palindrome")
                    return True
                
            elif len(accum) % 2 == 1:
                print(f"odd length => b: {beg}, {accum[beg]}, e: {end}, {accum[end]}")
                
                if beg == end:
                    print("is palindrome")
                    return True
        else:
            print(f"left: {accum[beg]}, right: {accum[end]}")
            break
    
    print("not a palindrome")     
    return False

def main() -> None:
    
    string_input = "A man, a plan, a canal: panama"
    # string_input = "aba"
    # string_input = "abacaba"
    # string_input = "ccc"
    valid_palindrome(string_input)
    
if __name__ == '__main__':
    main()
    
    
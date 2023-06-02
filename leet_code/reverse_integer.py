def reverse_integer(x: int) -> int:
    
    neg = False
    if x < 0:
        x = abs(x)
        neg = True
        
    r_digit = ""
    while x > 0:
        digit = x // 10
        last_digit = x % 10 
        r_digit += str(last_digit)
        x = digit
        
    if neg:
        r_digit = -1*int(r_digit)
    else:
        r_digit = int(r_digit)
        
    return r_digit

def main() -> None:
    
    a = 123
    b = -123
    c = 120
    
    for n in [a, b, c]:
        print(reverse_integer(n))
    
if __name__ == '__main__':
    main()
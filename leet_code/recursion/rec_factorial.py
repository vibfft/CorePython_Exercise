def rec_factorial(number: int) -> int:
    
    if number <= 1:
        return 1
    else:
        return number * rec_factorial(number - 1)
    
    
def main() -> None:
    
    print(f"fact(5): {rec_factorial(5)}")
    
if __name__ == '__main__':
    main()
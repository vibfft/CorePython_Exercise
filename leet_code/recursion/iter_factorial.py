import timeit

TEST_CODE = '''
def iter_factorial(num: int) -> int:
    
    # n! = n * (n - 1)!
    if not num:
        return 1
    
    accum = 1
    while num >= 1:
        accum *= num
        num = num - 1
        
    return accum
'''

def main() -> None:
    # print(f"fact(5): {iter_factorial(5)}")
    print(f"elapsed time: {timeit.repeat(stmt = TEST_CODE, repeat=10)}")
    
if __name__ == '__main__':
    main()
    
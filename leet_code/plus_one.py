def plus_one(digits: list) -> list:
    
    num_str = ""
    for num in digits:
        num_str += str(num)
    
    new_num = int(num_str) + 1
    new_list = []
    for c in str(new_num):
        new_list.append(int(c))
    return new_list

def main() -> None:
    arry_a = [1,2,3]
    arry_b = [4,3,2,1]
    arry_c = [9]
    
    for arry in [arry_a, arry_b, arry_c]:
        print(plus_one(arry))
    
if __name__ == '__main__':
    main()
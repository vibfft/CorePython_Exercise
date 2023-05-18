#!/usr/bin/env python3

class ArithmeticMean:
    
    def __init__(self, input_size: int, num_list: list) -> None:
        self.input_size = input_size
        self.num_list = num_list
        
    def calculate_mean(self):
        
        return sum(self.num_list)/float(self.input_size)
    
    
def main() -> None:
    
    input_size = input()
    num_list = []
    
    index = 0
    while index < int(input_size):
        num = input()
        num_list.append(int(num))
        index += 1
        
    m = ArithmeticMean(input_size.strip(), num_list)
    print(m.calculate_mean())
    
if __name__ == "__main__":
    main()
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
#
# Following are the fixed values of C and H:
#
# C is 50. H is 30.
#
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
#
# The output of the program should be:
#
# 18,22,24

import sys

def formula(number):
    c = 50
    h = 30
    return int((2*c*int(number)/h)**(0.5))

def main():
    
    input_str = input("Enter comma separated integers: ")
    
    print(input_str)
    input_lst = []
    [input_lst.append(s) for s in input_str.split(',')]
    print(input_lst)
    
    output = map(formula, input_lst)
    print(list(output))
    
if __name__ == "__main__":
    main()
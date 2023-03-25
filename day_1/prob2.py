# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# input: integer
# output: the factorial of the integer 0! = 1, 1! = 1, 2! = 2*1, 3! 3*2*1
def fact_rec(number):
    
    if number == 0 or number == 1:
        return 1
    else:
        return number*fact_rec(number-1)

def fact_iterative(number):
    
    fact = 1 # can't be less than 1 since product of a number and zero is zero
    while number >= 1:
        fact = fact * number
        number -= 1 # decrement
        
    return fact
    
print(fact_rec(8))
print(fact_iterative(8))
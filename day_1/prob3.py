# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8

# Then, the output should be:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# input: an integral number like 8
# output: a dictionary of the format, (i, i x i), i.e. (3, 3 x 3) or (3, 9)

def generate_dict_from_integer(number):
    
    integer_dict = {}
    for num in range(1,number + 1):
        integer_dict[num] = num*num
        
    return integer_dict

print(generate_dict_from_integer(8))
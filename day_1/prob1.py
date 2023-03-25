# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
# steps:
# 1. numbers divisible by 7: use modular division of 7 and see whether the remainder is zero
# 2. a multiple of 5: divide the number by 5 and see whether the remainder is not zero
# output: a comman-separated sequence on a signle line

def div_by_seven_not_multiple_five(number_range):
    modular_div = 7
    division = 5
    accumulator = ""
    for num in number_range:
        if (num % modular_div) == 0 and (num % division) != 0:
            accumulator += str(num) + ", "
    print(accumulator)

div_by_seven_not_multiple_five(range(2000,3201))

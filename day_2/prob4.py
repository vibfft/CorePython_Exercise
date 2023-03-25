# Write a program which accepts a sequence of comma-separated numbers from console and 
# generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:
#
# 34,67,55,33,12,98
# Then, the output should be:
#
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

lst_of_number = input("Enter a comma separated list of numbers: ")

my_lst = [s for s in lst_of_number.split(",")]
print(my_lst)
print(tuple(my_lst))

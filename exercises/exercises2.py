# is_magician = True
# is_expert = False

# if is_magician and is_expert:
#     print("you are a master magician")
# elif is_magician and not is_expert:
#     print("At least you are getting there")
# elif not is_magician:
#     print("You need magic powers")

# my_list = [1,2,3,4,5,6,7,8,9,10]

# sum = 0
# for num in my_list:
#     sum += num
# print(f"sum of {my_list} is {sum}")

# sum = 0

# # [0...9]
# for i, num in enumerate(list(range(10))):
#     sum += num
# print(f"sum of {list(range(10))} is {sum}")

# import string
# for i, c in enumerate(string.ascii_letters):
#     print(f"index: {i} => char: {c}")
    
picture = [
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,1,1,1,1],
    [0,0,1,0,0],
    [0,0,1,0,0]
]

fill = '*'
empty = ' '
for row in picture:
    for pt in row:
        if pt:
            print(fill, end="")
        else:
            print(empty, end="")
    print()
            

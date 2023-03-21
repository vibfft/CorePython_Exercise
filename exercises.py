
# num_list = []
# sum_squares = 0
# while True:

#     num = int(input())
#     num_list.append(num)

#     if sum(num_list) == 0:
#         for each_num in num_list:
#             sum_squares += each_num*each_num
#         print(sum_squares)
#         break

# name = "Charlotte Brontë"
# new_name = ""
# def normalize(name):
#   conv = {'é':'e', 'ë':'e', 'á':'a','å':'aa','œ':'oe','æ':'ae'}

#   for each_char in name:
#     if each_char in conv:
#       new_name = name.replace(each_char, conv[each_char])

#   return new_name

# print(normalize(name))

# d_input = input()

# d_input = "2020-04-30"

# year,month,day = d_input.split('-')
# print(f"{year}\n{month}\n{day}")

# import re

# text = input()

# text = "WWW.GOOGLE.COM uses 100-percent renewable energy sources and www.ecosia.com plants a tree for every 45 searches!"
# words = text.split()
# for word in words:
#     match = False
#     for prefix in ['https://', 'http://', 'www.']:
#         if word.lower().startswith(prefix):
#             match = True
#     if match:
#         print(word)

# dir(locals()['__builtins__'])
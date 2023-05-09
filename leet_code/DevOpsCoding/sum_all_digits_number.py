def sum_digits_rec(number):
    if number < 10:
        return number
    else:
        all_digits = number // 10
        last_digit = number % 10
        print(f"all: {all_digits}, last: {last_digit}")
        return sum_digits_rec(all_digits) + last_digit

def sum_digits_iter(number):

    sum = 0
    while number > 0:

        digits = number // 10
        last_digit = number % 10
        number = digits

        print(f"last digit: {last_digit}")
        sum += last_digit

    return sum
    
print(sum_digits_rec(1024))
print(sum_digits_iter(1024))

# all: 102, last: 4
# all: 10, last: 2
# all: 1, last: 0
# 7
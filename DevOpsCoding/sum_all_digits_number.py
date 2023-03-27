def sum_digits(number):
    if number < 10:
        return number
    else:
        all_digits = number // 10
        last_digit = number % 10
        print(f"all: {all_digits}, last: {last_digit}")
        return sum_digits(all_digits) + last_digit
    
print(sum_digits(1024))

# all: 102, last: 4
# all: 10, last: 2
# all: 1, last: 0
# 7
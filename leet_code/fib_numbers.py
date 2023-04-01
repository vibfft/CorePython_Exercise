

# iterable, any sequence including a string
# iterate, an act of going through the iterable
# generators are iterable, but not every iterable is not a generator
# list is not a generator, but range is generator

# def generator_function(num):
#     for i in range(num):
#         yield i
        

# g = generator_function(10)
# next(g)
# next(g)
# print(next(g))
import pdb

def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b
        
for num in fibonacci(10):
    print(num)
    
    
def fib_list(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
        
    return result

print(fib_list(10))

def fib_rec(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib_rec(number - 1) + fib_rec(number - 2)
        
        
print(fib_rec(10))

help(pdb)
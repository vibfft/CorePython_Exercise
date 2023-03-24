
# def my_decorator(func):
#     def wrap_func(greet):
#         func(greet)
#     return wrap_func

# @my_decorator
# def hello(greet):
#     print(greet)
    
# hello("hello!!!")

from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"It took {round((t2 - t1),2)} ms")
        return result
    return wrapper

@performance
def measure_loop_performance():
    for i in range(1000000):
        i*5
        
measure_loop_performance()


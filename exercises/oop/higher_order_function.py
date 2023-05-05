# accepts a function as an argument for a function

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("hello")
    print(text)
    
hello(loud)
hello(quiet)

def divisor(den):
    def dividend(num):
        return num / den
    return dividend

divide = divisor(2) # returns dividend function

print(divide(10))    
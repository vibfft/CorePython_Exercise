#Rule: params, *args, default parameters, **kwargs

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def oldest_cat(lst:list):
        oldest_cat = None
        for i, c in enumerate(lst):
            if i == 0:
                oldest_cat = c
                continue
            if c.age > oldest_cat.age:
                oldest_cat = c
                
        return oldest_cat
    
    def oldest_cat2(*args):
        print(type(args))
        print(type(*args))
        return max(args)
                
                
def main():
    a = Cat('Sue', 46)
    b = Cat('Crystal', 5)
    d = Cat('Helen', 78)
    
    c = Cat.oldest_cat([a,b,d])
    
    print(f"The oldest cat is {c.name} and she is {c.age}")
    
    e = Cat.oldest_cat2(a.age, b.age, d.age)
    print(f"Age: {e}")
    
if __name__ == '__main__':
    main()
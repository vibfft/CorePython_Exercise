class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
    def walk(self):
        return f'{self.name} is roaming around'

class Callie(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
    def walk(self):
        return f'{self.name} is walking on the fence'
    
class Pete(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
    def walk(self):
        return f'{self.name} is meandering the backyard'
    
def main():
    
    s = Simon("Simon", 6)
    c = Callie("Callie", 5)
    p = Pete("Pete", 5)
    
    my_cats = [s, c, p]
    
    pet = Pets(my_cats)
    
    pet.walk()

    
if __name__ == "__main__":
    main()
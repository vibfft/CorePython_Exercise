class Duck:
    def walk(self):
        print("This duck is walking")
        
    def talk(self):
        print("quack!")
        
class Chicken:
    def walk(self):
        print("This chicken walking")
        
    def talk(self):
        print("Cluck!")
        
class Person():
    
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")
        
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)

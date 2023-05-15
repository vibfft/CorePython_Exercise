import random

random.seed(3)

print(random.betavariate(alpha=0.9, beta=0.1))

random.seed(-94)
print(random.uniform(0,1))

random.seed(-6)
print(random.choice("Voldemort"))
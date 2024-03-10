from random import *

randomowe = []
for i in range(10):
    randomowe.append(random.randint(1, 100))
print(randomowe)
RandParz = [x for x in randomowe if x % 2 == 0]
print(RandParz)

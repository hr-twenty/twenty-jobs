from ga import GA
import random

arr = [[(-1 if random.randint(0, 1) == 0 else 1) for i in range(3)] for i in range(100)]
data = []
for row in arr :
  decision = -1 if random.randint(0, 1) == 0 else 1
  row[0] = decision
  data.append( (True if decision==1 else False, row) )

print(data)
######
best = GA(data).evolve(100)
print(best)

# from ga import Chromosome
# ch = Chromosome([[random.uniform(-1, 1) for j in range(3)] for i in range(10)])

# ch = Chromosome([0.3, 1, 0])

# print(ch.score(data))
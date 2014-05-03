from ga import GA
import random

arr = [[(-1 if random.randint(0, 1) == 0 else 1) for i in range(30)] for i in range(100)]
data = []
for row in arr :
  decision = -1 if random.randint(0, 1) == 0 else 1
  row[0] = decision
  data.append( (True if decision==1 else False, row) )

print(data)
######
host = GA(data=data, poolSize=10)
best = host.evolve(stableFactor=100, breedRate=0.3, mutateRate=0.2, mutationDegree=0.05, mutationComplexity=0.3)
print(best)
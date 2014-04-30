import random

class Chromosome
  def __init__(self, genes,  mutateRate, mutationDegree) :
    self.genes = genes
    self.mutateRate = mutateRate
    self.mutationDegree = mutationDegree

  def breedWidth (self, mate) :
    return Chromosome([self.genes[i] if random.randint(0, 1) else mate.genes[i] for i in self.genes], self.mutateRate, self.mutationDegree)

  def mutate () :
    for i in range(len(self.genes)) :
      if (random.random() < self.mutateRate) :
        self.genes[i] *= random.uniform(1-self.mutationDegree, 1+self.mutationDegree));
    
    return None

  def score (data) :
    success = 0
    for entry in data :


    return success/len(data)

class GA
  poolSize = 100
  breedRate = 1
  mutateRate = 0.1
  mutationDegree = 0.1

  def __init__(self, data) :
    self.data = data
    self.chromosomes = [Chromosome([random.random(-1, 1) for j in range(len(data[0][1]))], mutateRate, mutationDegree) for i in range(poolSize)]

  def evolve (stableFactor) :
    max = self.chromosomes[0]
    stableCycles = 0

    while stableCycles < stableFactor :
      self.cycle()
      if (self.chromosomes[0] == max) :
        stableCycles += 1
      else :
        max = self.chromosomes[0]
        stableCycles = 0

    return max

  def cycle (self) :
    self.breed()
    self.mutate()
    self.survive()

  def breed () :
    self.chromosomes += [self.breedRandom() for i in range(int(poolSize*breedRate))]

  def breedRandom (self) :
    f = self.chromosomes[random.ranint(0, poolSize)]
    m = self.chromosomes[random.ranint(0, poolSize)]
    return f.breedWith(m)

  def mutate (self) :
    for chromosome in self.chromosomes
      chromosome.mutate();

  def survive (self) :
    self.chromosomes = sorted(self.chromosomes, key=lambda chromosome: chromosome.score(self.data), reverse=True)
    self.chromosomes = self[:poolSize]

      


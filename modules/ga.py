import random

class Chromosome :
  def __init__(self, genes) :
    self.genes = genes

  def breedWith (self, mate) :
    return Chromosome([self.genes[i] if random.randint(0, 1) else mate.genes[i] for i in range(len(self.genes))])

  def mutate (self, complexity, degree) :
    for i in range(len(self.genes)) :
      if random.random() < complexity :
        self.genes[i] = min(1, max(-1, self.genes[i] * random.uniform(1-degree, 1+degree)))

  def score (self, data) :
    success = 0
    for entry in data :

      label, features = entry
      score = 0

      for i in range(len(features)) :
        score += features[i] * self.genes[i]

      success += 1 if (score >= 1) == label else 0

    return success/len(data)


###########
# data should be an array of tuples, (label, features)
#label is true/false, 
#features is array of features
###########

class GA :
  def __init__(self, data, poolSize, stableFactor=100) :
    self.poolSize = poolSize
    self.data = data
    self.stableFactor = stableFactor
    self.chromosomes = [Chromosome([random.uniform(-1, 1) for j in range(len(data[0][1]))]) for i in range(self.poolSize)]

  def evolve (self, breedRate, mutateRate, mutationDegree, mutationComplexity) :
    max = 0
    stableCycles = 0

    while stableCycles < self.stableFactor :
      self.cycle(breedRate, mutateRate, mutationDegree, mutationComplexity)
      score = self.chromosomes[0].score(self.data)
      if (score == max) :
        stableCycles += 1
      else :
        max = score
        stableCycles = 0

    return self.chromosomes[0].genes

  def cycle (self, breedRate, mutateRate, mutationDegree, mutationComplexity) :
    self.breed(breedRate)
    self.mutate(mutateRate, mutationDegree, mutationComplexity)
    self.survive()

  def breed (self, breedRate) :
    self.chromosomes += [self.breedRandom() for i in range(int(self.poolSize*breedRate))]

  def breedRandom (self) :
    f = self.chromosomes[random.randint(0, self.poolSize-1)]
    m = self.chromosomes[random.randint(0, self.poolSize-1)]
    return f.breedWith(m)

  def mutate (self, mutationRate, mutationDegree, mutationComplexity) :
    mutationResults = []
    for chromosome in self.chromosomes :
      if ( random.random() < mutationRate ) :
        chromosome.mutate(mutationComplexity, mutationDegree)

  def survive (self) :
    self.chromosomes = sorted(self.chromosomes, key=lambda chromosome: chromosome.score(self.data), reverse=True)
    self.chromosomes = self.chromosomes[:self.poolSize]
      


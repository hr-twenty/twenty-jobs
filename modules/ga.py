import random

def mutateGene (gene, degree) : 
  return min(1, max(-1, gene * random.uniform(1-degree, 1+degree)))

class Chromosome :
  def __init__(self, genes) :
    self.genes = genes

  def breedWith (self, mate) :
    return Chromosome([self.genes[i] if random.randint(0, 1) else mate.genes[i] for i in range(len(self.genes))])

  def mutate (self, complexity, degree) :
    return Chromosome([mutateGene(gene, degree) if random.random() < complexity else gene for gene in self.genes])

  def score (self, data) :
    success = 0
    for entry in data :

      label, features = entry
      score = 0

      for i in range(len(features)) :
        score += features[i] * self.genes[i]

      #print("score", self.genes, features, score)
      success += 1 if (score >= 1) == label else 0

    return success/len(data)


###########
# data should be an array of tuples, (label, features)
#label is true/false, 
#features is array of features
###########

class GA :
  poolSize = 100
  breedRate = 0.3
  mutateRate = 1
  mutationDegree = 1
  mutationComplexity = 0.5

  def __init__(self, data) :
    self.data = data
    self.chromosomes = [Chromosome([random.uniform(-1, 1) for j in range(len(data[0][1]))]) for i in range(self.poolSize)]

  def evolve (self, stableFactor) :
    max = self.chromosomes[0].genes
    stableCycles = 0

    while stableCycles < stableFactor :
      self.cycle()
      if (self.chromosomes[0].genes == max) :
        stableCycles += 1
      else :
        print("new")
        max = self.chromosomes[0].genes[:]
        stableCycles = 0
      print(stableCycles, max, self.chromosomes[0].score(self.data))

    return max

  def cycle (self) :
    self.breed()
    self.mutate()
    self.survive()

  def breed (self) :
    self.chromosomes += [self.breedRandom() for i in range(int(self.poolSize*self.breedRate))]

  def breedRandom (self) :
    f = self.chromosomes[random.randint(0, self.poolSize-1)]
    m = self.chromosomes[random.randint(0, self.poolSize-1)]
    return f.breedWith(m)

  def mutate (self) :
    mutationResults = []
    for chromosome in self.chromosomes :
      if ( random.random() < self.mutateRate ) :
        mutationResults.append(chromosome.mutate(self.mutationComplexity, self.mutationDegree));
    self.chromosomes += mutationResults

  def survive (self) :
    self.chromosomes = sorted(self.chromosomes, key=lambda chromosome: chromosome.score(self.data), reverse=True)
    self.chromosomes = self.chromosomes[:self.poolSize]
      


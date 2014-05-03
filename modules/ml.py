from sklearn.cluster import DBSCAN
from sklearn.linear_model import ElasticNet
import numpy
###########################################################
def cluster (data):
  init = DBSCAN(eps=0.3, min_samples=1)
  clusters = init.fit(numpy.array(data, numpy.float64))
  return list(map(lambda f: int(f), clusters.labels_))
###########################################################
def weighting (data):
  pool = GA(data=data, poolSize=10, stableFactor=100)
  return pool.evolve(breedRate=0.3, mutateRate=0.2, mutationDegree=0.05, mutationComplexity=0.3)
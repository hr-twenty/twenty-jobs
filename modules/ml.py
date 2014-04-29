from sklearn.cluster import DBSCAN
import numpy
###########################################################
def cluster (data):
  init = DBSCAN(eps=0.3, min_samples=1)
  clusters = init.fit(numpy.array(data, numpy.float64))
  return list(map(lambda f: int(f),clusters.labels_))
###########################################################

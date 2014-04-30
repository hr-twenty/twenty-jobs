from sklearn.cluster import DBSCAN
from sklearn.linear_model import ElasticNet
import numpy
###########################################################
def cluster (data):
  init = DBSCAN(eps=0.3, min_samples=1)
  clusters = init.fit(numpy.array(data, numpy.float64))
  return list(map(lambda f: int(f),clusters.labels_))
###########################################################
def weighting (data):
  init = ElasticNet(l1_ratio=0.5, fit_intercept=True, normalize=False, precompute='auto', copy_X=True, warm_start=False, positive=False)
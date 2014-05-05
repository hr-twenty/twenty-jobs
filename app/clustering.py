from modules import db
from modules import ml
###########################################################
def runClustering ():
  (users, features) = db.getFeatureArrays()
  
  labels = ml.cluster(features)

  clusters = db.createClusters(len(set(labels)))

  print('number of clusters: ', len(clusters))
  print('number of users: ', len(users))

  for i in range(len(users)) :
    db.assignCluster(users[i], clusters[labels[i]])

  return None
  
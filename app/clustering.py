from modules import db
from modules import ml
###########################################################
def runClustering ():
  (users, features) = db.getFeatureArrays()
  
  labels = ml.cluster(features)

  db.createClusters(len(labels))

  for i in range(len(users)) :
    db.assignCluster(users[i], labels[i])

  return None
  
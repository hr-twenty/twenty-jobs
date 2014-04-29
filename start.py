from app import clustering
from modules import db

clustering.runClustering()

query = """
  MATCH (user:User) --> (cluster:Cluster)
  RETURN user.userId, user.firstName, user.lastName, cluster.clusterIndex
"""
table = db.mapArray(db.cypherQuery(query))

print(table)
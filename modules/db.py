from py2neo import neo4j
import secret

db = neo4j.GraphDatabaseService(secret.neo4jcon())

def cypherQuery (query): 
  return neo4j.CypherQuery(db, query).execute()

###########################################################
def mapArray (result) : 
  return list(map(lambda row: list(row.values), list(result._data)))
def mapColumn (rows, col) :
  return list(map(lambda row: row[col], rows))
###########################################################
def getSkillList ():
  query = """
    MATCH (skill:Skill)
    RETURN skill.skill
  """
  return cypherQuery(query)

def getUserList ():
  query = """
    MATCH (user:User)
    RETURN user.userId
  """
  return cypherQuery(query)
###########################################################
def getFeatureArrays ():
  skills = mapColumn(mapArray(getSkillList()), 0)
  users = mapColumn(mapArray(getUserList()), 0)

  query = """
    MATCH (user:User)-->(skill:Skill)
    RETURN user.userId, skill.skill
  """
  rows = mapArray(cypherQuery(query))
  
  #transform
  features = [[0 for i in skills] for i in users];

  for row in rows :
    features[users.index(row[0])][skills.index(row[1])] = 1

  return (users, features)

###########################################################
def createClusters (num):
  query = """
    MATCH (c:Cluster)<-[r:BELONGS_TO]-()
    DELETE c, r
  """
  cypherQuery(query)

  for i in range(num):
    q = "MERGE (c:Cluster {{clusterIndex:{0}}}) RETURN c.clusterIndex".format(i)
    cypherQuery(q)

  return None

###########################################################
def assignCluster (userId, clusterIndex) :
  query = """
    MATCH (me:User {{userId:"{0}"}}), (cluster:Cluster {{clusterIndex: {1}}})
    CREATE (me)-[r:BELONGS_TO]->(cluster)
    RETURN me, r, cluster
  """
  query = query.format(userId, clusterIndex)
  
  cypherQuery(query)
  
  return None

###########################################################
def getHistory (userId) :
  skills = mapColumn(mapArray(getSkillList()), 0)

  query = """
    MATCH (me:User {{userId:"{0}"}})-->(:Stack)-[:APPROVES]->(other:User)
    RETURN other.userId
  """
  others = mapColumn(mapArray(cypherQuery(query.format(userId))), 0)

  query = """
    MATCH (me:User {{userId:"{0}"}})-->(:Stack)-[:APPROVES]->(other:User)-->(skill:Skill)
    RETURN other.userId, skill.skill
  """

  rows = mapArray(cypherQuery(query.format(userId)))
  
  #transform
  features = [[0 for i in skills] for i in others];

  for row in rows :
    features[others.index(row[0])][skills.index(row[1])] = 1

  return (others, features)


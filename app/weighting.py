from modules import db
from modules import ml

def calcUser (userId) : 
  (others, features) = db.getHistory(userId)
  

  #needs array of tuples
  weights = ml.weighting(features);

  return None

def calculate():
  users = db.getUserList()

  for user in users 
    calcUser(user)

  return None

def weight (userId) :
  query = """
    MATCH (user:User {{userId: "{userId}"}})-->(:Stack)-[r]->(other:User)
    WITH other, r
    MATCH (other)-[:HAS_SKILL]->(s:Skill)
    RETURN other, r, collect(skill)
  """.format(userId)

  results = db.mapArray(db.cypherQuery(query))
  print(results)


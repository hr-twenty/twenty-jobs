from modules import db

def printList() :
  query = """
    MATCH (user:User)-->(skill:Skill)
    RETURN user.userId, skill.skill
  """
  pairs = db.mapArray(db.cypherQuery(query))

  skillset = {}

  for pair in pairs :
    if pair[0] not in skillset :
      skillset.update({pair[0]: ''})
    skillset[pair[0]] = skillset[pair[0]] + ', ' + pair[1]

  query = """
    MATCH (user:User) --> (cluster:Cluster)
    RETURN DISTINCT user.userId, user.firstName, user.lastName, cluster.clusterIndex
    ORDER BY cluster.clusterIndex
  """
  table = db.mapArray(db.cypherQuery(query))

  for row in table :
    row.append(skillset[row[0]])
    print(row)

  return None
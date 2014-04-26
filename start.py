from py2neo import neo4j
import secret

db = neo4j.GraphDatabaseService(secret.neo4jcon())

query = ''

list = neo4j.CypherQuery(db, query).execute();

print [method for method in dir(list) if callable(list, method)]

print str(list[0][0])
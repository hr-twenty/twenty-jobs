from py2neo import neo4j
import secret

print secret.neo4jcon

db = neo4j.GraphDatabaseService(secret.neo4jcon())

print(secret.neo4jcon())

query = 'MATCH (a)-->(b) RETURN a, b'

list = neo4j.CypherQuery(db, query).execute()

print(str(list[0][0]))

print('end')

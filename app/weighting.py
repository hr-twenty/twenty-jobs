from modules import db
from modules import ml

def calcUser (userId) : 
  (others, features) = db.getHistory(userId)
  
  return None

def calculate():
  users = db.getUserList()

  for user in users 
    calcUser(user)

  return None
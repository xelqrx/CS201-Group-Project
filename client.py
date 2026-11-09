import random
import subprocess

class Client:
 def __init__(name, balance, is_riding=False, id_created=False):
    name.balance = balance
    name.is_riding = is_riding
    name.client_ID = create_id(name)
    name.id_created = id_created
  
 def create_id(name):
   if  name.id_created==True:
     return client_ID
   else:
    client_ID = random.randint(1000, 9999)
     name.id_created=True
     return client_ID
   
 def check_balance(balance)->bool :
  if name.balance <2:
    return False
  else:
    return True
   
 def assign_bike(name, bike_id):
   return name.client_ID
  
 def balance_change(balance, change):
   balance = name.balance
   balance = balance - change
   return balance

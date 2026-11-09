import random

class Client:
 def __init__(name, balance, is_riding=False, id_created=False):
    name.balance = balance
    name.is_riding = is_riding
    client_ID = create_id(name)
    name.id_created = id_created
  
 def create_id(name):
   if  name.id_created==True:
     return client_ID
   else:
    client_ID = random.randint(1000, 9999)
     return client_ID
   
 def check_balance(balance)->bool :
  #Якщо баланс менше нуля - return False
  pass
 def assign_bike(name, bike):
   #закріплює людину за велосивпоруклл
  pass
 def balance_change(balance, change):
  #відняти гроші
   pass

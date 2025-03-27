from DataStructures.Map import map_functions as mp
from DataStructures.Map import map_entry as me
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al


def new_map(num, factor, primo=109345121):
   mapa = {}
   mapa["prime"] = primo
   cantidad_buckets = max(1, int(num // factor)) 
   if (num % factor) > 0:
       cantidad_buckets += 1
  
   cantidad_buckets = mp.next_prime(cantidad_buckets)
  
   mapa["capacity"] = cantidad_buckets
   mapa["scale"] = 1
   mapa["shift"] = 0
   mapa["table"] = al.new_list()
   for i in range (cantidad_buckets):
       lista = sl.new_list()
       al.add_last(mapa["table"],lista)
      
   mapa["limit_factor"]= factor
   mapa ["size"] = 0
   mapa["current_factor"] = 0
   return mapa


def rehash(my_map):
   initial_capacity = int(my_map['capacity'])
   num = mp.next_prime(initial_capacity * 2) 
  
   factor = my_map["limit_factor"] 
  
   resized = new_map(num, factor)
   buckets = my_map['table']['elements']
  
   for bucket in buckets:
       print("Santiago es gay")
       for i in range(sl.size(bucket)):
           elm = sl.get_element(bucket, i)
           key = elm["key"]
           value = elm["value"]
           put(resized, key, value)
   
   return resized


def put(my_map, key, value):
   hash_llave = mp.hash_value(my_map,key)
   bucket = my_map["table"]["elements"][hash_llave]
   capacidad = my_map["capacity"]
   size = my_map["size"]
   valor = {"key":key,"value":value}
   repetido = contains(my_map,key)
   if repetido:
       for i in range(sl.size(bucket)):
           elm = sl.get_element(bucket,i)
           if elm["key"] == key:
               elm["value"] = value
   else:
       sl.add_last(bucket,valor)
       my_map["size"] += 1


   my_map["current_factor"] = round(size/capacidad,1)
   if my_map["current_factor"] > my_map["limit_factor"]:
       rehash(my_map)
   return my_map


def default_compare(key, element):


  if (key == me.get_key(element)):
     return 0
  elif (key > me.get_key(element)):
     return 1
  return -1


def contains(map, key):
   retorno = False
   pos = mp.hash_value(map,key)
   if pos <= map["capacity"]:
       bucket = map["table"]["elements"][pos]
       for i in range (sl.size(bucket)):
           elm = sl.get_element(bucket,i)
           if elm["key"] == key:
               retorno = True
   return retorno


def get(map, key):
   retorno = None
   if contains(map,key):
       pos = mp.hash_value(map,key)
       bucket = map["table"]["elements"][pos]
       for i in range(sl.size(bucket)):
           elm = sl.get_element(bucket,i)
           if elm["key"] == key:
               retorno = elm["value"]
   return retorno


def remove(map,key):
   if contains(map,key):
       pos = mp.hash_value(map,key)
       bucket = map["table"]["elements"][pos]
       for i in range(sl.size(bucket)):
           elm = sl.get_element(bucket,i)
           if elm["key"] == key:
               sl.delete_element(bucket,i)
               map["size"] -= 1
   return map


def size(map):
   return map["size"]


def is_empty(map):
   return map["size"] == 0


def key_set(map):
   buckets = map["table"]["elements"]
   keys = al.new_list()
   for i in range(map["capacity"]):
       bucket = buckets[i]
       for j in range(bucket["size"]):
           elm = sl.get_element(bucket,j)
           key = elm["key"]
           al.add_last(keys,key)


      
   return keys


def value_set(map):
   buckets = map["table"]["elements"]
   valores = al.new_list()
   for i in range(map["capacity"]):
       bucket = buckets[i]
       for j in range(bucket["size"]):
           elm = sl.get_element(bucket,j)
           value = elm["value"]
           al.add_last(valores,value)


   return valores






#no fino


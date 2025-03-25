from DataStructures.Map import map_functions as mp
from DataStructures.Map import map_entry as me
from DataStructures.List import single_linked_list as sl

def new_map(num, factor=4, primo=109345121):
    mapa = {}
    mapa["prime"] = primo
    cantidad_buckets = (num//factor) + (num%factor)
    mapa["capacity"] = cantidad_buckets
    mapa["scale"] = 1
    mapa["shift"] = 0
    mapa["table"] = {}
    mapa["table"]["size"] = num
    mapa["table"]["elements"] = [] 
    for i in range (cantidad_buckets+1):
        lista = sl.new_list()
        mapa["table"]["elements"].append(lista)
        
    mapa["limit_factor"]= factor
    mapa ["size"] = 0
    mapa["current_factor"] = 0
    return mapa

def rehash(my_map):
    capacity = int(my_map['capacity'])
    num = mp.next_prime(capacity*2)
    resized = new_map(num)
    buckets = my_map['table']['elements']
    for bucket in buckets:
        for i in range(sl.size(bucket)):
            elm = sl.get_element(bucket,i)
            key = elm["key"]
            value = elm["value"]

            put(resized,key,value)
        
    return resized

def put(my_map, key, value):
    hash_llave = mp.hash_value(my_map,key)
    bucket = my_map["table"]["elements"][hash_llave]
   
    valor = {"key":key,"value":value}
    sl.add_last(bucket,valor)
    my_map["size"] += 1
    my_map["current_factor"] = round(size/my_map["capacity"],1)
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
    bucket = map["table"]["elements"][key]
    if bucket["first"]["info"]["key"] == key:
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
    return map

def size(map):
    return map["size"]
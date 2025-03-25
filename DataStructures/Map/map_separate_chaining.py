import map_functions as mp
from DataStructures.List import single_linked_list as lists

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
        lista = lists.new_list()
        mapa["table"]["elements"].append(lista)
        
    mapa["limit_factor"]= factor
    mapa ["size"] = 0
    mapa["current_factor"] = 0
    return mapa

def rehash(my_map):
    capacity = int(my_map['capacity'])
    num = mp.next_prime(capacity*2)
    resized = new_map(num,factores=4,primo=109345121)
    elements = my_map['table']['elements']
    for element in elements:
        put(resized,llave,valor)
    return resized

def put(my_map, key, value):
    return 0

def contains(map, key):
    return 0

def get(map, key):
    return 0

def remove(map,key): 
    return 0

def size(map):
    return 0
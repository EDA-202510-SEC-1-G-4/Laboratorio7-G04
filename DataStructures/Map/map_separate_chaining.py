import map_functions as mp

def new_map(num, factores=0.5, primo=1093598347):
    mapa = {}
    mapa["prime"] = primo
    mapa["capacity"] = num
    mapa["scale"] = 1
    mapa["shift"] = 0
    mapa["table"] = {}
    mapa["table"]["size"] = num
    mapa["table"]["elements"] = []
    for i in range (num+1):
        mapa["table"]["elements"].append({"Key": None, "Value": None})
        
    mapa["limit_factor"]= factores
    mapa ["size"] = 0
    mapa["current_factor"] = 0
    return mapa

def rehash(my_map):
    return 0

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
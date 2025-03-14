import map_functions as mp

def new_map():
    return

def put():
    
    return

def contains(map, key):
    cont = False
    if map['table']['size'] > 0:
        for pair in map['table']['elements']:
            k = pair['key']
            if k == key:
                cont = True
    return cont

def get(map, key):
    res = None
    if contains(map,key):
        hash = mp.hash_value(map,key)
        if map['table']['elements'][hash]['key'] == key:
            res = map['table']['elements'][hash]['value'] 
        else:
            cent = True
            while cent: 
                res = map['table']['elements'][hash]['value']
                if map['table']['elements'][hash]['key'] == key:
                    cent = False
            hash += 1
    return res

def remove():
    return 

def size():
    return
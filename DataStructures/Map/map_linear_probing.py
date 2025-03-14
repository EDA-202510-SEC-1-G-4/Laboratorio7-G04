
def hash(map, key):
    return int(abs(hash(key) % map["capacity"]))

def rehash(map, old_hash):
    return (old_hash + 1) % map["capacity"]

def new_map(num, factores=0, primo=1093598347):
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


def put(self, my_map, key, value):
        hash_value = self._hash(key)
        found = False
        first_avail = None
        
        while not found:
            if my_map['table'][hash_value]['key'] is None or my_map['table'][hash_value]['key'] == "__EMPTY__":
                if first_avail is None:
                    first_avail = hash_value
                if my_map['table'][hash_value]['key'] is None:
                    found = True
            elif my_map['table'][hash_value]['key'] == key:
                my_map['table'][hash_value]['value'] = value
                return my_map
            
            hash_value = (hash_value + 1) % my_map['capacity']
        
        my_map['table'][first_avail] = {'key': key, 'value': value}
        my_map['size'] += 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']
        
        if my_map['current_factor'] >= my_map['limit_factor']:
            self._resize(my_map)
        
        return my_map

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

def remove(map,key): 
    for elm in map["table"]["elements"]:
        pos = mp.hash_value(map,elm["key"])
        if pos == key:
            elm["key"] = "__EMPTY__"
            elm["value"] = "__EMPTY__"
    return map

def size(map):
    return map["size"]
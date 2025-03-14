def new_map():
    return

def put():
    
    return

def contains():
    return

def get():
    return

def remove(map,key): 
    for elm in map["table"]["elements"]:
        pos = mp.hash_value(map,elm["key"])
        if pos == key:
            elm["key"] = "__EMPTY__"
            elm["value"] = "__EMPTY__"
    return map
                    
def size(map):
    return map["size"]


def new_map(num, factores=0.5, primo=109345121):
    mapa = {}
    mapa["prime"] = primo
    mapa["capacity"] = num
    mapa["scale"] = 1
    mapa["shift"] = 0
    mapa["table"] = new_list()
    for i in range (num+1):
        add_last(mapa["table"],{"Key": None, "Value": None})

    mapa["limit_factor"]= factores
    mapa ["size"] = 0
    mapa["current_factor"] = 0
    return mapa

def rehash(my_map):
    capacity = int(my_map['capacity'])
    num = next_prime(capacity*2)
    resized = new_map(num,factores=0.5,primo=1093598347)
    elements = my_map['table']['elements']
    for element in elements:
        llave = element['key']
        valor = element['value']
        put(resized,llave,valor)
    return resized

def put(my_map, key, value):
        hash_value = hash_value(my_map, key)
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
            my_map = rehash(my_map)

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
        hash = hash_value(map,key)
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
        pos = hash_value(map,elm["key"])
        if pos == key:
            elm["key"] = "__EMPTY__"
            elm["value"] = "__EMPTY__"
    return map

def size(map):
    return map["size"]



def rehash(my_map):
    capacity = int(my_map['capacity'])
    num = next_prime(capacity*2)
    factor = my_map["limit_factor"]
    resized = new_map(num,factor)
    buckets = my_map['table']['elements']
    for bucket in buckets:
        for i in range(size(bucket)):
            elm = get_element(bucket,i)
            key = elm["key"]
            value = elm["value"]

            put(resized,key,value)
        
    return resized

def put(my_map, key, value):
    hash_llave = hash_value(my_map,key)
    bucket = my_map["table"]["elements"][hash_llave]
    capacidad = my_map["capacity"]
    size = my_map["size"]
    valor = {"key":key,"value":value}
    add_last(bucket,valor)
    my_map["size"] += 1
    my_map["current_factor"] = round(size/capacidad,1)
    if my_map["current_factor"] > my_map["limit_factor"]:
        rehash(my_map)
    return my_map

"""
  Estructura que contiene la información a guardar en una ``entry`` de un Map
"""


def new_map_entry(key, value):
    """
    Crea una nueva entrada (de tipo :ref:`map_entry<map-entry>`) de una tabla con una llave y un valor dados.

    La entrada es creada con los siguientes atributos:

    * **key**: Llave de la entrada. Inicializada con el valor de la llave dada ``key``.
    * **value**: Valor de la entrada. Inicializada con el valor del valor dado ``value``.

    :param key: Llave de la entrada.
    :type key: any
    :param value: Valor de la entrada.
    :type value: any

    :return: Entrada de una tabla.
    :rtype: :ref:`map_entry<map-entry>`
    """
    entry = {"key": key, "value": value}
    return entry


def set_key(my_entry, key):
    """
    Establece un valor nuevo a la ``key`` de una entrada recibida.

    :param my_entry: Entrada a modificar.
    :type my_entry: :ref:`map_entry<map-entry>`
    :param key: Llave nueva de la entrada.
    :type key: any

    :return: Entrada con la llave modificada.
    :rtype: :ref:`map_entry<map-entry>`
    """
    my_entry["key"] = key
    return my_entry


def set_value(my_entry, value):
    """
    Establece un valor nuevo al ``value`` de una entrada recibida.

    :param my_entry: Entrada a modificar.
    :type my_entry: :ref:`map_entry<map-entry>`
    :param value: Valor nuevo de la entrada.
    :type value: any

    :return: Entrada con el valor modificado.
    :rtype: :ref:`map_entry<map-entry>`
    """
    my_entry["value"] = value
    return my_entry


def get_key(my_entry):
    """
    Obtiene la llave ``key`` de una entrada recibida.

    :param my_entry: Entrada de la cual se desea obtener la llave.
    :type my_entry: :ref:`map_entry<map-entry>`

    :return: Llave de la entrada.
    :rtype: any
    """
    return my_entry["key"]


def get_value(my_entry):
    """
    Obtiene el valor ``value`` de una entrada recibida.

    :param my_entry: Entrada de la cual se desea obtener el valor.
    :type my_entry: :ref:`map_entry<map-entry>`

    :return: Valor de la entrada.
    :rtype: any
    """
    return my_entry["value"]


def default_compare(key, element):

   if (key == get_key(element)):
      return 0
   elif (key > get_key(element)):
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
        pos = hash_value(map,key)
        bucket = map["table"]["elements"][pos]
        for i in range(size(bucket)):
            elm = get_element(bucket,i)
            if elm["key"] == key:
                retorno = elm["value"]
    return retorno

def remove(map,key): 
    if contains(map,key):
        pos = hash_value(map,key)
        bucket = map["table"]["elements"][pos]
        for i in range(size(bucket)):
            elm = get_element(bucket,i)
            if elm["key"] == key:
                delete_element(bucket,i)
    return map

def size(map):
    return map["size"]

def is_empty(map):
    return map["size"] == 0

def key_set(map):
    buckets = map["table"]["elements"]
    keys = new_list()
    for i in range(map["capacity"]):
        bucket = buckets[i]
        for j in range(bucket["size"]):
            elm = get_element(bucket,j)
            key = elm["key"]
            add_last(keys,key)

        
    return keys

def value_set(map):
    buckets = map["table"]["elements"]
    valores = new_list()
    for i in range(map["capacity"]):
        bucket = buckets[i]
        for j in range(bucket["size"]):
            elm = get_element(bucket,j)
            value = elm["value"]
            add_last(valores,value)

    return valores

import math

"""
    Funciones auxiliares para el manejo de tablas de simbolos (**mapas**)
"""


def is_prime(n):
    """Valida si un número es primo o no

    :param n: Número a validar
    :type n: int

    :return: True si es primo, False en caso contrario
    """
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def next_prime(n):
    """
    Encuentra el siguiente número primo mayor a n

    :param n: Número a partir del cual se busca el siguiente primo
    :type n: int

    :return: El siguiente número primo mayor a n
    """
    found = False
    next_p = 1
    # Base case
    if n <= 1:
        next_p = 2
        found = True
    if found is False:
        next_p = int(n)
        # Loop continuously until is_prime returns
        # True for a number greater than n
        while not found:
            next_p = next_p + 1
            if is_prime(next_p):
                found = True
    return int(next_p)


def hash_value(table, key):
    """
    Calcula un hash para una llave, utilizando el método
    MAD : hash_value(y) = ((a*y + b) % p) % M.

    Donde:
    M es el tamaño de la tabla, primo
    p es un primo mayor a M,
    a y b enteros aleatoreos dentro del intervalo [0,p-1], con a > 0

    :param table: Tabla de hash
    :type table: map
    :param key: Llave a la que se le calculará el hash
    :type key: any

    :return: Valor del hash
    :rtype int
    """

    h = hash(key)
    a = table["scale"]
    b = table["shift"]
    p = table["prime"]
    m = table["capacity"]

    value = int((abs(a * h + b) % p) % m)
    return value

def new_list():
    new_list = {
        'first': None,
        'last': None,
        'size': 0
    }
    return new_list

def default_sort_criteria (elm1,elm2):
    is_sorted = False
    if elm1 <= elm2:
      is_sorted = True
    return is_sorted

def get_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("get_element(): posición fuera de rango")
    
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"] 

def is_present (my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
        
    if not is_in_array:
            count = -1
    return count

def add_first (my_list, element):
    new_node = {
        'info': element,
        'next': my_list['first']
    }
    my_list['first'] = new_node
    if my_list['size'] == 0:
        my_list["last"] = new_node
        my_list["first"] = new_node
    my_list['size'] += 1
    return my_list

def add_last (my_list, element):
    new_node = {
        'info': element,
        'next': None
    }
    if my_list['size'] == 0:
        my_list['first'] = new_node
    else:
        my_list['last']['next'] = new_node
    my_list['last'] = new_node
    my_list['size'] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element (my_list):
    return my_list["first"]["info"]

def is_empty (my_list):
    return my_list["size"] == 0


def remove_first(my_list):

    if my_list["size"] > 0:
        removed = my_list["first"]["info"]
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -= 1
        if my_list["size"] == 0:
            my_list["last"] = None
            my_list["first"] = None
        return removed
    return None

def last_element(my_list):
    if my_list["size"] == 0:
        return None
    else:
        return my_list["last"]["info"]
    
def remove_last(my_list):
    if my_list["size"] == 0:
        return None
    elif my_list["size"] == 1:
        return remove_first(my_list)
    else:
        removed = my_list["last"]["info"]
        i = 0
        actual = my_list["first"]
        while i < my_list["size"]:
            actual = actual["next"]
            i += 1
    
        actual["next"] = None
        my_list["last"] = actual
        my_list["size"] -= 1

        if my_list["size"] == 0:
            my_list["last"] = None
            my_list["first"] = None
        return removed

def insert_element(my_list, elm, pos):

    if pos < 0 or pos > my_list["size"]:
        return my_list 
    new_node = {"info": elm, "next": None}

    if pos == 0:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node
        if my_list["last"] is None:
            my_list["last"] = new_node
    elif pos == my_list["size"]:
        if my_list["last"] is not None:
            my_list["last"]["next"] = new_node
        my_list["last"] = new_node
        if my_list["first"] is None:
            my_list["first"] = new_node
    else:
        prev = my_list["first"]
        for _ in range(pos - 1):
            prev = prev["next"]
        new_node["next"] = prev["next"]
        prev["next"] = new_node

    my_list["size"] += 1
    return my_list


def delete_element(my_list, pos):

    if pos == 0:
        remove_first(my_list) # remove_first already modifies my_list
        return my_list # Return the modified list here
    elif 0 < pos < my_list["size"]:
        prev = my_list["first"]
        for _ in range(pos - 1):
            prev = prev["next"]
        prev["next"] = prev["next"]["next"]
        if prev["next"] is None:
            my_list["last"] = prev
        my_list["size"] -= 1
        return my_list
    return None

def change_info(my_list, pos, new_info):

    if 0 <= pos < my_list["size"]:
        current = my_list["first"]
        for _ in range(pos):
            current = current["next"]
        current["info"] = new_info
        return new_info
    return None

def exchange(my_list, pos1, pos2):
    if not isinstance(pos1, int) or not isinstance(pos2, int):
        raise TypeError(f"exchange() recibió valores incorrectos: pos1={pos1}, pos2={pos2}")
    
    if 0 <= pos1 < my_list["size"] and 0 <= pos2 < my_list["size"]:
        current1 = my_list["first"]
        for _ in range(pos1):
            current1 = current1["next"]
        
        current2 = my_list["first"]
        for _ in range(pos2):
            current2 = current2["next"]

        current1["info"], current2["info"] = current2["info"], current1["info"]
        return my_list
    else:
        raise IndexError("exchange(): posiciones fuera de rango")

def sub_list(my_list, start, length):

    if not (0 <= start < my_list["size"]) or length <= 0:
        return new_list()

    current = my_list["first"]
    for _ in range(start):
        current = current["next"]

    sublist = new_list()
    for _ in range(length):
        if current is None:
            break
        add_last(sublist, current["info"])
        current = current["next"]
    return sublist

def default_sort_criteria (elm1,elm2):
    is_sorted = False
    if elm1 <= elm2:
      is_sorted = True
    return is_sorted

def default_cmp_function(a, b):
   #n.castano hizo esta calidad pa single"
    return a - b  


def selection_sort(my_list, cmp_function):
    if my_list["size"] < 2:
        return my_list  # No es necesario ordenar si hay 0 o 1 elementos

    current = my_list["first"]
    
    while current is not None:
        min_node = current
        search = current["next"]

        while search is not None:
            if cmp_function(search["info"], min_node["info"]) < 0:
                min_node = search
            search = search["next"]
        
        # Intercambiar valores en lugar de nodos
        if min_node != current:
            current["info"], min_node["info"] = min_node["info"], current["info"]

        current = current["next"]
    
    return my_list    
        
def insertion_sort(lista, default_sort_criteria):
    for i in range(1, lista["size"]):
        j = i
        while j > 0 and not default_sort_criteria(get_element(lista, j - 1), get_element(lista, j)):
            exchange(lista, j - 1, j)  
            j -= 1
    return lista
    

def shell_sort(list,default_sort_criteria):
    h = 1
    while h < size(list):
        h = (3*h) + 1
    
    h //= 3
    h -= 1

    while h >= 1:
        for i in range (size(list)-h):
            elm1 = get_element(list,i)
            elm2 = get_element(list,i+h)
            if not default_sort_criteria (elm1,elm2):
                exchange(list,i,i+h)
                ordenado = False
                j = i
                while not ordenado:
                    if j-h >= 0:
                        if not default_sort_criteria(get_element(list,j-h),get_element(list,j)):
                            exchange(list,j-h,j)
                            ordenado = False
                            j -= h
                        else:
                            ordenado = True
                    else:
                        ordenado = True
        h //=3       
            
    '''''
    searchpos = 0
    retorno = []
    node = list['first']
    while searchpos < size(list)-1:
        node = node['next']
        retorno.append(node['info'])
        searchpos += 1
    '''
    return list

 
def merge_sort(my_list, cmp_function):
    if my_list["size"] <= 1:
        return my_list
   
    mid = my_list["size"] // 2
    left_list = sub_list(my_list, 0, mid)
    right_list = sub_list(my_list, mid, my_list["size"] - mid)


    left_list = merge_sort(left_list, cmp_function)
    right_list = merge_sort(right_list, cmp_function)


    return merge_linked_lists(left_list, right_list, cmp_function)


def merge_linked_lists(left, right, cmp_function):
    result = new_list()
    while left["first"] is not None and right["first"] is not None:
        if cmp_function(left["first"]["info"], right["first"]["info"]) < 0:
            add_last(result, left["first"]["info"])
            left["first"] = left["first"]["next"]
        else:
            add_last(result, right["first"]["info"])
            right["first"] = right["first"]["next"]


    while left["first"] is not None:
        add_last(result, left["first"]["info"])
        left["first"] = left["first"]["next"]


    while right["first"] is not None:
        add_last(result, right["first"]["info"])
        right["first"] = right["first"]["next"]


    return result


def quick_sort_recursive(list,default_sort_criteria,lo,hi):
    if lo >= hi:
        return
    pivote = partition(list,default_sort_criteria,lo,hi)
    quick_sort_recursive(list,default_sort_criteria,lo,pivote-1)
    quick_sort_recursive(list,default_sort_criteria,pivote+1,hi)

    
    

def quick_sort(list,default_sort_criteria):
    quick_sort_recursive(list,default_sort_criteria,0,size(list)-1)
    
    return list
    

def partition (list,default_sort_criteria,lo,hi):
    #print(f"\nParticionando entre {lo} y {hi}")
    pivote = hi
    pivote_elm = get_element(list,pivote)
    peque = lo - 1
    i = lo
    while i < pivote:
        elm1 = get_element(list,i)
        #print(f"Comparando {elm1} con {pivote_elm}")
        if default_sort_criteria(elm1,pivote_elm):
            peque += 1
            if peque != i:
                #print(f"  -> {elm1} es menor, peque es {get_element(list,peque-1)} intercambio {get_element(list,peque)} con {elm1}")
                exchange(list,peque,i)
        i += 1

    if peque + 1 != pivote:
        #print(f"\nIntercambiando pivote {pivote_elm} con {get_element(list,peque+1)}")
        exchange(list,peque + 1, pivote)

    '''
    searchpos = 0
    node = list['first']
    retorno = [node["info"]]
    while searchpos < size(list)-1:
        node = node['next']
        retorno.append(node['info'])
        searchpos += 1'
    '''
    #print(f"Lista después de particionar: {retorno} y pivote es {get_element(list,peque+1)}\n")

    
    return peque + 1


# Crear una tabla vacía
my_table = new_map(5, 0.5)
print(my_table)


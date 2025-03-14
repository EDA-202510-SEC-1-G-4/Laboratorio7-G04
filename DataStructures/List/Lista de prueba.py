# App/logic.
import array_list as al
import single_linked_list as sll
# Función de comparación por defecto
sort_crit = sll.default_sort_criteria


# Crea una lista vacía
lista = sll.new_list()
lista = sll.add_last(lista, 3)
lista = sll.add_last(lista, 17)
lista = sll.add_last(lista, 25)
lista = sll.add_last(lista, 8)
lista = sll.add_last(lista, 92)
lista = sll.add_last(lista, 46)
lista = sll.add_last(lista, 57)
lista = sll.add_last(lista, 30)
lista = sll.add_last(lista, 14)
lista = sll.add_last(lista, 20)
lista = sll.add_last(lista, 3)
lista = sll.add_last(lista, 17)
lista = sll.add_last(lista, 25)
lista = sll.add_last(lista, 8)
lista = sll.add_last(lista, 92)
lista = sll.add_last(lista, 46)
lista = sll.add_last(lista, 57)
lista = sll.add_last(lista, 30)
lista = sll.add_last(lista, 14)
lista = sll.add_last(lista, 20)





#print(sll.quick_sort(lista,sort_crit,0,al.size(lista)-1))

''''
searchpos = 0
node = lista['first']
print(node['info'])
while searchpos < sll.size(lista)-1:
    node = node['next']
    print(node['info'])
    searchpos += 1
'''   
print(sll.quick_sort(lista,sort_crit))





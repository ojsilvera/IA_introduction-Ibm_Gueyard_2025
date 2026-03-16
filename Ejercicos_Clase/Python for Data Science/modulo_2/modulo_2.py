# listas y tuplas
# las listas son mutables, es decir, se pueden modificar después de su creación
# las tuplas son inmutables, es decir, no se pueden modificar después de su creación
# listas
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)
# tuplas
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
# acceso a los elementos de una lista y una tupla
print(mi_lista[0])  # acceso al primer elemento de la lista
print(mi_tupla[0])  # acceso al primer elemento de la tupla
# modificación de una lista
mi_lista[0] = 10
print(mi_lista)
# modificación de una tupla (esto generará un error)
# mi_tupla[0] = 10
# concatenación de listas y tuplas
nueva_lista = mi_lista + [6, 7, 8]
print(nueva_lista)
nueva_tupla = mi_tupla + (6, 7, 8)
print(nueva_tupla)
# longitud de una lista y una tupla
print(len(mi_lista))
print(len(mi_tupla))
# métodos de las listas
mi_lista.append(9)  # agrega un elemento al final de la lista
print(mi_lista)
mi_lista.insert(0, 0)  # inserta un elemento en una posición específica
print(mi_lista)
mi_lista.remove(3)  # elimina la primera aparición de un elemento en la lista
print(mi_lista)
# métodos de las tuplas (no hay métodos para modificar las tuplas, pero se pueden usar métodos para acceder a sus elementos)
print(mi_tupla.count(1))  # cuenta el número de veces que un elemento aparece en la tupla
print(mi_tupla.index(3))  # devuelve el índice de la primera aparición de un elemento en la tupla

# listas anidadas
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_anidada)
# acceso a los elementos de una lista anidada
print(lista_anidada[0])  # acceso a la primera sublista
print(lista_anidada[0][0])  # acceso al primer elemento de la primera sublista
# modificación de una lista anidada
lista_anidada[0][0] = 10
print(lista_anidada)

# tuplas anidadas
tupla_anidada = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tupla_anidada)
# acceso a los elementos de una tupla anidada
print(tupla_anidada[0])  # acceso a la primera subtupla
print(tupla_anidada[0][0])  # acceso al primer elemento de la primera subtupla
# modificación de una tupla anidada (esto generará un error)
# tupla_anidada[0][0] = 10
# concatenación de listas anidadas y tuplas anidadas
nueva_lista_anidada = lista_anidada + [[10, 11, 12]]
print(nueva_lista_anidada)
nueva_tupla_anidada = tupla_anidada + ((10, 11, 12),)
print(nueva_tupla_anidada)

# quiz
# How do you access the last element of the following tuple: A=(0,1,2,3)? Select all possible correct answers.
A = (0, 1, 2, 3)
print(A[-1])  # acceso al último elemento de la tupla
print(A[3])   # acceso al último elemento de la tupla usando su índice

# Consider the list: B=["a","b","c"]. What is the result of the following B[1:]?
B = ["a", "b", "c"]
print(B[1:])  # acceso a los elementos de la lista desde el índice 1 hasta el final de la lista


# sets
# los sets son colecciones de elementos únicos y no ordenados
# creación de un set
mi_set = {1, 2, 3, 4, 5}
print(mi_set)
# acceso a los elementos de un set (no se puede acceder a los elementos de un set por su índice, pero se puede iterar sobre ellos)
for elemento in mi_set:
    print(elemento)
# modificación de un set
mi_set.add(6)  # agrega un elemento al set
print(mi_set)
mi_set.remove(3)  # elimina un elemento del set
print(mi_set)
# operaciones con sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))  # unión de dos sets
print(set_a.intersection(set_b))  # intersección de dos sets
print(set_a.difference(set_b))  # diferencia de dos sets
print(set_a.symmetric_difference(set_b))  # diferencia simétrica de dos sets

# quiz

# What is the result of the following lines of code:

S={'A','B','C'}

U={'A','Z','C'}

U.union(S)

# The result of the code will be a set that contains all the unique elements from both sets S and U. The union of sets S and U will be:
{'A', 'B', 'C', 'Z'}

# What is the intersection of set S and U?

S={'A','B','C'}

U={'A','Z','C'}

# The intersection of sets S and U will be a set that contains only the elements that are present in both sets. The intersection of sets S and U will be:
{'A', 'C'}

# dictionaries
# los diccionarios son colecciones de pares clave-valor
# creación de un diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario)
# acceso a los elementos de un diccionario
print(mi_diccionario["nombre"])  # acceso al valor asociado a la clave "nombre"
print(mi_diccionario.get("edad"))  # acceso al valor asociado a la clave "edad" usando el método get
# modificación de un diccionario
mi_diccionario["edad"] = 31  # modificación del valor asociado a la clave "edad"
print(mi_diccionario)
mi_diccionario["profesión"] = "Ingeniero"  # adición de un nuevo par clave-valor al diccionario
print(mi_diccionario)
# eliminación de un elemento de un diccionario
del mi_diccionario["ciudad"]  # eliminación del par clave-valor asociado a la clave "ciudad"
print(mi_diccionario)
# métodos de los diccionarios
print(mi_diccionario.keys())  # devuelve una vista de las claves del diccionario
print(mi_diccionario.values())  # devuelve una vista de los valores del diccionario
print(mi_diccionario.items())  # devuelve una vista de los pares clave-valor del diccionario

# quiz
# Consider the following dictionary:

D = {'a':0,'b':1,'c':2}

# What is the result of the following: D.values()?
# The result of D.values() will be a view object that displays a list of all the
# values in the dictionary D. In this case, the values are 0, 1, and 2. So the output will be: dict_values([0, 1, 2])

result = D.values()
print(result)

# Consider the following dictionary:
# What is the output of the following D['b']? # The output of D['b'] will be the
# value associated with the key 'b' in the dictionary D. In this case, the value is 1. So the output will be: 1

D = {'a':0,'b':1,'c':2}
resultKey = D['b']
print(resultKey)

# quiz review

# What is the syntax used to obtain the first element of the tuple:

A = ('a','b','c')

print(A[0])  # acceso al primer elemento de la tupla

# true or false, After applying the following method, L.append(['a','b']), the following list will only be one element longer.

L = [1, 2, 3]
L.append(['a', 'b'])

print(L)

# la lista L ahora contiene el elemento [1, 2, 3, ['a', 'b']], por lo
# que es un elemento más larga, pero el elemento añadido es una lista, no dos elementos separados.
# Por lo tanto, la afirmación es verdadera

# How many duplicate elements can you have in a set?
# En un set no se pueden tener elementos duplicados, por lo que el número de
# elementos duplicados en un set es cero.
# Si intentas añadir un elemento que ya existe en el set, simplemente no se añadirá
# y el set permanecerá sin cambios.

# Consider the following Python dictionary:

Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}

# What is the result of the following operation: Dict["D"]?
# The result of Dict["D"] will be the value associated with the key "D" in the
# dictionary Dict. In this case, the value is the tuple (4, 4, 4). So the output will be: (4, 4, 4)

# What is an important difference between lists and tuples?
# Lists can't contain a string.
# Tuples can only have integers.
#Lists and tuples are the same.
# Lists are mutable, tuples are not.
# There are no zeros in lists.

# The important difference between lists and tuples is that lists are mutable,
# meaning they can be modified after their creation, while tuples are immutable,
# meaning they cannot be modified after their creation. This means that you can add,
# remove, or change elements in a list, but you cannot do the same with a tuple.
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





# Este es un programa simple en Python que imprime "Hello, World!" en la consola.
print('Hello, World!')

# Esto imprimirá <class 'float'>, indicando que 3.14 es un número de punto flotante.
print(type(3.14))

# Esto imprimirá <class 'str'>, indicando que 'Hello, World!' es una cadena de texto.
print(type('Hello, World!'))

# expresión matemática simple que suma dos números.
result = 5 + 3
print(result)  # Esto imprimirá 8, que es la suma de 5 y 3.

# expresion matemática simple de resta
result = 10 - 4
print(result)  # Esto imprimirá 6, que es la resta de 10 y 4.

# expresion matemática simple de multiplicación
result = 7 * 6
print(result)  # Esto imprimirá 42, que es el producto de 7 y 6.

# expresion matemática simple de división
result = 20 / 5
print(result)  # Esto imprimirá 4.0, que es el resultado de dividir 20 entre 5.

# variables y asignación
x = 10
y = 20
z = x + y
print(z)  # Esto imprimirá 30, que es la suma de x e y

# strings y concatenación
# Esto imprimirá 'John Doe', que es la concatenación de
# first_name y last_name con un espacio entre ellos.

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
print(full_name)

# obtener los pares del siguiente string
text = "0123456"

# Esto imprimirá '0246', que son los caracteres en las posiciones pares del string.

even_index_chars = text[::2]
print(even_index_chars)

# cual seria la salida de la siguiente expresión
result = "0123456".find('1')
# Esto imprimirá 1, que es el índice de la primera aparición del carácter '1' en el string "0123456".
print(result)

# ejercicios propuesto quiz 1

# el resultado para la siguiente operacion

op = 3 + 2 * 2
print(op)  # Esto imprimirá 7, que es el resultado de la operación 3+2*2 (siguiendo el orden de operaciones)

# In Python, if you executed name = 'Lizz', what would be the output of print(name[0:2])?
name = 'Lizz'
print(name[0:2])  # Esto imprimirá 'Li', que son los caracteres
# en las posiciones 0 y 1 del string 'Lizz' (el índice 2 no se incluye).

# In Python, if you executed var = '01234567', what would be the result of print(var[::2])?
var = '01234567'
print(var[::2])  # Esto imprimirá '0246', que son los caracteres
# en las posiciones pares del string '01234567' (índices 0, 2, 4, 6).

# In Python, what is the result of the following operation '1'+'2'?
result = '1' + '2'
print(result)  # Esto imprimirá '12', que es la concatenación de las cadenas '1' y '2'.

# Given myvar = 'hello', how would you convert myvar into uppercase?
myvar = 'hello'
uppercase_var = myvar.upper()
print(uppercase_var)  # Esto imprimirá 'HELLO', que es la versión en mayúsculas de la cadena 'hello'.
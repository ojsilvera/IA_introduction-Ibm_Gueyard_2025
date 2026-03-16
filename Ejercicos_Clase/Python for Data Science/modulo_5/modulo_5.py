# Numpy
# Numpy es una biblioteca de Python que se utiliza para trabajar con arreglos
# multidimensionales y realizar operaciones matemáticas de manera eficiente. Es
# fundamental para el análisis de datos y la ciencia de datos, ya que proporciona
# una estructura de datos eficiente y funciones optimizadas para realizar cálculos
# numéricos.

# example
import numpy as np
# Crear un arreglo de Numpy
arr = np.array([1, 2, 3, 4, 5])
print(arr)
# Operaciones con arreglos
print(arr + 10)  # Suma 10 a cada elemento del arreglo
print(arr * 2)   # Multiplica cada elemento del arreglo por 2
# Crear un arreglo bidimensional
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# Acceder a elementos específicos
print(arr_2d[0, 1])  # Accede al elemento en la primera fila y segunda columna (2)
# Operaciones con arreglos bidimensionales
print(arr_2d + 10)  # Suma 10 a cada elemento del arreglo bidimensional
print(arr_2d * 2)   # Multiplica cada elemento del arreglo bidimensional por 2
# Funciones de Numpy
print(np.mean(arr))  # Calcula la media del arreglo
print(np.median(arr))  # Calcula la mediana del arreglo
print(np.std(arr))  # Calcula la desviación estándar del arreglo
print(np.sum(arr))  # Calcula la suma de los elementos del arreglo
print(np.min(arr))  # Encuentra el valor mínimo del arreglo
print(np.max(arr))  # Encuentra el valor máximo del arreglo
# Numpy también es útil para realizar operaciones de álgebra lineal, como la
# multiplicación de matrices, la inversa de matrices, etc.

# example
# Crear dos matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# Multiplicación de matrices
C = np.dot(A, B)
print(C)
# Inversa de una matriz
A_inv = np.linalg.inv(A)
print(A_inv)

# Numpy es una herramienta esencial para cualquier persona que trabaje con datos
# en Python, ya que proporciona una base sólida para el análisis de datos y la
# manipulación de arreglos.
# En resumen, Numpy es una biblioteca de Python que se utiliza para trabajar con
# arreglos multidimensionales y realizar operaciones matemáticas de manera eficiente.
# Es fundamental para el análisis de datos y la ciencia de datos, ya que proporciona
# una estructura de datos eficiente y funciones optimizadas para realizar cálculos
# numéricos.




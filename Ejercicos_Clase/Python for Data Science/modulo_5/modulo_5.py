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
# multiplicar dos arreglos
arr2 = np.array([10, 20, 30, 40, 50])
print(arr * arr2)  # Multiplica elemento por elemento entre arr y arr2
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

# quiz

# What is the result of the following operation:
import numpy as np
resultado = np.array([1,-1])*np.array([1,1])
print(resultado)

# array([ 0, 0])
# array([ 1, -1])
# 0

# la respuesta correcta es: array([ 1, -1])

# What is the result of the following operation:

import numpy as np
operacion = np.dot(np.array([1,-1]),np.array([1,1]))
print(operacion)

# array([0, 0])
# array([1, -1])
# 0

# la respuesta correcta es: 0

# Numpy 2D Arrays

# How many rows are in the following numpy array?

A = np.array([[1,2],[3,4],[5,6],[7,8]])

#2
# 4
# 6

# la respuesta correcta es: 4

# Is it possible to perform the following operation?

A = np.array([[1,2],[3,4],[5,6],[7,8]])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])
np.dot(A,B)

# Yes
# No

# la respuesta correcta es: No

# simple apis - apis simples
# Las APIs simples son interfaces de programación de aplicaciones que proporcionan
# una forma fácil y directa de interactuar con un servicio o una biblioteca. Estas
# APIs están diseñadas
# para ser intuitivas y fáciles de usar, lo que permite a los desarrolladores acceder
# a funcionalidades específicas sin tener que preocuparse por la complejidad subyacente.
# Las APIs simples suelen tener una sintaxis clara y concisa, lo que facilita su
# comprensión y uso. Estas APIs pueden ser utilizadas por desarrolladores de todos
# los niveles de experiencia, ya que no requieren un conocimiento profundo de la
# implementación interna del servicio o la biblioteca.
# Las APIs simples son comunes en el desarrollo de software, ya que permiten a los
# desarrolladores integrar fácilmente funcionalidades específicas en sus aplicaciones
# sin tener que reinventar la rueda. Por ejemplo, una API simple para acceder a
# datos de # una base de datos podría proporcionar métodos para realizar consultas
# básicas, mientras que una API simple para un servicio web podría ofrecer métodos
# para enviar solicitudes y recibir respuestas de manera sencilla.

# ejemplo de una API simple para acceder a datos de una base de datos:
class DatabaseAPI:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        # Aquí se establecería la conexión a la base de datos

    def query(self, sql_query):
        # Aquí se ejecutaría la consulta SQL y se devolverían los resultados
        return "Resultados de la consulta: " + sql_query
# Uso de la API simple
db_api = DatabaseAPI("mi_conexion_a_la_base_de_datos")
resultados = db_api.query("SELECT * FROM usuarios")
print(resultados)
# En este ejemplo, la clase DatabaseAPI proporciona una API simple para interactuar con una base de datos. El método query permite a los desarrolladores ejecutar consultas SQL de manera sencilla, sin tener que preocuparse por los detalles de la conexión o la ejecución de la consulta.


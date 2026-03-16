# Working with Data in Python
# leyendo archivos
import pandas as pd
# Leer un archivo CSV
data = pd.read_csv('data.csv')
# Mostrar las primeras filas del DataFrame
print(data.head())
# Leer un archivo Excel
data_excel = pd.read_excel('data.xlsx')
print(data_excel.head())
# Leer un archivo JSON
data_json = pd.read_json('data.json')
print(data_json.head())
# Manipulación de datos
# Filtrar datos
filtered_data = data[data['column_name'] > 10]
print(filtered_data)
# Agrupar datos
grouped_data = data.groupby('category_column').mean()
print(grouped_data)
# Crear nuevas columnas
data['new_column'] = data['existing_column'] * 2
print(data.head())
# Guardar el DataFrame modificado en un nuevo archivo CSV
data.to_csv('modified_data.csv', index=False)
# Guardar el DataFrame modificado en un nuevo archivo Excel
data.to_excel('modified_data.xlsx', index=False)
# Guardar el DataFrame modificado en un nuevo archivo JSON
data.to_json('modified_data.json', orient='records')

# with open
# Leer un archivo de texto
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)
# Escribir en un archivo de texto
with open('output.txt', 'w') as file:
    file.write('This is a sample output text.')
# Agregar texto a un archivo existente
with open('output.txt', 'a') as file:
    file.write('\nThis line is appended to the file.')
# Leer un archivo línea por línea
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())
# cerrar automáticamente el archivo después de su uso
# example
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)
# El archivo se cierra automáticamente después del bloque with

# quiz

# Consider the dataframe df. How would you find the element in the second row and first column?

# df.ix[0,1] or df.iloc[0,1]
# df.ix[1,0] or df.iloc[1,0]
# df[1,1]

# The correct answer is: df.ix[1,0] or df.iloc[1,0]

# Will the following code run?

import pandas as banana
df=banana.DataFrame({'a':[11,21,31],'b':[21,22,23]})
df.head()

# Yes
# No

# The correct answer is: Yes

# Working with and Saving Data with Pandas is a common task in data science. The
# code provided demonstrates how to read different types of files (CSV, Excel, JSON) into
# a pandas DataFrame, manipulate the data by filtering, grouping, and creating new columns,
# and then save the modified DataFrame back to various file formats. Additionally,
# it shows how to use the `with open` statement to read and write text files efficiently.

# quiz

# Consider the dataframe:
df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})
# What type does the following return: df['a']==1 ?

# int
# bool
# float

# The correct answer is: bool

# What task does the following method perform: df.to_csv("file.csv")?


# Save a dataframe to a csv file.
# Load a csv file to a dataframe.

# The correct answer is: Save a dataframe to a csv file.

# quiz general

# What do the following lines of code do?

with open("Example1.txt","r") as file1:

    FileContent=file1.readlines()

print(FileContent)

# Read the file "Example1.txt".
# Write to the file “Example1.txt".
# Append the file "Example1.txt".

# The correct answer is: Read the file "Example1.txt".

# What do the following lines of code do?

with open("Example2.txt","w") as writefile:

    writefile.write("This is line A\n")

    writefile.write("This is line B\n")

# Read the file "Example2.txt".
# Write to the file "Example2.txt".
# Append the file "Example2.txt".

# The correct answer is: Write to the file "Example2.txt".

# What do the following lines of code do?

with open("Example3.txt","a") as file1:

    file1.write("This is line C\n")

# Read the file "Example3.txt".
# Write to the file "Example3.txt".
# Append the file "Example3.txt".

# The correct answer is: Append the file "Example3.txt".

# What is the result of applying the following method df.head() to the dataframe "df"?

# Prints the first row of the dataframe.
# Prints the first column of the dataframe.
# Prints the first 5 rows of the dataframe.
# Prints out the entire dataframe.

# The correct answer is: Prints the first 5 rows of the dataframe.
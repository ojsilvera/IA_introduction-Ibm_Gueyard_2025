# Conditions and Branching
# If, Elif, Else
# If condition:
#     # code to execute if condition is true
# Elif another_condition:
#     # code to execute if another_condition is true
# Else:
#     # code to execute if all conditions are false

# Example:
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:    print("x is zero")

# Nested If
# If condition:
#     If another_condition:
#         # code to execute if both conditions are true
#     Else:
#         # code to execute if condition is true but another_condition is false
# Else:
#     # code to execute if condition is false

# Example:
y = 5
if y > 0:
    if y % 2 == 0:
        print("y is a positive even number")
    else:
        print("y is a positive odd number")
else:    print("y is not positive")

# quiz

# Select the values of i that produces a True for the following: valor = i!=0

# 1
# 0
# -1
#100000000

# The values of i that produce a True for the condition valor = i != 0 are:
- 1
- -1
- 100000000

# What is the output of the following:

x='a'

if(x!='a'):

    print("This is not a.")

else:

    print("This is a.")


# "This is not a."
# "This is a."

# The output of the code is: "This is a."

# Loops
# For Loop
# For variable in iterable:
#     # code to execute for each item in the iterable

# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop
# While condition:
#     # code to execute as long as condition is true

# Example:
count = 0
while count < 5:
    print(count)
    count += 1

# quiz

# What is the output of the following lines of code:

A=[3,4,5]

for a in A:

    print(a)

# The output of the code is:
# 3
# 4
# 5

# What is the output of the following lines of code:

x=3

y=1

while(y!=x):

    print(y)

y=y+1

# The output of the code is:
# 1
# 2

# functions

# Function Definition
# def function_name(parameters):
#     # code to execute when the function is called
#     return value

# Example:
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

# quiz

# What is the value of c after the following block of code is run ?

a=1

def add(b):

    return a+b

c=add(10)

# The value of c after the code is run is 11.

# What is the value of c after the following block of code is run with proper numerical input?

def f(*x):

    return sum(x)

print(f(5, 3, 4))

# Return the total of a variable amount of parameters.
# Return the total of a list.
# The function is not valid.

# The function f is valid and it takes a variable number of arguments (using *x)
# and returns the sum of those arguments using the built-in sum() function.

# objects and class

# Class Definition
# class ClassName:
#     # class attributes and methods
# Example:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
print(my_dog.bark()) # Output: Woof!

# objects
# An object is an instance of a class. It is created using the class constructor and can have its own attributes and methods.
# Example:
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = color
my_car = Car("Toyota", "Corolla", "blue")
print(my_car.make)  # Output: Toyota
print(my_car.model) # Output: Corolla
print(my_car.color) # Output: blue

# quiz

# Using the Class Car in the lab, create a Car object with the following attributes:

make="Honda"
model="Accord"
color="blue"

# Car(make="Honda",model="Accord",color="blue")
# Car("Honda","Accord","blue")
# Car(model="Accord",make="Honda",color="blue")
# Car("Accord","Honda","blue")

# The correct way to create a Car object with the given attributes is:
# Car("Honda","Accord","blue")
# Car("Accord","Honda","blue")

# From the lab, how would you change the data attribute owner_number ?

# Utilising the method sell().
# Utilising the method car_info().

# The correct way to change the data attribute owner_number is by utilizing the
# method sell() if it is defined to update that attribute. If car_info() is just
# for displaying information, it would not be the correct method to change the attribute.

# quiz general

# What is the output of the following lines of code:

x=1

if(x!=1):

    print('Hello')

else:

    print('Hi')

print('Mike')

# Hi Mike
# Mike
# Hello Mike
# The Mike

# The output of the code is: Hi Mike

# What is the output of the following few lines of code?

A = ['1','2','3']

for a in A:

    print(2*a)

# 2 4 6
# '2' '4' '6'
# '11' '22' '33'
# A B C

# The output of the code is: '11' '22' '33' because the elements in the list A
# are strings, and multiplying a string by 2 concatenates it with itself.

# Consider the function Delta, when will the function return a value of 1

def Delta(x):

    if x==0:

        y=1;

    else:

        y=0;

    return(y)

# When the input is anything but 0.
# When the input is 1.
# Never.
# When the input is 0.

# The function Delta will return a value of 1 when the input is 0, because the
# condition x == 0 will be true, and y will be set to 1 before being returned.

# What is the correct way to sort the list 'B' using a method? The result should
# not return a new list, just change the list 'B'.

# B.sort()
# sort(B)
# sorted(B)
# B.sorted()

# The correct way to sort the list 'B' in place is by using the method B.sort().
# This will sort the list without creating a new list.

# What are the keys of the following dictionary: {'a':1,'b':2}?

# 1,2
# ;,:
# a,b

# The keys of the dictionary {'a':1,'b':2} are 'a' and 'b'.
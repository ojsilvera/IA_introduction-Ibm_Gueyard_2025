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

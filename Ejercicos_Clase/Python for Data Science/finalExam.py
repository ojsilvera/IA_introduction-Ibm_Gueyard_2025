# What is the result of the following operation ?

operacion = 3+2*2

# 3
# 12
# 9
# 7

# The result is 7, because according to the order of operations (parentheses,
# exponents, multiplication and division from left to right, and addition and subtraction
# from left to right), the multiplication is performed before the addition.
# So, 2*2 is calculated first, which equals 4, and then 3 is added to that result,
# giving a final answer of 7.

# What is the type of the following variable: True?

# int
# bool
# str
# list

# The type of the variable True is bool, which stands for boolean. It represents
# a value that can be either True or False.

# What is the result of the following operation int(3.2)?

# 3.2
# 3
# 4
# '3.2'

# The result of the operation int(3.2) is 3. The int() function converts a floating-point

# Consider the string A='1234567', what is the result of the following operation: A[1::2]

# '1234567'
# '246'
# '1357'
# error

# The result of the operation A[1::2] is '246'. This is because the slicing operation
# A[1::2] starts at index 1 (which is the second character '2') and then takes every
# second character from that point onward.
# So it takes '2', skips '3', takes '4', skips '5', takes '6', and skips '7',
# resulting in the string '246'.

# Consider the string Name="Michael Jackson" , what is the result of the following operation

Name = "Michael Jackson"
operacion = Name.find('el')

# 5
# 4
# 5,6
# -1

# The result of the operation Name.find('el') is 5. The find() method returns the lowest

# The variables A='1' and B='2' ,what is the result of the operation A+B?

# you cant add two strings
# 3
# '3'
# '12'

# The result of the operation A+B is '12'. In Python, the + operator concatenates
# strings, so when you add '1' and '2', it combines them into '12'.

# Consider the variable F="You are wrong", Convert the values in the variable F to uppercase?

# F.up()
# F.upper
# F.upper()

# The correct way to convert the values in the variable F to uppercase is by using
# the method F.upper(). This will return a new string with all characters in uppercase,
# which would be "YOU ARE WRONG".

# Consider the tuple tuple1=("A","B","C" ), what is the result of the following operation tuple1[-1]?

# "A"
# "B"
# "C"

# The result of the operation tuple1[-1] is "C". In Python, negative indexing allows

# Consider the tuple A=((11,12),[21,22]), that contains a tuple and list. What is
# the result of the following operation A[1]:

# ((11,12),[21,22])
# (11,12)
# (21,22)
# [21,22]

# The result of the operation A[1] is [21,22]. In the tuple A, the first element
# (index 0) is the tuple (11,12), and the second element (index 1) is the list [21,22]
# Therefore, A[1] retrieves the second element, which is the list [21,22].

# Consider the tuple A=((11,12),[21,22]), that contains a tuple and list. What is
# the result of the following operation A[0][1]:

# 12
# 11
# 22
# 21

# The result of the operation A[0][1] is 12. In the tuple A, the first element (index 0)
# is the tuple (11,12). When you access A[0], you get the tuple (11,12). Then, when
# you access [1] of that tuple, you get the second element, which is 12. Therefore,
# A[0][1] retrieves the value 12

# What is the result of the following operation '1,2,3,4'.split(',')

# '1','2','3','4'
# ('1','2','3','4')
# ['1','2','3','4']
# '1234'

# The result of the operation '1,2,3,4'.split(',') is ['1','2','3','4']. The split() method
# takes a string and splits it into a list of substrings based on the specified delimiter,
# which in this case is a comma. So it splits the string '1,2,3,4' into the list ['1','2','3','4'].

# Concatenate the following lists A=[1,'a'] and B=[2,1,'d']:

# A+B
# A-B
# A*B
# A/B

# The correct way to concatenate the lists A and B is by using the + operator, so
# the result of A+B is [1,'a',2,1,'d']. The + operator combines the elements of
# both lists into a single list.

# How do you cast the list 'A' to the set 'a'?

# a.set()
# a=A.append()
# a=A.dict()
# a=set(A)

# The correct way to cast the list 'A' to the set 'a' is by using the set() function,
# so the result of a=set(A) will create a set 'a' that contains the unique elements
# of the list 'A'. However, since 'A' is not defined as a list in the question, we
# cannot directly cast it to a set. If 'A' were defined as a list,
# for example A = [1, 2, 3], then a = set(A) would create a set containing the
# elements {1, 2, 3}.

# Consider the Set: V={'A','B'}, what is the result of V.add('C')?

# {'A','B'}
# {'A','B','C'}
# {'AC','BC'}
# error

# The result of V.add('C') is {'A','B','C'}. The add() method adds an element to a set,
# so when you add 'C' to the set V, it will include 'C' in the set, resulting in {'A','B','C'}.

# Consider the Set: V={'A','B','C' }, what is the result of V.add('C')?

# {'A','B'}
# {'A','B','C'}
# {'A','B','C','C'}
# error

# The result of V.add('C') is still {'A','B','C'}. In a set, duplicate elements are not allowed,
# so adding 'C' again does not change the set. The set will remain {'A ,'B','C'} even after trying to add 'C' again.

# What is the output of the following lines of code:

x="Go"
if(x!="Go"):
    print('Stop')
else:
    print('Go ')
    print('Mike')

# Go Mike
# Mike
# Stop Mike
# The Mike

# The output of the code will be:
# Go
# Mike

# What is the output of the following lines of code:

x="Go"
if(x=="Go"):
    print('Go ')
else:
    print('Stop')
print('Mike')

# Go Mike
# Mike
# Stop Mike
# The Mike

# The output of the code will be:
# Go
# Mike

# how many iterations are performed in the following loop?

for n in range(3):
    print(n)

# 1
# 2
# 3
# 4

# The loop will perform 3 iterations. The range(3) function generates a sequence
# of numbers from 0 to 2, so the loop will iterate over the values 0, 1, and 2,
# resulting in a total of 3 iterations.

# What does the following loop print?

for n in range(3):
    print(n+1)

# 0 1 2
# 1 2 3
# 3 2 1
# 2 1 0

# The loop will print:
# 1
# 2
# 3
# This is because the loop iterates over the values 0, 1, and 2 (generated by range(3)),
# and for each value of n, it prints n+1. So when n is 0, it prints 1; when n is
# 1, it prints 2; and when n is 2, it prints 3.

# What is the output of the following few lines of code ?

A=['1','2','3']
for a in A:
    print(2*a)

# 2 4 6
# '2' '4' '6'
# '11' '22' '33'
# A B C

# The output of the code will be:
# '11'
# '22'
# '33'

# This is because the loop iterates over each element in the list A, which are
# the strings '1', '2', and '3'. When it prints 2*a, it concatenates the string '2'
# with each element of A. So '2' + '1' results in '21', '2' + '2' results in '22', and '2

# Consider the function add, what is the result of calling the following Add('1','1') (look closely at the return statement )

def Add(x,y):
    z=y+x
    return(y)

# error
# '2'
# '11'
# '1'

# The result of calling Add('1','1') will be '1'. The function Add takes two parameters x and y,
# and it assigns z the value of y+x, which would be '1' + '1' resulting in '11'.
# However, the function then returns y, which is the second parameter passed to the
# function. Since y is '1', the function will return '1' instead of '11'.

# Consider the class Points, what are the data attributes:

class Points(object):

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def print_point(self):
        print('x=',self.x,'y=',self.y)

# __init__
# self.x self.y
# print_point

# The data attributes of the class Points are self.x and self.y. These attributes
# are defined in the __init__ method and are used to store the x and y coordinates
# of a point in a 2D space. The __init__ method is a constructor that initializes
# these attributes when an instance of the class is created, and print_point is a
# method that prints the values of these attributes.

# What is the result of running the following lines of code ?

class Points(object):

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def print_point(self):
        print('x=',self.x,' y=',self.y)
        p1=Points(1,2)
        p1.print_point()

# x=1
# y=2
# x=1 y=2

# The result of running the code will be:
# x= 1  y= 2
# This is because when the class Points is defined, it includes a method print_point that
# prints the values of x and y. When an instance of the class is created with p1 = Points(1,2),
# it initializes the attributes x and y with the values 1 and 2, respectively.
# Then, when p1.print_point() is called, it executes the print_point method, which
# outputs the values of x and y in the format specified in the print statement.

# What is the result of running the following lines of code ?

class Points(object):

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def print_point(self):
        print('x=',self.x,' y=',self.y)
        p2=Points(1,2)
        p2.x=2
        p2.print_point()

# x=1
# y=2
# x=1 y=2
# x=2 y=2

# The result of running the code will be:
# x= 2  y= 2

# This is because when the class Points is defined, it includes a method print_point that
# prints the values of x and y. When an instance of the class is created with
# p2 = Points(1,2), it initializes the attributes x and y with the values 1 and 2,
# respectively. Then, the line p2.x = 2 changes the value of x to 2. Finally,
# when p2.print_point() is called, it executes the print_point method,
# which outputs the updated values of x and y, resulting in "x= 2  y= 2".

# Consider the following line of code: with open(example1,"r") as file1:

# What mode is the file object in?

# read
# write
# append

# The file object is in read mode. The "r" argument in the open() function indicates that the file is being opened for reading. This means that you can read the contents of the file, but you cannot modify it or write new data to it while it is open in this mode.
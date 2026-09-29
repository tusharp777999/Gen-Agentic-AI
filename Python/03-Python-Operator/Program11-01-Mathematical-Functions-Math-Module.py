'''
Mathematical functions from math module:
Module: A group of variables, functions, classes save into the file, such type of file is considered as Module.
'''
import module_file
module_file.addition(10, 20)
module_file.multiplication(10, 20)

#Various ways to import module
'''
Example 01:
from math1 import *
from math2 import *

print(sqrt(4))

In this program we have two modules imported from math1 and math2 both having sqrt() method. From this both which one it will use
or it will give you a error.
The answer is Python follow latest one, even if you have two similar variables, methods, classes ... etc it will take latest one.
'''
def function():
    print('Old function.')

def function():
    print('New function.')

function()

'''
Important functions in math module:
sqrt(x)
floor(x)
ceil(x)
pow(x, y)
gcd(x, y)
sin()
cos()
tan()
...etc

Important variables in math mdoule:
pi : pi value.
e : Logarithmic base e
inf : Infinity
nan : Not a number
...etc
'''
#Find area of circle for a given radius.
from math import *
radius = int(input('Enter radius: '))
print('Area of circle is: ', pi * radius * radius)
print('Area of circle is: ', pi * radius ** 2)
print('Area of circle is: ', pi * pow(radius, 2))
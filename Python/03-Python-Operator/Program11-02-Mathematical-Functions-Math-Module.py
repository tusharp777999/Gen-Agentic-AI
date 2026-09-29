'''
Mathematical functions from math module:
In Python there are many modules present in it.
To import module we need to use 'import' keyword.
To shorten the module name we can use alias name using 'as' keyword. 
Note: Once we have alias name we can't use real module name it will give you an error.
Example:
    math, random, time, threading ...etc.
'''
#To print all module functions and constants:
import math
print(dir(math))
print(math.sqrt(16)) # 4.0
print(math.pi) # 3.141592653589793
print(math.e) # 2.718281828459045
print(math.floor(3.9)) # 3
print(math.ceil(3.9)) # 4
print(math.pow(3,2)) # 9.0

#Instead of math we can use alias name using as keyword as below
import math as m
print(m.sqrt(16)) # 4.0
print(m.pi) # 3.141592653589793

#If you don't want to use any module name or alias the we can use 'from' keyword.
from math import sqrt
print(sqrt(25)) # 5
print(pi) # It will give error because we just imported only one function from math module.

#To solve the problem of importing of 'pi' we have two ways.
from math import sqrt, pi
#from math import *
print(sqrt(25)) # 5.0
print(pi) 

#For memebers also alias name is possible
from math import sqrt as s
print(s(16)) # 4.0

from math import sqrt as s, pi as p
print(s(25)) # 5.0
print(p) 
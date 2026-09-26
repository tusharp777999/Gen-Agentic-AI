'''
and : returns True if both argument are True.
or : returns True if atleast one argument is True.
not : it is reverse/complement operators
'''
#Behaviour for boolean data types using 'and' operator:
print('True and True : ', True and True) # True
print('True and False : ', True and False) # False
print('False and True : ', False and True) # False
print('False and Fasle : ', False and False) # False

#Behaviour for boolean data types using 'or' operator:
print('True or True : ', True or True) # True
print('True or False : ', True or False) # True
print('False or True : ', False or True) # True
print('False or Fasle : ', False or False) # False

#Behaviour for boolean data types using 'not' operator:
print('not True : ', not True) # False
print('not False : ', not False) # True

#Program to demonstrate the use of operators:
username = input('Enter Username: ')
password = input('Enter Password: ')

if username == 'Tushar' and password == '1234':
    print('Valid user.')
else:
    print('Invalid user.')

'''
For non-boolean type how the behaviour is:
0 : It means False.
non-zero : It means True.
Empty : str, list, tuple, set, dict considered as False.
'''

'''
x and y: Both are non boolean type.
The result will be x or y but not boolean value.

If x is false, then result is x.
If x is True, then result is y.
'''
print(10 and 20) # 20
print(0 and 20) # 0
print('Tushar' and 'Patil') # Patil
print('' and 'Patil') # Empty string

'''
x or y: Both are non boolean type.
The result will be x or y but not boolean value.

If x is false, then result is y.
If x is True, then result is x.
'''
print(10 or 20) # 10
print(0 or 20) # 20
print('Tushar' or 'Patil') # Tushar
print('' or 'Patil') # Patil

'''
not operator for non-boolean type
Result is always boolean.
'''
print(not 'Tushar') # False
print(not '') # True
print(not 0) # True
print(not 10) # False
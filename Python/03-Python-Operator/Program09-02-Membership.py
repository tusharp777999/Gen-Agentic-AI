'''
Membership Operator:
It is special type of Operator.
in : It returns True if particular object or its part present in another one then it return True otherwise False.
not in : It returns True if particular object or its part is not present in another one then it return True otherwise False.
Note: It is case sensitive.
'''
string = 'Hello, learning Python is very easy.'
print('h' in string) # True
print('T' in string) # False

print('T' not in string) # True
print('python' in string) # False
print('Python' in string) # True

list1 = ['Sunny', 'Bunny', 'Chinny', 'Vinny']
print('Sunny' in list1) # True
print('Pinny' in list1) # False
print('Pinny' not in list1) # True

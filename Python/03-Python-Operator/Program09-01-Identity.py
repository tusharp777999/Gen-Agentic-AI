'''
Identity Operator:
It is special type of Operator.
is : It returns True if Object1 and Object2 pointing to the same object otherwise returns False.
is not : It returns True if Object1 and Object2 are not pointing to the same object otherwise returns False.
'''
a = 10
b = 10
print(a is b) # True
print(a is not b) # False

list1 = [10, 20, 30, 40]
list2 = [10, 20, 30, 40]
print(list1 is list2) # False
print(list1 is not list2) # True
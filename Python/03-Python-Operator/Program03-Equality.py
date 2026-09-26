'''
== : It checks whether the values of two operands are equal or not. If yes, then the condition becomes true.
!= : It checks whether the values of two operands are equal or not. If the values are not equal, then the condition becomes true.
'''
a = 10
b = 20
print("a == b : ", a == b) # False
print("a != b : ", a != b) # True
print(1 == True) # True
print(10 == 10.0) # True
print('Tushar' == 'Tushar') # True

#Note: During Equality Operator if both sides are not belong to same data type it wont raise any error it simply returns False.
print(10 == 'Tushar') #False
print(10 == '10') #False

#Equality Operator chaining.
print(10 == 10 == 10 == 10) # True
print(10 == 20 == 30 == 40) # False

#Difference between '==' operator and 'is' operator.
# '==' operator is for content comparision.
# 'is' operator is for reference/address comparision.  

list1 = [10, 20, 30] # Separate object.
list2 = [10, 20, 30] # Seperate object.
print(list1 == list2) # True
print(list1 is list2) # False

list3 = list1 # Pointing to same object
print(list1 == list3) # True
print(list1 is list3) # True
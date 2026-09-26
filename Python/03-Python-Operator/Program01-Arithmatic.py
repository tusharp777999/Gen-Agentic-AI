'''
+ : Addition operator
- : Subtraction operator
* : Multiplication operator
/ : Division operator(Quotient)
% : Modulus operator(Remainder)
// : Floor Division operator
** : Exponentiation operator or power operator
'''

a = 10
b = 2
print("Addition of a and b is : ", a + b)
print("Subtraction of a and b is : ", a - b)
print("Multiplication of a and b is : ", a * b)
print("Division of a and b is : ", a / b)
print("Modulus of a and b is : ", a % b)
print("Floor Division of a and b is : ", a // b)
print("Exponentiation of a and b is : ", a ** b)

c = 20.5
d = 2
print("Division of c and d is : ", c / d)
print("Floor Division of c and d is : ", c // d)

print("Tushar" + " " + "Patil")  # String concatenation both should be string

print("Tushar" * 3)  # String repetition one should be string and other should be integer
print(3 * "Tushar")  # String repetition one should be string and other should be integer
print("Tushar" * True)  # String repetition one should be string and other can be boolean True is considered as 1.
print("Tushar" * False)  # String repetition one should be string and other can be boolean False is considered as 0. Empty string will be printed.
print("Tushar" * -1)  # String repetition one should be string and other can be negative integer. Empty string will be printed.
print("Tushar" * None)  # String repetition one should be string and othe can be None. TypeError will be raised.

print(10 / 0)  # Division by zero will give error
print(10 // 0)  # Floor Division by zero will give error
print(10 % 0)  # Modulus by zero will give error
print(10.0 / 0.0)  # Division by zero will give error
print(10.0 // 0.0)  # Floor Division by zero will give error
print(10.0 % 0.0)  # Modulus by zero will give error
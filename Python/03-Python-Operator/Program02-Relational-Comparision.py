'''
Relational Operators in Python
< : Less than
> : Greater than
<= : Less than or equal to
>= : Greater than or equal to
'''
a = 10
b = 20
print("a < b : ", a < b)
print("a > b : ", a > b)
print("a <= b : ", a <= b)
print("a >= b : ", a >= b)

print(ord('a'))  # To get the ASCII value of a character.
print(chr(97))  # To get the character of an ASCII value.

c = 'Tushar'
d = 'Patil'
print("c < d : ", c < d)
print("c > d : ", c > d)
print("c <= d : ", c <= d)
print("c >= d : ", c >= d)

e = 'Tushar'
f = 'Tushar'
print("e < f : ", e < f)
print("e > f : ", e > f)
print("e <= f : ", e <= f)
print("e >= f : ", e >= f)

#Relational Operators chaining.
print(10 < 20 < 30)  # True
print(10 < 20 > 30)  # False
print(10 < 20 < 30 > 40 < 50)  # False because print((10 < 20) and (20 < 30) and (30 > 40) and (40 < 50)) it evaluates like this.

#Note: If both sides are not belong to similar data type during Relational it raise error.
print(10 < "Tushar") #Error
'''
Operator Precedence:
If multiple operators are there, in which order they will execute is called as Operator Precedence.

() : Parenthesis.
++ : Exponential Operator.
~, - : Bitwise complement operator and Unary minus operator.
*, %, /, // : Multiplication, Modulo, Division and Floor division.
+, - : Addition and Substraction.
<<, >> : Left shift and Right shift.
& : Bitwise and.
^ : Bitwise XOR.
| : Bitwise or.
==, !=, <, <=, >, >= : Comparision and Relational operator.
=, +=, -=, *=, %=, /=, //=, **=, &=, |=, ^=, <<=, >>= : Assignment operators.
is, is not : Identity operators.
in, not in : Membership operators.
not : Logical not.
and : Logical and.
or : Logical or.
'''
print(10 + 2 * 3) # 16
print((10 + 2) * 3) # 36

a = 30
b = 20
c = 10
d = 5
print((a + b) * c / d) # 100.0
print((a + b) * (c / d)) # 100.0
print(a + (b * c) / d) # 70.0
print(3 / 2 * 4 + 3 + (10 / 5) ** 3 - 2) # 15.0

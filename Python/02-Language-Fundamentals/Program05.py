'''
complex: It is called a complex data type. It is used to store complex numbers in the form of a + bj, where a is the real part and b is the imaginary part. For example, 2 + 3j, -1 - 4j are all complex numbers.
Note: In Python, the imaginary part is represented using the letter 'j' or 'J'
'''

x = 10 + 20j;
print(x) #To print the value of x
print(type(x)) #To print the type of x

print(x.real) #To print the real part of x
print(x.imag) #To print the imaginary part of x

z = 11.5 + 2.5j;
print(z) #To print the value of z
#Note: We can use integer or float values for the real and imaginary parts of a complex number.

k = 0b1111 + 15j;
print(k) #To print the value of k
#Note: We can use binary, octal, decimal or hexadecimal values for the real part of a complex number but not for the imaginary part. Only integer or float values can be used for the imaginary part of a complex number.
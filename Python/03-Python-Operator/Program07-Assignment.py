'''
Assignment Operators:
= :
+= :
-= :
*= :
/= :
%= :
//= :
**= :
&= :
|= :
^= :
<<= :
>>= :

Note: 
    x = 10
    x++ (or) x--
    print(x)

    There is no such increment or decrement operator in Python like ++ or -- if you try to use it will give you syntax error.
    But we can use sign before any variable as below
    x = 10
    print(+x) # 10
    print(++x) # 10
    print(+++++++++x) # 10

    print(-x) # -10
    print(--x) # 10
    print(---------x) # -10
'''
x = 10
x += 20
print("Addition is: ",x)

x = 10
x -= 20
print("Substraction is: ", x)

x = 10
x *= 20
print("Multiplication is: ", x)

x = 10
x /= 20
print("Division is: ", x)

x = 10
x %= 20
print("Modulo is: ", x)

x = 10
x //= 20
print("Floor Division is: ", x)

x = 10
x **= 2
print("Power is: ", x)

x = 10
x &= 20
print("AND is: ", x)

x = 10
x |= 20
print("OR is: ", x)

x = 10
x ^= 20
print("XOR is: ", x)

x = 10
x <<= 2
print("Left Shift is: ", x)

x = 10
x >>= 2
print("Right Shift is: ", x)

x = 10
print(+x) # 10
print(++x) # 10
print(+++++++++x) # 10

print(-x) # -10
print(--x) # 10
print(---------x) # -10
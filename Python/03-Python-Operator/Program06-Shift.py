'''
Shift Operator:
    << : Left Shift Operator
    Example:
        10 << 2
        0000 0000 0000 0000 0000 0000 0000 1010 : 10
     00 0000 0000 0000 0000 0000 0000 0010 1000 : 40 (Shifted 2 bits to the left side so answer is 40)
     ^
     Shifted bits to the left side.
     
    >> : Right Shift Operator
    Example:
            10 >> 2
            0000 0000 0000 0000 0000 0000 0000 1010 : 10
            0000 0000 0000 0000 0000 0000 0000 0010 10 : 2 (Shifted 2 bits to the right side so answer is 2)
                                                    ^
                                                Shifted bits to the right side.
    Note: While doing Left Shift add 0 to the right side.
          But while doing Right Shift add sign bit to the Right side.
'''
print(10 << 2) # 40
print(10 >> 2) # 2

'''
Bitwise Operator bheaviour in boolean data type:
'''
print(True & False) # False
print(True | False) # True
print(True ^ False) # True

'''
~True will not be False
~True equivalent to ~1

0000 0000 0000 0000 0000 0000 0000 0001 : 1
1111 1111 1111 1111 1111 1111 1111 1110 : ~1
^
MSB(It is negative value.) 

0000 0000 0000 0000 0000 0000 0000 0001 : 1's compliment
---------------------------------------
                                      1 : Adding 1 for 2's compliment
---------------------------------------
0000 0000 0000 0000 0000 0000 0000 0010 : 2

MSB was 1 so the final answer is: -2
'''
print(~ True) # -2

'''
True << 2
True equivalent to 1

    0000 0000 0000 0000 0000 0000 0000 0001 : 1
00  0000 0000 0000 0000 0000 0000 0000 0100 : 4
^
MSB(It is 0 that means it is positive number.)
'''
print(True << 2) # 4

'''
True >> 2
True equivalent to 1

0000 0000 0000 0000 0000 0000 0000 0001 : 1
0000 0000 0000 0000 0000 0000 0000 0000 01 : 0
^
MSB(It is 0 that means it is positive number.)
'''
print(True >> 2) # 0
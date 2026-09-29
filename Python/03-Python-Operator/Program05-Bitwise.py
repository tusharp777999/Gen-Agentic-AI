'''
Bitwise Operators:
& (Bitwise and operator): If both bits are 1 then result it is 1 otherwise 0.
    Example:
        4 2 1
        -----
        1 0 0
        0 1 0
        -----
        0 0 0 -> 0
| (Bitwise or operator): If atleast one bit is 1 then it is 1 otherwise 0.
    Example:
        4 2 1
        -----
        1 0 0
        0 1 0
        -----
        1 1 0 -> 6
^ (Bitwise XOR operator): If both bits are different then it is 1 otherwise 0.
    Example:
        8 4 2 1
        -------
        1 0 0 1
        0 1 0 1
        -------
        1 1 0 0 -> 12

~ (Bitwise complement operator):
<< (Bitwise left shift operator):
>> (Bitwise right shift operator):
Note: It is applicable for only integer and boolean data type.
'''
print(4 & 5) # 4
print(4 | 5) # 5
print( 4 ^ 5) # 1

'''
~ (Bitwise complement operator): 
Example: 
    While doing ~4,
    4: don't represent number 4 as
        4 2 1
        -----
        1 0 0
        Represent as how much bit size is used to represent Integer number. Like 32 bit's.
    
The Most Significant Bit (MSB) act as sign bit.
    0: Positive number.
    1: Negative number.
Positive number will be represented directly in the memory.
Negative number will be represented in 2's complement form.

How to find 1's complement:
    Interchange the bit's like 1 will be 0 and 0 will be 1. This is called 1's complement.

How to find 2's complement:
    After getting 1's complement add 1 in it.

Example:
~4:
First take number 4 in 32 bit's form and it is positive number so MSB will be 0.

4: 0000 0000 0000 0000 0000 0000 0000 0100
   ^
  MSB(It is 0 so it is positive number)

~4: 1111 1111 1111 1111 1111 1111 1111 1011 : We know the answer will be in minus
    ^
    MSB(It is 1 so it is negative number)

1's complement:
1111 1111 1111 1111 1111 1111 1111 1011 : ~4 (Here MSB is 1 so the answer will be in negative)
---------------------------------------
0000 0000 0000 0000 0000 0000 0000 0100 : 1's complement
---------------------------------------
                                      1 : Adding one to get 2's complement
---------------------------------------
0000 0000 0000 0000 0000 0000 0000 0101 : Answer is 5

Final answer is: -5
'''
print(~4) # -5

'''
0000 0000 0000 0000 0000 0000 0000 0101 : 5
---------------------------------------
1111 1111 1111 1111 1111 1111 1111 1010 : ~5 (Here MSB is 1 so the answer will be in negative)
---------------------------------------
0000 0000 0000 0000 0000 0000 0000 0101 : 1's complement
---------------------------------------
                                      1 : Adding one to get 2's complement
----------------------------------------
0000 0000 0000 0000 0000 0000 0000 0110 : -6
'''
print(~5) # -6

'''
~ -4:
-4: 1--- ---- ---- ---- ---- ---- ---- ----
    ^
   MSB(It is negative number so it will start from 1 and remaining will be 2's complement as it is negative number)

Here its bit tricky, the number is in negative form.

0000 0000 0000 0000 0000 0000 0000 0100 : 4 Positive four in bits
---------------------------------------
1111 1111 1111 1111 1111 1111 1111 1011 : 1's compliment
---------------------------------------
                                      1 : Adding one to get 2's complement
---------------------------------------
1111 1111 1111 1111 1111 1111 1111 1100 : -4

0000 0000 0000 0000 0000 0000 0000 0011 : ~ -4 i.e 3
'''
print(~-4) # 3
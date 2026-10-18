'''
How the below code works:
input('Enter two numbers: ') : On this line we are providing the string value like '10 20' i.e space separated.
input('Enter two numbers: ').split() : Because of split() function it splits the string based on space and convert it into list of
string i.e. ['10', '20'] so it becomes value1, value2 = [int(x) for x in ['10', '20']], then for loop iterates on this list of string
this string type we are converting to int type hence we are using int(x) then it becomes value1, value2 = [10, 20] this concept is called as list comprehension.
and then this value is assigned to the variables in sequence this concept is called as list unpacking.
'''
#How to read multiple values from the keyboard in a single line:
value1, value2 = [int(x) for x in input('Enter two numbers: ').split()] # i/p: 10 20
print('Sum is: ', value1 + value2)

value1, value2, value3 = [float(x) for x in input('Enter three floating point numbers by comma separated: ').split(',')] # i/p: 10.5, 20.5, 30.5
print('Sum is: ', value1 + value2 + value3)
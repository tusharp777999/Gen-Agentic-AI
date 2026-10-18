'''
raw_input() : It will always gives you input data in string form only. You have to convert the data explicitly.
input() : Based on provided value it will provide the data type. Like if you provide int data, it will consider as int, for float value
it will consider float based on provided value it will take the type of the data.

x = raw_input('Enter number: ')
print(type(x))
y = int(x)
print(type(y))
Note: raw_input(), input() this function belongs to Python 2.x with above behaviour.

In Python 3.x we will have only input() function but it provides only string value not based on input value.
'''
x = input('Enter data: ')
print(type(x))
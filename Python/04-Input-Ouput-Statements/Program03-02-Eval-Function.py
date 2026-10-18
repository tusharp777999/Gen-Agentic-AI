'''
eval(): The eval() function converts the input data based on provided data type.
It is alternative to type casting functions like int(), float(), str() etc. 
It is used to evaluate the string as a Python expression and returns the result. 
'''
data = eval(input('Enter a data: '))
print('Type of data is: ', type(data))
print('Data is: ', data)

#It can also be used to evaluate mathematical expressions:
data = eval('10 + 20')
print('Type of data is: ', type(data))
print('Data is: ', data)

data = eval('10 + 20 +30 / 3 // 2 * 5 ** 5')
print('Type of data is: ', type(data))
print('Data is: ', data)
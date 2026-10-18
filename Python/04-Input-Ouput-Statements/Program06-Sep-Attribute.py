'''
sep attribut: 
a, b, c, d = 10, 20, 30, 40
print('Values are: ',a, b, c, d)
output: Values are:  10 20 30 40
Here space is taken care by print() function. We can also use sep parameter to change the space to any other character.
Default value of sep parameter is space. We can change it to any other character like comma, hyphen, etc.
Example:
a, b, c, d = 10, 20, 30, 40
print('Values are: ',a, b, c, d, sep='-')
output: Values are:  10-20-30-40
'''
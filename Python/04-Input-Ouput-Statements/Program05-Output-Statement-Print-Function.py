'''
print() : It is used to print the output on the console.
If we used it without any argument then it will print a new line on the console.
We can also use escape sequences like \n, \t, \r etc. to print the output in a specific format.
Example: 
print('Hello \n World')
Output:
Hello
World

print('Hello \t World')
Output: 
Hello    World

print('Hello' +  'World')
Output: 
HelloWorld

print(10 * 'Hello') or print('Hello' * 10)
Output: 
HelloHelloHelloHelloHelloHelloHelloHelloHelloHello

We can print multiple values by separating them with a comma. It will print the values with a space in between.
Example:
a, b, c = 10, 20, 30
print('Values are: ',a, b, c)
output: Values are:  10 20 30
Here space is taken care by print() function. We can also use sep parameter to change the space to any other character.
'''
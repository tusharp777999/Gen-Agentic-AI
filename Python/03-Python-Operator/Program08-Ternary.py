'''
Unary Operator: If operator operates on single operand is called Unary Operator.
Example: ~a, +a, -a, ... etc

Binary Opearator: If operator operates on two operand is called Binary Operator.
Example: a + b, a - b, a * b, ... etc

Ternary Operator: If operator operates on three operand is called Ternary Operator.
'''
x = 10
y = 20
z = 30 if x > y else 40
print(z) # 40

#Read two integer numbers from keyboard and print minimum value.
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
result = first_number if first_number < second_number else second_number
print("Minimum value: ", result)

#Nesting of Ternart Operators: This is proper way
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
third_number = int(input('Enter third number: '))
result = first_number if (first_number < second_number and first_number < third_number) else second_number if second_number < third_number else third_number
print('Minimum value: ', result)

#For nesting example if we tried to use other way it will give us wrong output.
#Provide input as first_number: 5, second_number: 35 and third_number: 30
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
third_number = int(input('Enter third number: '))
result = first_number if (first_number < second_number < third_number) else second_number if second_number < third_number else third_number
print('Minimum value: ', result)

#Nesting of Ternart Operators: This is proper way
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
third_number = int(input('Enter third number: '))
result = first_number if (first_number > second_number and first_number > third_number) else second_number if second_number > third_number else third_number
print('Maximum value: ', result)

#If both numbers are equal print equal.
#If first number is smaller print smaller.
#If first number is greater print greater.
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
result = 'both are equal' if first_number == second_number else 'first number smaller than second number' if first_number < second_number else 'first number is greater than second number'
print(result)
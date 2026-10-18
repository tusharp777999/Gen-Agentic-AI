x = input('Enter first value: ')
y = input('Enter second value: ')
i = int(x)
j = int(y)
print('The sum is: ', i + j)

#Simplified version(Recommended.)
x = int(input('Enter first value: '))
y = int(input('Enter second value: '))
print('The sum is: ', x + y)

#Another simplified version(Not recommended.)
print('The sum is: ', int(input('Enter first value: ')) + int(input('Enter second value: ')))

#Write a program to read employee data from the keyboard and print the data.

employeeID = int(input('Enter Employee ID: '))
employeeName = input('Enter Employee Name: ')
employeeSalary = float(input('Enter Employee Salary: '))
employeeAddress = input('Enter Employee Address: ')
maritalStatus = bool(input('Is Employee Married?[True | False]: '))

print('Please confirm your provided information: ')
print('Employee ID: ', employeeID)
print('Employee Name: ', employeeName)
print('Employee Salary: ', employeeSalary)
print('Employee Address: ', employeeAddress)
print('Employee Married? ', maritalStatus)

'''
maritalStatus = bool(input('Is Employee Married?[True | False]: ')) 
For this even if you provide value as False but during result print it will always print true.
The reason is bool() this type casting function always return 'True' if provided string is non-empty so False is considered as 'False'
which is a non-empty string, hence the result even for provided value 'False' is 'True'.
Instead of bool() use eval() function. for 'True' it will take True and for 'False' it will take False.
'''
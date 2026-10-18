'''
Commnand Line Arguments in Python
Command line arguments are the arguments passed to the script when it is executed.
Example: python script.py arg1 arg2 arg3
These arguments can be accessed using the sys module in Python.
It contains the argv variable which gives the list of command line arguments passed to the script.
If we try to get the argv[0], it will give the name of the script. The rest of the arguments can be accessed using argv[1], argv[2] and so on.
Example: python script.py arg1 arg2 arg3
argv[0] = script.py
argv[1] = arg1
argv[2] = arg2
argv[3] = arg3
'''
from sys import argv
print(type(argv))

print(argv)
print('Name of script is: ', argv[0])
print('First argument is: ', argv[1])
print('Second argument is: ', argv[2])
print('Third argument is: ', argv[3])

print('Total number of arguments passed: ', len(argv))
print('The list of arguments passed: ', argv)
print('The command lines arguments are: ')
for i in argv:
    print(i)

#Write a program to print sum of given numbers provided as command line arguments.
args = argv[1:]  # Exclude the script name from the arguments
sum = 0
for arg in args:
    sum += int(arg)  # Convert each argument to an integer and add to sum
print('The sum of the given numbers is: ', sum)

#Write a program for file manager application.
file1 = open('file1.txt') # file1 = open(argv[1])
file2 = open('file2.txt') # file2 = open(argv[2])
file3 = open('output.txt', 'w') # file3 = open(argv[3], 'w')
for line in file1:
    file3.write(line)
for line in file2:
    file3.write(line)
file1.close()
file2.close()
file3.close()

'''
case 1: python file.py sunny leone
If our command line argument is space sperated then it will be treated as two different arguments.
If we want to consider it as a single argument then we have to use double quotes. but not single quotes.
python file.py "sunny leone"
output: sunny leone

python file.py 'sunny leone'
output: 'sunny
        leone'
If you use single quotes then it will be treated as two different arguments. like this: 'sunny and leone'.

case 2: python file.py 10 20
print(argv[1] + argv[2]) 
output: 1020
print(int(argv[1]) + int(argv[2]))
output: 30

case 3: python file.py 10 20
print(argv[100])
output: IndexError: list index out of range.
'''

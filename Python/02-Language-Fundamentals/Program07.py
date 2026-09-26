'''
str: allowed values: any sequence of characters enclosed in single or double quotes. It cannot be combination of both single and double quotes.
recommended: use single quotes.
'''

a = 'Hello, World'
print(a)#To print the value of a
print(type(a)) #To print the type of a

b = "Python is a programming language"
print(b) #To print the value of b
print(type(b)) #To print the type of b

c = 'a';
print(c) #To print the value of c
print(type(c)) #To print the type of c
#Note: In Python, there is no separate character data type. A single character is simply a string.

# d = 'Hello'
#       to
#        World'
# print(d) #To print the value of d
#If you try to run the above code, it will give a syntax error because the string is not properly enclosed in quotes. You cannot have a line break in a string unless you use triple quotes or escape the newline character.

d = '''Hello
            to
                World'''
print(d) #To print the value of d
print(type(d)) #To print the type of d

e = 'Hello, "My" World'
print(e) #To print the value of e
print(type(e)) #To print the type of e
#If we want to use double quotes inside a string that is enclosed in single quotes.

f = "Hello, 'My' World";
print(f) #To print the value of f
print(type(f)) #To print the type of f
#If we want to use single quotes inside a string that is enclosed in double quotes.

#Triple Quote:
g = '''Hello, "My" World 'India' '''
print(g) #To print the value of g
print(type(g)) #To print the type of g
#If we want to use both single and double quotes inside a string, we can use triple quotes to enclose the string.

#Indexing:
#Positive Indexing: The index of the first character is 0, the index of the second character is 1, and so on.
#Negative Indexing: The index of the last character is -1, the index of the second last character is -2, and so on.
data = "Hello"
print(data[0]) #To print the first character of the string
print(data[1]) #To print the second character of the string
#print(data[100]) #To print the 100th character of the string but it will give an error because the string has only 5 characters. The index starts from 0, so the last character is at index 4.
print(data[-1]) #To print the last character of the string

#Slice Operator: string[start:end]
h = 'abcdefghijklmnopqrstuvwxyz';
print(h[0:5]) #To print the first 5 characters of the string here end index is exclusive, so it will print characters from index 0 to 4.
print(h[4:]) #To print the characters from index 4 to the end of the string
print(h[:4]) #To print the characters from the beginning of the string to index 3
print(h[:]) #To print the entire string
print(h[5:1000]) #To print the characters from index 5 to the end of the string, even if the end index is greater than the length of the string, it will not give an error and will print till the end of the string.
print(h[5:3]) #To print the characters from index 5 to index 3, but it will not print anything because the start index is greater than the end index. The slice operator will return an empty string in this case.
print(h[5:-1]) #To print the characters from index 5 to the second last character of the string

i = 'Tushar';
output = i[0].upper() + i[1:];
print(output) #To print the string with the first character in uppercase and the rest in lowercase

output = i[0:len(i)-1] + i[-1].upper();
print(output) #To print the string with the last character in uppercase and the rest in lowercase
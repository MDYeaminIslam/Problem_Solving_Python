"""
Printing string pattern here:

p 
p y
p y t
p y t h
p y t h o
p y t h o n

"""

string = str(input("Enter the string:"))
length = len(string)
for row in range(length):
    for col in range(row+1):
        print(string[col], end=" ")
    print()
    
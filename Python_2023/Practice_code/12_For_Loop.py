thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)

print("________________________________________")
#Even strings are iterable objects, they contain a sequence of characters:

string = "This is a string and we !love you"
for x in string:
    print(x) #first of all value from string store into x and we will print those using x variable

print("________________________________________")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("________________________________________")

#print value using range function
for x in range(2,11,2): #here 2 is starting point and 8 is ending point and if we add another value that will represent increment value
    print(x)
    
print("________________________________________")

one = ["apple","orange","kola"]
two = ["banana","mango","cherry"]

for x in one:
    for y in two:
        print(x,y)
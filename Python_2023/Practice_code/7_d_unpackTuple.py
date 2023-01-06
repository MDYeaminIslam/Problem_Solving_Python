#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

tupelvalue = ("Mango","Apple","Pineapple")
(x,y,z) = tupelvalue
print(x)
print(y)
print(z)

#here "*" this asteric sign will keep rest of the value

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
print(type(red))

#joining two tuple
tupel1 = (12,645,23,46)
tuple2 = (645,32,538,634347)
result = tupel1+tuple2
print(result)
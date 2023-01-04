#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#But there is a workaround.
#You can convert the tuple into a list, change the list, and convert the list back into a tuple.

#adding value in the tuple
tuple_value = ("Apple","Banana","lichi","Mango")
list_value = list(tuple_value)
list_value[1] = "another_fruit"
tuple_value = tuple(list_value)
print(tuple_value)

#we can add value in existing tuple with the help of another tuple
newTuple = ("Nice","Looking","Car")
anotherOne = ("You","have")
newTuple += anotherOne
print(newTuple)

#removing item from the tuple with the help of List
xTuple = (1,453,12,76,34,7876,34)
yList = 



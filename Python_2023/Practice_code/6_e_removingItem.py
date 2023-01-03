#The remove() method removes the specified item.we have to give specific value in the function
thislist = ["apple", "banana", "cherry"]
thislist.remove("cherry")
print(thislist)

#using pop function we can delet value from the list. here we'll give position value.
thislist = ["apple", "banana", "cherry","Jackfruit","lichi","orange"]
thislist.pop(0)
print(thislist)

#only pop function will remove the last item of the list
thislist = ["apple", "banana", "cherry","Jackfruit","lichi","orange"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:
thislist = ["hello","hiii","apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.
#thislist = ["apple", "banana", "cherry"]
#del thislist

#The clear() method empties the list. The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


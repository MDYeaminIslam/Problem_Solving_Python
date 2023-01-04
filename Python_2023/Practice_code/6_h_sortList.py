#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#sorting the digits
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sorting in reverse
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

#Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
#reverse will simply change the sequence of present order. doesn't change according to first letter.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy the list
newlist = [1,856,23,565,324,545]
finalList = newlist.copy()
print(finalList)
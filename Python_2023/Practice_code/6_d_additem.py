#adding value in the list
#To add an item to the end of the list, use the append() method:
thislist = ["apple","juice","price"]
thislist.append("hike")
print(thislist)

#extend function merge two list and make single list
listone = ["one","two","three"]
listtwo = ["four","five","six"]
listone.extend(listtwo) #here two list add together and put value in listone list
print(listone)

#we can add tuple,set,dictionary with a list using extend

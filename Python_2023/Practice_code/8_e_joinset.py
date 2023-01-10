#The union() method returns a new set with all items from both sets:
set1 = {1,23,655,34365,344}
set2 = {3,43544,2335,7563,42}
set3 = set1.union(set2)
print(set3)
#we have to union two set and put it into another set than it'll work.
#Note: Both union() and update() will exclude any duplicate items.

#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple","banana","jackfruit","orange"}
y = {"kola","banana","apple","nothing","happened"}
x.intersection_update(y)
print(x)

#The intersection() method will return a new set,
#that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

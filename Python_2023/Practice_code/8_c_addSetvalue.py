#Once a set is created, you cannot change its items, but you can add new items.

thisset = {"Orange","apple","Banana"}
print(thisset)
thisset.add("Kola")
print(thisset)

#if we want to add new set than use update() fundtion
one = {1,2,4565,76534}
two = {809,234,57,2343}
one.update(two)
print(one)

#The object in the update() method does not have to be a set,
#it can be any iterable object (tuples, lists, dictionaries etc.).
oneset = {"One","two","three"}
twoset = ["One1","two2","three3"]
oneset.update(twoset)
print(oneset)

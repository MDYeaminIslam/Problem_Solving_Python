#The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#we have to give key value in the pop function
thisdict.pop("brand")
print(thisdict)

#here popitem will remove last inserted item from the dictionary
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2.popitem()
print(thisdict2)

#The del keyword removes the item with the specified key name:
thisdict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict3["model"]
print(thisdict3)
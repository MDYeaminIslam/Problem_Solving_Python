#There are ways to make a copy, one way is to use the built-in Dictionary method copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
newdict = dict(thisdict)
print(newdict)
print(type(newdict))

#another way is to copy is given below
mydict = thisdict.copy()
print(mydict)
print(type(mydict))
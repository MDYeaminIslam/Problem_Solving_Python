#You can access the items of a dictionary by referring to its key name, inside square brackets:
dicOne = {
    "color":"White",
    "BrandName":"Hayabusa",
    "Mielages":120
}
print(dicOne)
print(dicOne["color"])
#There is also a method called get() that will give you the same result:
print(dicOne.get("BrandName"))

#The keys() method will return a list of all the keys in the dictionary.
print(dicOne.keys())

car = {
    "Brand":"Ford",
    "model":"Mustang",
    "year":1998
}
y = car.keys()
print(y) #Before adding new key

car["Topspeed"] = 450
print(y) #after adding new key

#The values() method will return a list of all the values in the dictionary.
print(car.values())
#The returned list is a view of the items of the dictionary,
#meaning that any changes done to the dictionary will be reflected in the items list.
val = car.items()
print(val)

#we can change item using [] this bracket
dictionary = {
    "color":"White",
    "BrandName":"Hayabusa",
    "ParentsCompany":"Honda"
}
dictionary["color"] = "Black"
print(dictionary)

#adding value using update method
dictionary.update({"Mileage":120})
print(dictionary) 
#change item in the list
listValue = ["Apple","Banana","Kola","JackFruit","Pineapple"]
listValue[1] = "Potato"
print(listValue)

#chang value using slice
listValue[2:4] = ["Tomato","Ladyfinger"]
print(listValue)

#using insert function.insert(position,value)
valuelist = ["value","has"]
valuelist.insert(2,"rotten")
print(valuelist)
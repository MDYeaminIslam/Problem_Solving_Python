#this is the formula of using python comprehension
#newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = [x for x in fruits if "a" in x]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
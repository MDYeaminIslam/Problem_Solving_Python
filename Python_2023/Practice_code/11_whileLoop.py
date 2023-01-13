value = 1
while value < 10:
    print(value)
    value +=1

print("--------------------")
#using break statement
i = 1
while i<5:
    print(i)
    if i==3:
        break
    i+=1

print("--------------------")
#using continue statement
j = 0
while j<10:
    j+=1
    if j==5:
        continue
    print(j)
    
    
'''
printing pattern like this:
* 
* * 
* * * 
* * * * 
* * * * *

'''

n = int(input("Enter the number of rows needed: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print() #this will lead code to next line
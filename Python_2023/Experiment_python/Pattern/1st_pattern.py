
"""
printing pattern like this:
1
1 2
1 2 3
1 2 3 4

if we change the value of in print function j to i than pattern look like this.
1
2 2
3 3 3
4 4 4 4
        
"""
n = int(input("Enter the number of rows needed: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print() #this will lead code to next line
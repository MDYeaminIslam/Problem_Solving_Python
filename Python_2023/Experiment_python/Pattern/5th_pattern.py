"""
printing pattern like this:
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
    
"""
n = int(input("Enter the number of rows needed: "))
for i in range(n):
    for j in range(i,-1,-1):
        print(n-j, end=" ")
    print() #this will lead code to next line

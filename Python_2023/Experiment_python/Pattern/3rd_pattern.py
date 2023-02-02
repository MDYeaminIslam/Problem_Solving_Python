"""
printing pattern like this:
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
    
"""
n = int(input("Enter the number of rows needed: "))
for i in range(n):
    for j in range(i+1):
        print(n-i, end=" ")
    print() #this will lead code to next line

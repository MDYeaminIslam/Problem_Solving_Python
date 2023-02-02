"""
printing pattern like this:
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
    
"""
n = int(input("Enter the number of rows needed: "))
for i in range(n):
    for j in range(i+1):
        print(n-j, end=" ")
    print() #this will lead code to next line

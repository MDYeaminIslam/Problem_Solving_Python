"""
printing pattern like this:
      1 
    1 2
  1 2 3
1 2 3 4
"""
n = int(input("Enter the number of rows needed: "))
for i in range(n):
    for k in range(n-i-1):
        print(" ", end=" ")
    for j in range(i+1):
        print(j+1, end=" ")
    print() #this will lead code to next line

"""
Printing string pattern here:

6 6 6 6 6 6 
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

"""

n = int(input("Enter the number of rows needed: "))

for row in range(n,0,-1):
    for col in range(1,row+1):
        print(row, end=" ")
    print()
    
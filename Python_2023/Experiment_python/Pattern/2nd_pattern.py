"""
printing pattern like this:
1
1 2
1 2 3
1 2 3 4

"""

value = int(input("Enter the number of rows needed:"))

for i in range(value):
    for j in range(i, -1, -1):
        print(j+1, end=" ")
    print()


#printing Floyd's Triangle
'''
pattern look like this
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''
n = int(input("Enter the number of rows needed: "))
num=1
for row in range(n):
    for col in range(row+1):
        print(num, end=" ")
        num=num+1
    print()

'''
printing pattern like this using while loop:
* 
* * 
* * * 
* * * * 


'''

num = int(input("Enter the number of rows:"))
row = 0
while row < num:
    star = row + 1
    while star > 0:
        print("*", end=" ")
        star -= 1
    row = row + 1
    print()
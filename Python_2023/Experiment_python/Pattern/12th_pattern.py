'''
printing pattern like this:
* 
* *
*   *
*     *
*       *
*         *
*           *
*             *
*               *
* * * * * * * * * *
'''

n = int(input("Enter the number of rows needed: "))
for row in range(n):
    for col in range(row+1):
        if col==0 or row==(n-1) or row==col:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print() #this will lead code to next line
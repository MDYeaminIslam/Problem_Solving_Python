'''
printing pattern like this

   *   
  * *  
 *   * 
*******



'''

value = int(input("Enter the number of rows:"))

for row in range(1, value+1):
    for col in range(1, 2*value):
        if row+col==value+1 or col-row==value-1 or row==value:
            print("*", end="")
        else:
            print(end=" ")
    print()
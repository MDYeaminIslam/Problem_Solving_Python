'''
Create a pattern like this

  *   
 *  *
*    *
 *  *
  *

'''
#this one is 5 rows and 5 columns
for row in range(5):
    for col in range(5):
        if row + col == 2 or col-row==2 or row-col==2 or row+col==6:
            print("*", end=" ")
        else:
            print(end=" ")
    print() #this is for printing new line
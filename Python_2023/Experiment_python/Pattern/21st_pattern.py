'''
Create a pattern like this

   *    
  * *   
 * * *  
* * * * 


'''

num = int(input("Enter the number of rows:"))
row = 0
while row < num:
    space = num - row - 1 #this is the number of spaces we want in each row
    #this loop is for printing spaces
    while space > 0:
        print(end=" ")
        space = space - 1
    #ths loop is for printing stars
    star = row + 1
    while star > 0:
        print("*", end=" ")
        star = star - 1
    row = row + 1
    print() #this is for printing new line
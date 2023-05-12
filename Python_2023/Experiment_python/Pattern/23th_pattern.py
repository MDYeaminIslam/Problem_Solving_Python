'''
creating this pattern:



'''

num = int(input("Enter the number of rows: "))
n_list = [[0 for x in range(num)] for y in range(num)]

#pattern starting from 1
n=1
#defining low and high value
low = 0
high = num-1
count = int((num+1)/2) #if we want to print 5 rows then we need to print 3 squares or 3 times

for i in range(count):
    #printing row = 0 and column = 0 to 4
    for j in range(low,high+1):
        n_list[i][j]=n
        n=n+1 #first n =1 and increasing the value of n to get next value
    
    #printing row = 1 to 4 and column = 4 and here we skip row = 0 and colmn = 4 because we already printed it in above loop
    for j in range(low+1,high+1):
        n_list[j][high]=n
        n=n+1
        
    #printing row = 4 and column = 3 to 0 and here we skip row = 4 and column = 4 because we already printed it in above loop
    for j in range(high-1,low-1,-1):
        n_list[high][j]=n
        n=n+1
    
    #printing row = 3 to 1 and column = 0 and here we skip (row = 4 and column = 0) and (row = 0 and column = 0) because we already printed it in above loop
    for j in range(high-1,low,-1):
        n_list[j][low]=n
        n=n+1
    #these two will move on to next square
    low = low+1
    high = high-1

#this code for converting the nested list into a matrix pattern and printing final output
for i in range(num):
    for j in range(num):
        print(n_list[i][j],end="\t")
    print()
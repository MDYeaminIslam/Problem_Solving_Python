#printing amstrong number between 1 to 1000
#Amstrong number is a number that is equal to the sum of nth power of its digits.

for i in range(1001):
    num=i
    result=0
    power=len(str(i))
    while(i!=0):
        digit = i%10
        result=result+digit**power
        i=i//10
    if num==result:
        print(f"{num} is an Armstrong number")

        
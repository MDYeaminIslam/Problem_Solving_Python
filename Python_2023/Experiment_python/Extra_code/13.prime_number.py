#checking if a number is prime or not

lower = int(input("Enter lower interval range: "))
upper = int(input("Enter upper interval range: "))

for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
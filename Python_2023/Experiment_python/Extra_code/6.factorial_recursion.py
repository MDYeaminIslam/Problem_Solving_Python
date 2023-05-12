#Here we will find the factorial of a number using recursion

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    



n = int(input("Enter a number:"))
result = fact(n)
print(f"Factorial of {n} is {result}")
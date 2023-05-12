first_val = int(input("Enter the first number: "))
second_val = int(input("Enter the second number: "))
print(f"Before the swap, the first value is: {first_val} and the second value is: {second_val}")
first_val = first_val + second_val
second_val = first_val - second_val
first_val = first_val - second_val
print(f"After the swap, the first value is: {first_val} and the second value is: {second_val}")

'''
we can swap this way also
x = 12
y = 33
print('x, y', x, y)
#swap these two
x, y = y, x
print('x, y', x, y)


'''
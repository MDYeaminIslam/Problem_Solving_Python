#Perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.

#perfect number is a positive integer that is equal to the half of the sum of its proper positive divisors.

num = int(input("Enter the number: "))
result = 0

for i in range(1, num):
    if (num%i)==0:
        result = result + i
if result == num:
    print(f"{num} is a perfect")
else:
    print(f"{num} is not a perfect")
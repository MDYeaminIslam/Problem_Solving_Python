valueA = int(input("Enter the value of A: "))
valueB = int(input("Enter the value of B: "))

valueA = valueA + valueB
#storing value of A in B
valueB = valueA - valueB
#storing value of B in A
valueA = valueA - valueB

print("After swaping")
print(f"The value of A is: {valueA}")
print(f"The value of B is: {valueB}")
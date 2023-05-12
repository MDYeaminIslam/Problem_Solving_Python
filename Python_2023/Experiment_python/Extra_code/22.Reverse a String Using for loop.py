#Reverse a String Using for loop

#define a function
def reverseString(string):
    reverse_str = ""
    for i in string:
        reverse_str = i + reverse_str
        #here loop will take a char and concatinate it with reverse_str
        #this way first latter of taken string will be added at the end of reverse_str
    print("Reverse string is :",reverse_str)

string = str(input("Enter a string:"))
print("Original string is :",string)
reverseString(string)
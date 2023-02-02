"""Write A Python Program To Take Age From The User To Check Whether User Able To Participate In Voting Or Not. If Age Is Less Than 18 Then It Don’t Allow To Participation. And Show, After How Much Year A Person Will Be Able To Participate:

Expected Result if user input 10 year then:
Sorry! You cannot participate in voting, you will be able to participate after 8 year
"""

user_age = int(input("Enter your age: "))

if user_age>=18:
    print("You can participate in voting")
    
elif user_age<=0:
    print("Age can't be negetive or zero")
    
else:
    print(f"Sorry! You cannot participate in voting, you will be able to participate after {18-user_age} year")
"""Write A Python Program To Take Marks From The User To Check Whether User Able To Admission In College Or Not. If Marks Is Less Than 60 Then It Don’t Allow To Take Admission. 

Expected Result if user input 50 year then:
Sorry! You cannot take admission, you need 10 numbers more to take admission
"""

user_marks = int(input("Enter your marks: "))

if user_marks>= 60:
    print(("You can take admission in college"))
else:
    print(f"Sorry! You cannot take admission, you need {60-user_marks} numbers more to take admission")
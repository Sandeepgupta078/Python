# a1 = int(input("Enter the Number:"))
# a2 = int(input("Enter the Number:"))
# a3 = int(input("Enter the Number:"))
# a4 = int(input("Enter the Number:"))

# if(a1 > a2 and a1 > a3 and a1 > a4):
#     print("greatest number is:",a1)

# elif(a2 > a1 and a2 > a3 and a2 > a4):
#     print("greatest number is:",a2)

# elif(a3 > a1 and a3 > a2 and a3 > a4):
#     print("greatest number is:",a3)

# else:
#     print("greatest number is:",a4)

# ----------------------------------------------------------------------------------------------------------------------------

# Q.2 - Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# sub1 = int(input("Enter the marks of subject 1: "))
# sub2 = int(input("Enter the marks of subject 2: "))
# sub3 = int(input("Enter the marks of subject 3: "))

# total = sub1 + sub2 + sub3
# percentage = (total/300)*100

# if(sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and percentage >= 40):
#     print("Congratulations! You have passed the exam, your total score is: ", percentage)

# else:
#     print("Sorry! You have failed the exam, your total score is: ", percentage)

# ----------------------------------------------------------------------------------------------------------------------------

# Q.3 - A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

# m1 = "Make a lot of money"
# m2 = "buy now"
# m3 = "subscribe this"
# m4 = "click this"

# comment = input("Enter your comment: ")

# if(m1 in comment or m2 in comment or m3 in comment or m4 in comment):
#     print("This is a spam comment")

# else:
#     print("This is not a spam comment")

# ----------------------------------------------------------------------------------------------------------------------------
# Write a program to find whether a given username contains less than 10
# characters or not.

# username = input("Enter your username: ")
# if(len(username) < 10):
#     print("Username contains less than 10 characters")

# else:
#     print("All good! ")

# ----------------------------------------------------------------------------------------------------------------------------

# q.5 - Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter your marks: "))

if(marks >= 90 and marks <= 100):
    grade = "Ex"

elif(marks >= 80 and marks < 90):
    grade = "A"

elif(marks >= 70 and marks < 80):
    grade = "B"

elif(marks >= 60 and marks < 70):
    grade = "C"

elif(marks >= 50 and marks < 60):
    grade = "D"

else:
    grade = "F"

print("Your grade is: ", grade)

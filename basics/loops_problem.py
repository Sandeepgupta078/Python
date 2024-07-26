# Write a program to print multiplication table of a given number using for loop.
# n = input("Enter a number: ")

# for i in range(1, 11):
#     print (f"{n} x {i} = {int(n) * i}")


# ---------------------- End of Problem 1 ----------------------

# Problem 2:Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S. 
# l = [“Harry”, “Soham”, “Sachin”, “Rahul”]

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for(name) in l:
#     if name.startswith("S"):
#         print(f"Hello {name}")

# ---------------------- End of Problem 2 ----------------------

# Problem 3: Attempt problem 1 using while loop.
# n = input("Enter a number: ")
# i = 1
# while (i < 11):
#     print (f"{n} x {i} = {int(n) * i}")
#     i = i + 1

# ---------------------- End of Problem 3 ----------------------

# n = int(input("Enter a number: "))

# for i in range(2,n):
#     if (n % i) == 0:
#         print("Not a prime number")
#         break

# else:
#     print("Prime number")

# ---------------------- End of Problem 4 ----------------------
# Write a program to find the sum of first n natural numbers using while loop.

# n = int(input("Enter a number: "))
# i = 0
# sum = 0
# while(i<=n):
#     sum += i
#     i += 1

# print(f"Sum of first {n} natural numbers is {sum}")

# ---------------------- End of Problem 5 ----------------------
# Write a program to calculate the factorial of a given number using for loop.
# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial = factorial * i
    
# print(f"Factorial of {n} is {factorial}")

# ---------------------- End of Problem 6 ----------------------
# Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3

# n = int(input("Enter a number: "))

# for i in range(1,n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print()

# ---------------------- End of Problem 7 ----------------------
# Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print("*"*i)
#     print()

# ---------------------- End of Problem 8 ----------------------
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if(i == 1 or i == n):
        print("*"*n)

    else:
        print("*" + " "*(n-2) + "*")

    print("")
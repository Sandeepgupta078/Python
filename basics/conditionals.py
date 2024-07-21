a = int(input("Enter your age: "))

if(a >= 18):
    print("You are above the age of consent")
    print("Good for you!, you can vote")

elif(a < 0):
    print("You are entering an Invalid age, try again!")

else:
    print("You are below the age of consent")
    print("Sorry, you can't vote yet")
# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

words = {
    "pankha": "fan",
    "dabba": "box",
    "raja": "king",
    "vaidya": "doctor",
}
# word = input("Enter the Hindi word which meaning you want to know: ")
# print(words[word])

# Write a program to input eight numbers from the user and display all the unique
# numbers (once).
# a = set()
# n = int(input("Enter the number: "))
# a.add(n)
# n = int(input("Enter the number: "))
# a.add(n)
# n = int(input("Enter the number: "))
# a.add(n)
# n = int(input("Enter the number: "))
# a.add(n)
# n = int(input("Enter the number: "))
# a.add(n)
# n = int(input("Enter the number: "))
# a.add(n)
# n = int(input("Enter the number: "))
# a.add(n)
# n = int(input("Enter the number: "))
# a.add(n)

# print(a) #prints the unique numbers

# Q.3 - What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)                     
s.add('20') # length of s after these operations?
print(len(s)) #prints 2

# Because 20 and 20.0 are same but '20' is different from 20 and 20.0


# Q.4 - Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

dictionary = {}
name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dictionary.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dictionary.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dictionary.update({name: language})

name = input("Enter your name: ")
language = input("Enter your favorite language: ")
dictionary.update({name: language})

print(dictionary) #prints the dictionary
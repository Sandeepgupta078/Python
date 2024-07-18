# Write a python program to display a user entered name followed by Good
# Afternoon using input () function.

# name = input("Enter your name: ")
# print(f"Good Afternoon, {name}!")


# Write a program to fill in a letter template given below with name and date.
letter = '''Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", "Sandeep").replace("<|Date|>", "7 Nov 2024"))
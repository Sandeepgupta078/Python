# import os

# def print_directory_contents(path):
#     for item in os.listdir(path):
#         print(item)

# # Example usage
# directory_path = "/Users/sandeepgupta/Code/Python"
# print_directory_contents(directory_path)

import os

# select the directory path which you want to search
directory_path = "/Users/sandeepgupta/Code/Python"

# use the os module to list the directory contents
contents = os.listdir(directory_path)

# print the contents
print(contents)
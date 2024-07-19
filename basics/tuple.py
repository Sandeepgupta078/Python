a = () #empty tuple

a = (1) #integer

print(type(a))

a = (1,) #tuple with 1 element
a = (1, 2, 3, 4, 5) #tuple with 5 elements
print(type(a))


# methods in tuple
tuple = (1, 2, 3, 4, 5, "Sandeep", "75", "Gupta", 75, 75.0, 75.0)

count = tuple.count("Sandeep")
print(count)

index = tuple.index("Sandeep")
print(index)

concatenation = tuple + (1, 2, 3, 4, 5)
print(concatenation)
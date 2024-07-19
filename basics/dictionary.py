# data = {} #empty dictionary

data = {
    "sandeep":90,
    "Sandy": 80,
    "kavita": 70,
    90:"Gupta",
}

# print(data)
# print(type(data)) #dict

# methods in dictionary
# print (data.keys())
# print(data.values())

# data.update({"sandeep": 95, "Renuka": 85})
# print(data)


# the diffrence b/w get and [] is that get will return None if key is not present but [] will throw error
# if key present then both will return the value
# print(data.get("sandeep2")) #prints None if key is not present
# print(data["sandeep2"]) #throws error if key is not present

print(data.pop("sandeep")) #removes the key and returns the value
print(data) #prints the updated dictionary

print(data.popitem()) #removes the last key-value pair and returns the key-value pair
print(data) #prints the updated dictionary
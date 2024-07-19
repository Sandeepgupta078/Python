e = set() # empty sets
# e = {} #empty dictionary
# print(type(e))

e = {1,4,5,5,5,7,7,7,6}
print(e) #prints only unique elements

# methods in sets
e.add(8)
print(e)

e.update([8,9,10])
print(e) #prints the updated set

e.remove(10)
print(e) #prints the updated set

#e.remove(10) #throws error if element is not present
e.discard(10) #does not throw error if element is not present
#print(e) #prints the updated set

e.pop() #removes the first element
print(e) #prints the updated set

#e.clear() #clears the set
#print(e) #prints the updated set

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# union
print(s1.union(s2)) #prints the union of two sets

print(s1 | s2) #prints the union of two sets

# intersection
print(s1.intersection(s2)) #prints the intersection of two sets

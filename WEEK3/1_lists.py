shoppingList = ["bread", "coffee", "jam", "milk", "cookies"]
print("Shopping list:", shoppingList)

for item in shoppingList:
    print(item)
    
# Manipulation

shoppingList.append("curd")
print(shoppingList);

print(shoppingList[1]); # 0 indexed
print(shoppingList[-1]); # last item
print(shoppingList[2]);

shoppingList.insert(0, "butter") # index, object
print(shoppingList)

shoppingList.insert(10, "chips") # index, object
print(shoppingList)

ages = [12,23,45,18,78,25,56,35,24,20,67,89 ,25]
print(ages.count(25))

print(len(ages)) # length

# Operations

ages.sort() # accending
print(ages)

ages.reverse()
print(ages)

students = ["naveen", "naman", "ojas", "manish", "ojasvi"]
students.sort()
print(students)
students.insert(0, "ayush")
print(students)\
    
# Slicing --> list_name[startIdx: endIdx+1]

slice1 = students[1:4]
print(slice1)

slice2 = students[:] # default start is 0 ans default end is length
print(slice2)

slice3 = students[1:] 
print(slice3)

slice3 = students[:4] 
print(slice3)
iceCreamFlavours = ("chocolate", "vanilla", "strawberry", "butterscotch", "oreo", "choco chips")

print(iceCreamFlavours)
print(iceCreamFlavours[2])
print(iceCreamFlavours[4])

# iceCreamFlavours[2] = "black current"  --> error, doesn't allow modification

# iceCreamFlavours[6] = "black current" --> error, doesn't allow addition

# del iceCreamFlavours("vanilla") --> error, can't delete

# TUPLES ARE IMMUTABLE
del iceCreamFlavours # deletes the flavour
# print(iceCreamFlavours)

toy = (1,2,3,4)
toy = (1,2,3,4,2,3,1,4) # earlier toy is destroyed this is new tuple
print(len(toy))
print(toy.count(2))
print(toy.index(2)) # 1st index from the left
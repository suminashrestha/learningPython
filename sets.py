# Sets -> collection of unordered items
# -->each element in the set must be unique and immutable

# collection = {1, 2, 3, 4, 4, "hi", "hi", 4}  # ignores duplicate items
# print(collection)
# print(type(collection))

# empty set  eg.1
newset = set()

# methods:
newset.add(1)  # adds an element
newset.add(2)
newset.add(2)
newset.add(3)
newset.remove(2)  # removes the element
newset.add("lalitpur")
newset.add((3, 4, 5))
# newset.add([5, 6, 7])  --> error , unhashable type list
# print(len(newset))
# # newset.clear() #empties the set
# print(newset.pop())  # removes a random value
# print(newset)

# eg 2
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))  # combines both set values and returns new
print(set1.intersection(set2))  # combines common values and returns new

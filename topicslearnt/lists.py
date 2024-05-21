# Lists :  denoted by []
# marks = [33, 44, 67, 89, 40]  # marks[0],marks[1]...
# student = ["Sumi", 22, "lalitpur"]  # elements of different types
# student[0] = "Sumina"  # allowed in python lists but not in string
# print(student)
# print(len(student))

# # slicing in lists
# # list_name[starting_idx:ending_idx]  --> ending idx in not included
# print(marks[2:4])
# print(marks[:4])
# print(marks[1:])
# print(marks[-4:-1])

# List methods
list = [2, 1, 3, 6]
list.append(4)  # adds one element at the end
list.sort()  # sorts in ascending order
list.sort(reverse=True)  # sorts in descending order
list.reverse()  # reverse list
list.insert(2, 6)  # insert element '6' at index 2
list.remove(6)  # removes first occurence of element
list.pop(2)  # removes element at index 2
print(list)
print(type(list))

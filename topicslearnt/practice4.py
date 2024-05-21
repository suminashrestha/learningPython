# Qn1
dict = {
    "table": ("a piece of furniture",  "list of facts and figures"),
    "cat": "a small animal"  # as a tuple
}
print(dict)
print(type("table"))

# Qn 2
subjects = {
    "python", "java", "C++", "python", "JS", "java", "python", "java", "C++", "C"
}
print(subjects)
print(len(subjects))

# Qn 3
# dictionary = {}
# phy = input("Enter marks of phy")
# math = input("Enter marks of math")
# chem = input("Enter marks of chem")
# dictionary.update({"physics": phy})
# dictionary.update({"maths": math})
# dictionary.update({"chemistry": chem})
# print(dictionary)

# Qn 4 to save 9 and 9.0 as different values
values = {9, "9.0"}  # --> one way
# next way by using built-in data type in the pair of tuples
value = {
    ("float", 9.0),
    ("int", 9)
}
print(value)

print(values)

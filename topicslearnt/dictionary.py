# Dictionary
# lists, tuples can be stored
# in the form -->  ["key":value]  --> also key can be int, float
# but generally key is string


# # Nested Dictionary
# student = {
#     "name": "rahul kumar",
#     "subjects": {
#         "maths": 78,
#         "phy": 67,
#         "chem": 98
#     }
# }
# print(student["subjects"]["chem"])
info = {
    "key": "value",
    "name": "sumina",
    "learning": "coding",
    "age": 22,
    "is_adult": True,
    "marks": 97
}
# print(info)
# print(type(info))
# # since it is unordered, info[0],info[1] are mistake
# # instead we use:
# print(info["key"])
# Dictionary Methods
# print(info.keys())
# print(info.values())
# print(info.items())  # in the form of tuples
# print(info.get("name"))  #return the key according to the value
info.update({"city": "ktm"})
print(info)

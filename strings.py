# str1 = "Sumina"
# str2 = "Shrestha"
# len1 = len(str1)
# len2 = len(str2)
# print(len1)
# print(len2)
# final_str = str1 + " " + str2
# print(final_str)
# print(len(final_str))

str = "apna college"
ch = str[2]
# str[4] = '@' //cant modify , can only access
print(ch)

# slicing
# str[starting_index:ending_index]  --> ending index is not included
print(str[1:4])
print(str[:4])  # is same as str[0:4]
print(str[1:])  # is same as str[1:len(str)]

# negative index
str4 = "Apple"
print(str4[-5:-1])

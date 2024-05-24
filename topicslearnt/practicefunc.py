# qn1 print length of a list
nums = [22, 3, 4, 56, 7, 5]  # this is a list
cities = ["ktm", "pokhara", "jhapa", "lalitpur", "bkt"]


def print_length(list):
    print(len(list))


print_length(nums)

# qn2 to print the elements of a list in a single line


def print_elements(list):
    for item in list:
        print(item, end=" ")


print_elements(cities)

# qn3 find factorial of n(n is the parameter)


def find_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


print(find_fact(4))

# qn4 convert usd into npr


def converter(usd_value):
    npr = 1
    npr = usd_value * 130
    return npr


print(converter(20))

# sum of first n natural numbers


# def sum_natural(n):
#     if (n == 0):
#         return 0
#     else:
#         return n + sum_natural(n-1)


# print(sum_natural(5))

# print all elements in a list
fruits = ["apple", "banana", "mango", "peach", "orange"]


def print_lists(list, idx=0):
    if (len(list) == idx):
        return
    else:
        print(list[idx])
        print_lists(list, idx+1)


print_lists(fruits)

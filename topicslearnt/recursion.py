# recursive function
# def show(n):
#     if (n == 0):  # Base case ->tells when should recursion stop
#         return  # we are returning the control
#     print(n)
#     show(n-1)  # recursion
#     print("End")


# show(5)

# factorial of a number


def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)


print(fact(5))

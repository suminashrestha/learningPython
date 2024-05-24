# Functions : Block of statements that performs a specific tasks.
#  "def" is used.

def summ(a, b):  # parameters --> returns
    sum = a+b
    return sum


print(summ(3, 4))  # function call

# average of 3 numbers


def calc_avg(a, b, c):
    sum = a + b + c
    average = sum/3
    print(average)


calc_avg(3, 4, 5)

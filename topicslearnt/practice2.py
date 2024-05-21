# Qn 1
num = int(input("Enter any number: "))

if (num % 2 == 0):
    print("Even number")
else:
    print("Odd number")

# Qn 2
n1 = int(input("Enter first  number: "))
n2 = int(input("Enter second  number: "))
n3 = int(input("Enter third  number: "))

if (n1 > n2 and n1 > n3):
    print(n1, "is greatest")
elif (n2 > n3):
    print(n2, "is greatest")
else:
    print(n3, "is greatest")

# Qn3
num2 = int(input("Enter any number: "))
if (num2 % 7 == 0):
    print(num2, "is a multiple of 7")
else:
    print(num2, "is not a multiple of 7")

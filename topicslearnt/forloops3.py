# For loops with range
'''
for number in range(first_index, last_index, increase_by ):
    print(number)
'''

for number in range(1, 11, 2):
    print(number)

# to print the sum : 0+1+2+3+4+....+100
total = 0
for num in range(1, 101):
    total += num
print(total)

# printing sum even numbers from 1 to 100
total = 0
for num in range(1, 101):
    if (num % 2 == 0):
        total += num
print(total)

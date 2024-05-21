# For loops using lists
'''
    for item in list_of_items:
       Do something to each item
'''
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# calculating average height
student_heights = input("Input a list of student heights:").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height = total_height + height
print(total_height)

num_of_students = 0
for students in student_heights:
    num_of_students = num_of_students+1
print(num_of_students)

average_height = total_height/num_of_students
print("The average height is: ", round(average_height))

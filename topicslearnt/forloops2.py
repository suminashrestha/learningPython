student_scores = input("Enter a list of students score: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print("The highest score in the class is: ", max_score)

min_score = 0
lowest_score = 0
for score in student_scores:
    if student_scores[min_score] < student_scores[min_score+1]:
        lowest_score = score
print("The lowest score in the class is: ", lowest_score)

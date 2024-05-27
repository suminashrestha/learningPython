# oops
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi ", self.name, ", Your average marks is: ", sum / 3)


s1 = Student("Sumina", [90, 98, 99])
s1.print_average()

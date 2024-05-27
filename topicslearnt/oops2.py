# constructor
#  __init__(self)  is default constructor
# __init__(self,name,marks) is parameterized constructor
class Student:
    college_name = "NCIT"  # class attribute
    name = "anonymous"

    def __init__(self, name, marks):
        self.name = name  # obj attr > class attr
        self.marks = marks

    @staticmethod
    def welcome():
        print("Welcome!")

    def hello(self):  # method (creating class)
        print("Hello", self.name)


s1 = Student("Sumina", 89)
s1.welcome()
print(s1.name)
print(s1.marks)
s1.hello()  # method (creating object)

# Methods
# -> methods are functions that belong to objects.

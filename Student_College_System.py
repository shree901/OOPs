class Student:
    college_name = "ABC College"   # Class Variable

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"


# Objects
s1 = Student("Rahul", 1)
s2 = Student("Anita", 2)

s1.display()
s2.display()

print("Result:", Student.is_pass(80))

# Change college
Student.change_college("XYZ College")

print("\nAfter College Change:")
s1.display()
s2.display()

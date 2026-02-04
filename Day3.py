# Parent class
class Father:
    def __init__(self, father_name, surname):
        self.father_name = father_name
        self.surname = surname

    def display_father_name(self):
        print("Father Name:", self.father_name)

    def display_surname(self):
        print("Surname:", self.surname)


# Child class
class Child(Father):
    def __init__(self, child_name, father_name, surname):
        super().__init__(father_name, surname)
        self.child_name = child_name

    def display_child_name(self):
        print("Child Name:", self.child_name)


# Creating object
child_obj = Child("Shreelakshmi", "Harish", "H")

# Calling different methods
child_obj.display_father_name()
child_obj.display_surname()
child_obj.display_child_name()

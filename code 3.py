class Student:
    def __init__(self, name, age, grade):
        self.name= name
        self.age= age
        self.grade= grade
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

class Undergraduatestudent(Student):
    def __init__(self, name, age, grade, major):
        super(). __init__(name, age, grade)
        self.major= major

    def display_info(self):
        super().display_info()
        print("Major:", self.major)

class Graduatestudent(Student):
    def __init__(self, name, age, grade, program_title):
        super(). __init__(name, age, grade)
        self.program_tile= program_title

    def display_info(self):
        super().display_info()
        print("Program_Title:", self.program_tile)

s1=Undergraduatestudent("Ali", 2025, 91, "Engineering")
s2=Graduatestudent("Mahmoud", 1244, 87, "Mater")

s1.display_info()
s2.display_info()


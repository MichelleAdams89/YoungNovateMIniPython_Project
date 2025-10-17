# 1. Create a class called Student
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.__grade = grade   # private attribute (cannot be accessed directly)

    # 2. A method to show the student's details
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.__grade)

    # Getter method to get the grade
    def get_grade(self):
        return self.__grade

    # Setter method to change the grade
    def set_grade(self, grade):
        self.__grade = grade


# 3. A new class that inherits from Student
class GraduateStudent(Student):
    def __init__(self, name, age, grade, degree):
        super().__init__(name, age, grade)  # call parent class
        self.degree = degree

    # 5. Overriding the display_info() method (Polymorphism)
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Degree:", self.degree)
        print("Grade:", self.get_grade())


# 6. Create three students
student1 = Student("Mimi", 20, "A")
student2 = Student("James", 19, "B+")
student3 = GraduateStudent("Sarah", 24, "A", "MSc Computer Science")

# Show their details
print("---- Student 1 ----")
student1.display_info()

print("\n---- Student 2 ----")
student2.display_info()

print("\n---- Graduate Student ----")
student3.display_info()

# Example of changing a grade using the setter
print("\nChanging Mimi's grade...")
student1.set_grade("A+")
print("New Grade:", student1.get_grade())

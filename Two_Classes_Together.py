class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self,student):
        if len(self.students) < self.max_student :
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 18, 85)

course = Course("Biology",1)

print(course.add_student(s1))

# s2 wont get added to the course since max_student is 1
print(course.add_student(s2))
print(course.get_average_grade())
print(course.students[0])

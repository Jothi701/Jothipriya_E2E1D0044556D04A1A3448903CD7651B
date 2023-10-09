class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

student1 = Student("Gobika", "CS08", 8.2)
student2 = Student("Harni", "CS17", 9.0)
student3 = Student("Poomagal", "CS28", 7.4)
student4 = Student("Senthilkumar", "CS41", 5.8)
students = [student1, student2, student3, student4]

sorted_students = sort_students(students)
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
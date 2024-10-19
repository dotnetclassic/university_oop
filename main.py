class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Human):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Teacher(Human):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

class Section:
    def __init__(self, section_name, start_time, end_time, teacher):
        self.section_name = section_name
        self.start_time = start_time
        self.end_time = end_time
        self.teacher = teacher  # instance of Teacher class
        self.students = []  # list of Student instances

    def add_student(self, student):
        self.students.append(student)

class University:
    def __init__(self, name):
        self.name = name
        self.students = []  # list of all students
        self.teachers = []  # list of all teachers
        self.sections = []  # list of sections in the university

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_section(self, section):
        self.sections.append(section)

    def get_section_details(self):
        print(f"University: {self.name}\n")
        for section in self.sections:
            print(f"Section: {section.section_name}")
            print(f"Teacher: {section.teacher.name}")
            print(f"Timing: {section.start_time} - {section.end_time}")
            print("Students enrolled:")
            for student in section.students:
                print(f"- {student.name}")
            print()  # For a blank line between sections

# Example usage
university = University("PIAIC")

# Create teachers
teacher1 = Teacher("Naveed Sarwar", 40, "T001")
teacher2 = Teacher("Abu Huraira", 35, "T002")

# Create students
student1 = Student("Muhammad Imran", 20, "S001")
student2 = Student("Saleh Saqib", 21, "S002")
student3 = Student("Shahid Rafiq", 22, "S003")

# Add teachers and students to the university
university.add_teacher(teacher1)
university.add_teacher(teacher2)
university.add_student(student1)
university.add_student(student2)
university.add_student(student3)

# Create sections
section1 = Section("AI 101", "9:00 AM", "10:30 AM", teacher1)
section2 = Section("Python 202", "11:00 AM", "12:30 PM", teacher2)

# Add students to sections
section1.add_student(student1)
section1.add_student(student2)
section2.add_student(student3)

# Add sections to university
university.add_section(section1)
university.add_section(section2)

# Display section details
university.get_section_details()

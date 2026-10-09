#Creating some typa project, lets spin: 
#Create an application for a student, using a student's paramaters like attendance, grades
#create subroutines to automate the process of calculating the student's performance based on their attendance and grades.
#create class for the student with attributes like name, attendance, grades, and methods to calculate performance.
#learn file handling for storing and retrieving student data.
#use dictionaries/lists to manage multiple students and their data.


def Student_Collection(student):
    student = {"name": input("Enter your name:"),
           "attendance":0,
           "subject": "",
           "age": 0,
           "performance": ""}
    student["attendance"] = input("Classes attended?")
    students.append(student)



print("Welcome to the SEAtS")
Answer =input("Would you like to register as a student or teacher?")

if Answer == "Student":
    Answer == input("Welcome! Your name is: ")
    Student_Collection(Answer)
    

students = []
teachers = []
#I realized here that created students and teachers would not be stored in memory when the subroutines are called#
#so i created an array to store the students and teachers in memory, so that they can be accessed later on in the program.
    


def teacher_collection(teacher):
    teacher = {"name": "",
           "subject": "",
           "age": 0}
    teachers.append(teacher)
\

if Answer == "student":
    name = input("What's your name")
    Student_Collection(name)

else:
    name = input("Enter your last name")
    teacher_collection(name)


def Change_Info(Student, number):
    for i in students:
        if i["name"] == Student:
            match number:
                case 1:
                    i["name"] = input("Enter your name")
                case 2:
                    i["attendance"] = input("Enter your attendance")
                case 3:
                    i["subject"] = input("Enter your subject")
                case 4:
                    i["age"] = input("Enter your age")
                case 5:
                    i["performance"] = input("enter your performance")

def Change_InfoT(Teacher, number):
    for i in teachers:
        if i["name"] == Teacher:
            match number:
                case 1:
                    i["name"] = input("Enter your name")
                case 2:
                    i["subject"] = input("Enter your subject")
                case 3:
                    i["age"] = input("Enter your age")

def RemoveUser(Student):
    try:
        students.index(Student)
        students.remove(Student)
        print("Student removed from the list.")
    except ValueError:
        print("Student not found in the list.")


class Student:
    def __init__(self, name, age, attendance, subject, performance):
        self.name = name
        self.age = age
        self.attendance = attendance
        self.subject = subject
        self.performance = performance

    def incrase_attendance(self, classes_attended):
        self.attendance+= classes_attended

    


#Plan for later: replicate this for teachers
#Learn file handling to store and retrieve student data, so that the data is not lost when the program is closed.
#Add some error handling - try and except blocks to handle errors like invalid input, file not found, etc.



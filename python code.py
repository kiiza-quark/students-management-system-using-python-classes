# NAME: NSHABIIRWE KIZZAH
# REGISTRATION NUMBER: 21/U/09435
# STUDENT NUMBER: 2100709435
import time

class Student:
    University = 'Makerere University'
    students = 0
    id_number = 2100000
    def __init__(this, full_name, student_No, registration_number):
        this.full_name = full_name
        this.student_No = student_No
        this.registration_number = registration_number
        Student.students += 1
        this.id_number = Student.id_number + 11  # to create a unique id for every student
        Student.id_number = this.id_number

    def print_statement(this):
        print(f' Name: {this.full_name} \n University: {this.University} \n 
              f'Reg No: {this.registration_number}\n Student No: {this.student_No}\n 
              f'ID No: {this.id_number} \n Total Students: {this.students}\n\n\n')

class CEDAT_Student(Student):
    college = 'CEDAT' 
    def print_statement(this):
            print(f' Name: {this.full_name} \n University: {this.University} \n 
                  f'College: {this.college} \n Reg No: {this.registration_number}\n Student No: {this.student_No} \n 
                  f'ID No: {this.id_number} \n Total Students: {this.students} \n\n\n')

class CoCIS_Student(Student):
    college = 'CoCIS'   
    def print_statement(this):
        print(f' Name: {this.full_name} \n University: {this.University} \n College: {this.college} \n Reg No: {this.registration_number}\n Student No: {this.student_No} \n ID No: {this.id_number} \n Total Students: {this.students} \n\n\n')

class EDUC_Student(Student):
    college = 'Education'   
    def print_statement(this):
        print(f' Name: {this.full_name} \n University: {this.University} \n College: {this.college} \n Reg No: {this.registration_number}\n Student No: {this.student_No} \n ID No: {this.id_number} \n Total Students: {this.students} \n\n\n')

class EASLIS_Student(CoCIS_Student, Student):
    School = 'EASLIS'
    def print_statement(this):
        print(f' Name: {this.full_name} \n University: {this.University} \n College: {this.college} \n School: {this.School}\n Reg No: {this.registration_number}\n Student No: {this.student_No}\n ID No: {this.id_number} \n Total Students: {this.students} \n\n\n')

class SCIT_Student(CoCIS_Student, Student):
    School = 'SCIT' 
    def print_statement(this):
        print(f' Name: {this.full_name} \n University: {this.University} \n College: {this.college} \n School: {this.School} \n Reg No: {this.registration_number}\n Student No: {this.student_No}\n ID No: {this.id_number} \n Total Students: {this.students} \n\n\n')

class CS_Student(CoCIS_Student, Student):
    department = 'Computer Science'   
    def print_statement(this):
        print(f' Name: {this.full_name} \n University: {this.University} \n College: {this.college} \n Reg No: {this.registration_number}\n Student No: {this.student_No} \n Department: {this.department}\n ID No: {this.id_number} \n Total Students: {this.students}\n\n\n')

class SE_Student(CoCIS_Student,Student):
    department = 'Networks'
    def print_statement(this):
        print(f' Name: {this.full_name} \n University: {this.University} \n College: {this.college}  \n Reg No: {this.registration_number}\n Student No: {this.student_No} \n Department: {this.department} \n ID No: {this.id_number} \n Total Students: {this.students}\n\n\n')

student1 = Student('Kayiwa John', 2020172, '2020/U/172')
student2 = SE_Student('Lumu Musa', 202018283, '2020/U/18283/EVE')
student3 = CS_Student('Adongo Diana', 20201725, '2020/U/1725')

student1.print_statement()
student2.print_statement()
student3.print_statement()

time.sleep(180)
 

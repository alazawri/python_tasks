# 1
student_1 = {
    'Name': input('Student Name :'),
    'Math_grade': input('Enter Math Grade :'),
    'Physics_grade': input('Enter Physics Grade :'),
    'Attendance': input('Enter Number Of Day Present :'),
}

student_2 = {
    'Name': input('Student Name :'),
    'Math_grade': input('Enter Math Grade :'),
    'Physics_grade': input('Enter Physics Grade :'),
    'Attendance': input('Enter Number Of Day Present :'),
}

# 2
students = {'student_1': student_1, 'student_2': student_2}


for student in students.values():
  print(student)
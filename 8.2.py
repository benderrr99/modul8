from peewee import *

from datetime import datetime

conn = SqliteDatabase('db2.sqlite')

class Students(Model):
    id = PrimaryKeyField(column_name = 'id')
    firstname = CharField(column_name = 'firstname')
    surname = CharField(column_name = 'lastname')
    age = IntegerField(column_name = 'age')
    city = CharField(column_name = 'city')

    class Meta:
        database = conn

class Courses(Model):
    id = PrimaryKeyField(column_name = 'id')
    name = CharField(column_name = 'name')
    time_start = DateTimeField(column_name = 'time_start')
    time_end = DateTimeField(column_name = 'time_end')

    class Meta:
        database =conn

class Student_Courses(Model):
    student_id = ForeignKeyField(Students, to_field = 'id', column_name = 'student_id')
    course_id = ForeignKeyField(Courses, to_field = 'id', column_name = 'course_id')

    class Meta:
        database =conn

Students.create_table()
Courses.create_table()
Student_Courses.create_table()

student = Students(firstname = 'Max', surname = 'Brooks', age = 24, city = 'Spb')
student.save()
student = Students(firstname = 'John', surname = 'Stones', age = 15, city = 'Spb')
student.save()
student = Students(firstname = 'Andy', surname = 'Wings', age = 45, city = 'Manchester')
student.save()
student = Students(firstname = 'Kate', surname = 'Brooks', age = 34, city = 'Spb')
student.save()

course = Courses(name = 'python', time_start = '21.07.21', time_end = '21.08.21')
course.save()
course = Courses(name = 'java', time_start = '13.07.21', time_end = '16.08.21')
course.save()

st_cs = Student_Courses(student_id = 1, course_id = 1)
st_cs.save()
st_cs = Student_Courses(student_id = 2, course_id = 1)
st_cs.save()
st_cs = Student_Courses(student_id = 3, course_id = 1)
st_cs.save()
st_cs = Student_Courses(student_id = 4, course_id = 2)
st_cs.save()

for student in Students.select().where(Students.age > 30):
    print(student.firstname, student.surname, student.age)
print('')

query = Students.select().join(Student_Courses).join(Courses).where(Courses.name == 'python')
for student in query:
    print(student.firstname, student.surname)
print('')

query_two = Students.select().join(Student_Courses).join(Courses).where((Students.city == 'Spb') & (Courses.name == 'python'))
for student in query_two:
    print(student.firstname, student.surname, student.city)
print('')

conn.close()
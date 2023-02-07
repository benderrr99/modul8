import sqlite3
from datetime import datetime

conn = sqlite3.connect('db1.sqlite')

cursor = conn.cursor()

cursor.execute('CREATE TABLE Students (id int PRIMARY KEY, firstname Varchar(32), surname Varchar(32), age int, city Varchar(32))')
cursor.execute('CREATE TABLE Courses (id int PRIMARY KEY, name Varchar(32), time_start datetime, time_end datetime)')
cursor.execute('CREATE TABLE Student_Courses (student_id int, course_id int, FOREIGN KEY(student_id) REFERENCES Students(id),  FOREIGN KEY(course_id) REFERENCES Courses(id))')

cursor.executemany('INSERT INTO Students VALUES (?, ?, ?, ?, ?)', [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')])
cursor.executemany('INSERT INTO Courses VALUES (?, ?, ?, ?)', [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')])
cursor.executemany('INSERT INTO Student_Courses VALUES (?, ?)', [(1, 1), (2, 1), (3, 1), (4, 2)])

conn.commit()

cursor.execute('SELECT * FROM Students WHERE age > 30')
print(cursor.fetchall())
cursor.execute('SELECT Students.firstname, Students.surname, Courses.name FROM Students, Courses, Student_Courses WHERE (Courses.id = 1) AND (Student_Courses.course_id=Courses.id) and (Students.id=Student_Courses.student_id)')
print(cursor.fetchall())
cursor.execute("SELECT Students.firstname, Students.surname, Students.city, Courses.name FROM Students, Courses, Student_Courses WHERE (Courses.id = 1) AND (Student_Courses.course_id=Courses.id) and (Students.id=Student_Courses.student_id) and (Students.city = 'Spb')")
print(cursor.fetchall())
conn.close()


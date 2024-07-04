import mysql.connector as a
con = a.connect(host='localhost', password='', user='') # Enter username, password, and host of your MySQL

#create cursor
c=con.cursor()
c.execute('create database if not exist AMS')
c.execute('use AMS')

#Table Creation
c.execute('''CREATE TABLE school(
school_id int PRIMARY KEY,
school_name VARCHAR(30)
)''')

c.execute('''CREATE TABLE parent(
parent_id int PRIMARY KEY,
Parent_name VARCHAR(25),
phone_number VARCHAR(25),
email VARCHAR(25)
);''')

c.execute('''CREATE TABLE class(
class_id int PRIMARY KEY,
class_name VARCHAR(25)
)''')

c.execute('''CREATE TABLE teacher(
teacher_id int PRIMARY KEY,
Teacher_name VARCHAR(25),
phone_number VARCHAR(25),
email VARCHAR(25),
school_id int,
FOREIGN KEY(school_id)REFERENCES school(school_id)
)''')

c.execute('''CREATE TABLE class_teacher(
class_id int,
teacher_id int,
PRIMARY KEY(class_id,teacher_id),
FOREIGN KEY(class_id)REFERENCES class(class_id),
FOREIGN KEY(teacher_id)REFERENCES teacher(teacher_id)
)''')

c.execute('''CREATE TABLE student(
student_id int PRIMARY KEY,
student_name VARCHAR(25),
phone_number VARCHAR(25),
email VARCHAR(25),
parent_id int,
class_id int,
FOREIGN KEY(parent_id)REFERENCES parent(parent_id),
FOREIGN KEY(class_id)REFERENCES class(class_id)
)''')

c.execute('''CREATE TABLE attendance(
student_id int,
class_id int,
adate DATE,
status VARCHAR(10),
PRIMARY KEY(student_id,class_id,adate),
FOREIGN KEY(student_id)REFERENCES student(student_id),
FOREIGN KEY(class_id)REFERENCES class(class_id)
)''')

c.execute('''CREATE TABLE alert(
alert_id int AUTO_INCREMENT PRIMARY KEY,
message VARCHAR(25),
sent_to VARCHAR(25)
)''')
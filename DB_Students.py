# �������� ������� Students
import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """CREATE TABLE Students 
(
Student_Id INTEGER NOT NULL PRIMARY KEY, 
Student_Name TEXT NOT NULL, 
School_Id INTEGER NOT NULL
);
"""
cursor.execute(query)
connection.commit()
connection.close()

# ���������� ������� Students
import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """INSERT INTO Students (Student_Id, Student_Name, School_Id) 
VALUES 
('201', '����', '1'), 
('202', '����', '2'), 
('203', '���������', '3'), 
('204', '�����', '4');
"""
cursor.execute(query)
connection.commit()
connection.close()

# ������ � ���� ������

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()



def get_student_detail(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM School 
    JOIN Students ON School.School_Id = Students.School_Id 
    WHERE Students.Student_Id  = ?"""
    cursor.execute(select_query, (student_id,))
    records = cursor.fetchall()
    print ("������ �� ��������")
    for row in records:
      print ("ID ��������", row[3])
      print ("��� ��������", row[4])
      print ("ID �����", row[0])
      print ("�������� �����", row[1])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("������ � ��������� ������ �� ��������", error)



print ("������ �� ��������")
print ("\n")
get_student_detail(203)
from collections import namedtuple
number_of_students = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
students = []
total = 0
for i in range(number_of_students):
    column1, column2, column3, column4 = input().split()
    students.append(Student(column1, column2, column3, column4))
    total += int(students[i].MARKS)
print('{:.2f}'.format(total/number_of_students))
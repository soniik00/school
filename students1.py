f = open('students.csv', encoding='utf-8')
students = []

class Student:
    id = 0
    fio = ''
    clas = ''
    score = 0



for i in range(501):
    students.append(Student())
    s = f.readline().split(',')
    if s[4] == None:
        s[4] = -10
    students[i].id = s[0]
    students[i].fio = s[1]
    students[i].clas = s[3]
    students[i].score = s[4]


f = 'Хадаров Владимир Валериевич'

for i in range(len(students)):
    if students[i].fio == f:
        print('Ты получил:', students[i].score, ', за проект -', students[i].id)
        break

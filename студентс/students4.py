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
    students[i].fio = s[1].split(' ')
    print(students[i].fio)
    students[i].clas = s[3]
    students[i].score = s[4]

for i in range(1, len(students)):
    login = students[i].fio[0]+'_'+students[i].fio[1][0]+students[i].fio[2][0]
    print(login)







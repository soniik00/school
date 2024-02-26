f = open('students.csv', encoding='utf-8')
students = []

class Student:
    fio = ''
    clas = ''
    score = 0


for i in range(501):
    students.append(Student())
    s = f.readline().split(',')
    if s[4] == None:
        s[4] = -10
    students[i].fio = s[1]
    students[i].clas = s[3]
    students[i].score = s[4]


for i in range(len(students)):
    t = students[i]
    j = i - 1
    while j >= 0 and t.score < students[j].score:
        students[j+1] = students[j]
        j -= 1
    students[j+1] = t



for i in range(3):
    print(i+1, 'место:', students[i].fio)
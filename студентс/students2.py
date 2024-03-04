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


students10 = []

for i in range(len(students)):
    if students[i].clas[:-1] == '10':
        students10.append(students[i])

for i in range(len(students10)):
    t = students10[i]
    j = i - 1
    while j >= 0 and t.score > students10[j].score:
        students10[j+1] = students10[j]
        j -= 1
    students10[j+1] = t

print('10 класс:')
for i in range(3):
    print(i+1, 'место:', students10[i].fio)


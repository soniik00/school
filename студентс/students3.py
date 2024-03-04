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
    students[i].fio = s[1]
    students[i].clas = s[3]
    students[i].score = s[4]
    students[i].id = s[0]


id1 = input()

for i in range(len(students)):
    if students[i].id == str(id1):
        print('Проект №', students[i].id, 'делал: ', students[i].fio, 'он(а) получил(а) оценку - ', students[i].score)
        exit()

print('Ничего не найдено.')

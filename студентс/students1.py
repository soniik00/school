f = open('students.csv', encoding='utf-8')
students = []

class Student:
    id = 0
    fio = ''
    clas = ''
    score = 0
    title = ''



for i in range(501):
    students.append(Student())
    s = f.readline().strip().split(',')
    students[i].id = s[0]
    students[i].fio = s[1]
    students[i].title = s[2]
    students[i].clas = s[3]
    students[i].score = s[4]

sum = 0
k = 0
for i in students:
    if str(i.score) == 'None\n':
        for j in students:
            if i.clas == j.clas and j.score != 'None\n':
                k += 1
                sum += j.score
                print(sum)
        i.score = round(sum/k, 3)



fil = open('new_students.csv', 'w')

for i in students:
    print(i.id, ',', i.fio, ',', i.title, ',', i.clas, ',', i.score, file = fil)



f = 'Хадаров Владимир Валериевич'

for i in range(len(students)):
    if students[i].fio == f:
        print('Ты получил:', students[i].score, ', за проект -', students[i].id)
        break

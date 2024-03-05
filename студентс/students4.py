import random
f = open('students.csv', encoding='utf-8')
students = []

class Student:
    title = ''
    id = 0
    fio = ''
    clas = ''
    score = 0
    login = ''
    p = ''



for i in range(501):
    students.append(Student())
    s = f.readline().strip().split(',')
    if s[4] == None:
        s[4] = 0
    students[i].id = s[0]
    students[i].fio = s[1].split(' ')
    students[i].title = s[2]
    students[i].clas = s[3]
    students[i].score = s[4]


a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def par():
    par = '00000000'
    for i in range(8):
        place = random.randint(0, 7)
        symb = random.choice(a)
        par[place] = symb
    print(par)


for i in range(1, len(students)):
    login = students[i].fio[0] + '_' + students[i].fio[1][0] + students[i].fio[2][0]
    p = par()




fil1 = open('students_password.csv', 'w')

for i in students:
    print(i.id, ',', i.fio, ',', i.title, ',', i.clas, ',', i.score, ',', i.login, ',', i.p, file = fil1)


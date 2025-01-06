grade = input()

dic = {
    'F': 60,
    'D': 69 ,
    'C': 79,
    'B': 89,
    'A': 100,
}

if int(grade) < dic['F']:
    print('F')
if int(grade) >= dic['F'] and int(grade) <= dic['D']:
    print('D')
if int(grade) >= dic['D'] and int(grade) <= dic['C']:
    print('C')
if int(grade) >= dic['C'] and int(grade) <= dic['B']:
    print('B')
if int(grade) > dic['B']:
    print('A')

#print(dic[0])

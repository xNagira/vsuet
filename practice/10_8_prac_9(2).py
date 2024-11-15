maxx=0

file=open(r'C:\Users\home\Desktop\files\Морозова Яна Евгеньевна_УБ-41_vvod.txt')

matr=[]
matr= [[int(num) for num in line.split(' ')] for line in file]

print('старая (исходная)',*matr, sep='\n')

for i in range(len(matr)):
    for j in range(len(matr[i])):
        if abs(matr[i][j]) > maxx:
            maxx = abs(matr[i][j])
            istrok=i
            jstol=j

print('Макс. по модулю эл. -',maxx)

del matr[istrok]
for i in range(len(matr)):
    matr[i].pop(jstol)

fw=open(r'C:\Users\home\Desktop\files\Морозова Яна Евгеньевна_УБ-41_vivod.txt', 'w')

for i in range(len(matr)):
    for j in range(len(matr[i])):
        fw.write(str(matr[i][j])+' ')
    fw.write('\n')
fw.write(str('Макс. по модулю эл. в исходной матрице было '+ str(maxx)+' , поэтому по нему и убрали строки и столбцы'))
fw.close()

print('новая',*matr, sep='\n')
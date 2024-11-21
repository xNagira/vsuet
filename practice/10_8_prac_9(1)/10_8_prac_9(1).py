maxx=0

file=open(r'C:\Users\home\Desktop\files1\Морозова Яна Евгеньевна_УБ-41_vvod.txt')
matr=[]
matr= [[int(num) for num in line.split(' ')] for line in file]

print('старая (исходная)',*matr, sep='\n')

k=int(input('(чему будут эл. кратны?) k= '))
c=0
for i in range(len(matr)):
    for j in range(len(matr[i])):
        if matr[i][j] % k == 0: #matr[i][j] элемент пересечения i-строки и j-столбца
            c += 1
            if matr[i][j] > maxx:
                maxx = matr[i][j]

fw=open(r'C:\Users\home\Desktop\files1\Морозова Яна Евгеньевна_УБ-41_vivod.txt', 'w')

for i in range(len(matr)):
    for j in range(len(matr[i])):
        fw.write(str(matr[i][j])+' ')
    fw.write('\n')
fw.write(str('эл. кратны ' + str(k)))
fw.write('\n')
fw.write(str('Найдено ' + str(c)))
fw.write('\n')
fw.write(str('Максимально '+ str(maxx)))
fw.close()

print(*matr, sep='\n') #убираем скобки и ставим разделитель
print('Найдено', c)
print('Максимально', maxx)
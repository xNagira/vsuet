from random import randint

n=m=int(input('размер матрицы: '))

matr = [[randint(-10, 10) for i in range(m)] for j in range(n)]
print('Исходная матрица - ',*matr, sep='\n')

maxx=0
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

print(*matr, sep='\n')
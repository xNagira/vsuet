from random import randint

n=m=int(input('размер матрицы: '))

matr = [[randint(-10, 10) for i in range(m)] for j in range(n)]
k=int(input('(чему будут эл. кратны?) k= '))
maxx=0
c=0
for i in range(len(matr)):
    for j in range(len(matr[i])):
        if matr[i][j] % k == 0: #matr[i][j] элемент пересечения i-строки и j-столбца
            c += 1
            if matr[i][j] > maxx:
                maxx = matr[i][j]
print(*matr, sep='\n') #убираем скобки и ставим разделитель
print('Найдено', c)
print('Максимально', maxx)
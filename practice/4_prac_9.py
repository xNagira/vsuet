N=int(input('N - количество чисел: '))

a, b = 0, 1
summ = 0

for i in range(N):
    summ = summ + a
    a, b = b, a + b

print(summ)
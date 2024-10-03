N=int(input('Кол-во вещ. эл.: \n'))
mas=[]
for i in range(N):
    mas.append(float(input()))

a=mas[0]
for i in mas:
    if abs(i)<a:
        a=i
print(a)
mas.reverse()
print(mas)
N=10
A=[]
for i in range(N):
    A.append(float(input('Ввести содержимое 1-го массива A: ')))

B=[]
for i in range(N):
    B.append(float(input('Ввести содержимое 2-го массива B: ')))
print("Исходный массив A:", A)
print("Исходный массив B:", B)

z=A
A=B
B=z

print("Преобразованный массив A:", A)
print("Преобразованный массив B:", B)
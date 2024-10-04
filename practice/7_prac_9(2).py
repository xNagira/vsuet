from random import*
import math

a=int(input('Введите кол-во для 1 массива: '))
b=int(input('Введите кол-во для 2 массива: '))
c=int(input('Введите кол-во для 3 массива: '))

A=[randint(1,30) for i in range(a)]
B=[randint(1,30) for i in range(b)]
C=[randint(1,30) for i in range(c)]

print(A)
print(B)
print(C)

sr_A=sum(A)/len(A)
prA = math.prod(A)
print('Произведение эл. массива 1:', prA)
print('Среднеарифметическое значение 1-го массива:', sr_A)
sr_B=sum(B)/len(B)
prB = math.prod(B)
print('Произведение эл. массива 2:', prB)
print('Среднеарифметическое значение 2-го массива:', sr_B)
sr_C=sum(C)/len(C)
prC = math.prod(C)
print('Произведение эл. массива 3:', prC)
print('Среднеарифметическое значение 3-го массива:', sr_C)








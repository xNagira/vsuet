import math

a=int(input('1 сторона 3-ника: '))
b=int(input('2 сторона 3-ника: '))
c=int(input('3 сторона 3-ника: '))

p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(S)

s=input('Введите строку, содержащую букву "н" и "!": \n')

maxx=0
a=0

for i in s:
    if i=='н':
        a=a+1
        maxx=max(maxx,a)
    else:
        a=0
    if i == "!":
        s = s.replace("!", ".")
print(maxx)
print(s)
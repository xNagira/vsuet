def suma(n):
    summa=0
    while n!=0:
        summa += n%10
        n=n//10
    return summa
def v(n):
    c = 0
    while n != 0:
        n -= suma(n)
        c = c + 1
    return c

s= int(input("Введите число: \n"))
re= v(s)
print(re)




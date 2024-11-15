a=int(input('1-е натур. число: '))
b=int(input('2-е натур. число: '))

def f(a, b):
    if a < b:
        return a
    else:
        return f(a-b, b)

print('остаток ', f(a,b))


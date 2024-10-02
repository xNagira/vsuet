A=int(input('A: '))
B=int(input('B: '))

if A<=B:
    for i in range(A,B+1):
        print(i)
else:
    print('A больше B')
def maxx_num():
    a=int(input('ввод: '))
    if a==0:
        return 0
    m=maxx_num()
    if a>m:
        return a
    else:
        return m

print('Наибольшее значение числа в последовательности: ',maxx_num())
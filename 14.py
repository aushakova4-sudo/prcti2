kn = int(input())
gall = kn//493
kn2 = kn%493
sicl = kn2//29
kn3 = kn2%29
if gall > 0:
    print (gall, "галлеонов")
if sicl > 0:
    print(sicl, 'сиклей')
if kn3 > 0:
    print (kn3, 'кнатов')
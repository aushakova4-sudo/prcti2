number = int(input())
lastnum = number % 10
lasttwonum = number % 100
if lasttwonum in (11, 12, 13, 14):
    print (number, 'попугаев')
elif lastnum == 1:
    print(number,'попугай')
elif lastnum in (2, 3, 4):
    print(number,'попугая')
else:
    print(number, "попугаев")
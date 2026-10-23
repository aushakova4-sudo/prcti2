score1, score2  = map(int,input().split(":"))
if score1 > score2:
    print(1)
elif score1 < score2:
    print(2)
else:
    print(0)
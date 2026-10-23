rec1, rec2, rec3 = map(int, input().split())
if rec1 >= rec2 and rec1 >= rec3:
    print(rec1)
elif rec2 >= rec1 and rec2 >= rec3:
    print(rec2)
else:
    print(rec3)
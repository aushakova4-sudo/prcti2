from math import sqrt
size =  input().split('x')
r = 6.5
d = r*2
A = float(size[0])
B = float(size[1])
diag = sqrt(A**2 + B**2)
if diag <= d:
    print('да')
else:
    print('нет')
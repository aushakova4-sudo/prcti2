size = input().split('x')
N = int(size[0])
M = int(size[1])
K = int(input())
if (K % N == 0 and K < N * M) or (K % M == 0 and K < N * M):
    print("успешно")
else:
    print("неосуществимо")
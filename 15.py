N, K, M = map(int, input().split())
if abs(M-K)>N//2:
    print(N+M-K-1)
else:
    print(M-K-1)

from math import ceil
N, K, M = map(int, input().split())
rides = N*2
sessions = ceil(rides / K)
time = sessions * M
print(time)
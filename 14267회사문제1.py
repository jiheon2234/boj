#https://www.acmicpc.net/problem/14267
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tmp = [*map(int, input().split())]
arr = [0 for _ in range(n)]


for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1] += b

for i in range(1, n):
    arr[i] += arr[tmp[i] - 1]
print(*arr)

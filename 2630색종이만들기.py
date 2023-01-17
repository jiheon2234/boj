# https://www.acmicpc.net/problem/2630

import sys

input = sys.stdin.readline

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]

color = [0, 0]


def check(pivot):
    global color
    if pivot == 0:
        color[0] += 1
    else:
        color[1] += 1


def solve(a, b, c):  # 가로,세로 단위
    pivot = arr[a][b]  # 기준점
    if c == 1:
        check(pivot)
        return
    for i in range(c):
        for j in range(c):
            if arr[a + i][b + j] != pivot:  # 색깔이 하나라도 다르면
                c = c // 2
                solve(a, b, c)
                solve(a + c, b, c)
                solve(a, b + c, c)
                solve(a + c, b + c, c)
                return
    check(pivot)


solve(0, 0, n)

print(color[0])
print(color[1])

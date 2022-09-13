# https://www.acmicpc.net/problem/2470
import sys

input = sys.stdin.readline

answer = 1e10
answer1 = [None, None]
n = int(input())
arr = sorted([*map(int, input().split())])

start, end = 0, n - 1

while end > start:
    tmp = arr[start] + arr[end]
    if abs(tmp) < answer:
        answer = abs(tmp)
        answer1 = [arr[start], arr[end]]
    if tmp < 0:  # 0보다작다면
        start += 1  # 더큰방향으로
    elif tmp > 0:  # 9보다크다면
        end -= 1  # 더작아지는방향으로
    else:  # 0이면 볼거없음
        answer = [arr[start], arr[end]]
        print(min(answer1), max(answer1))
        exit()


print(min(answer1), max(answer1))

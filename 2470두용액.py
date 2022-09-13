# https://www.acmicpc.net/problem/2470

import sys

input = sys.stdin.readline

answer = 1e10
answer1 = [None, None]
n = int(input())
arr = sorted([*map(int, input().split())])

start, end = 0, n - 1

while start<end:
    a,b=arr[start],arr[end]
    c=a+b

    if c<0: #0보다 작다면
        start+=1 
    elif c>0: #0보다 크다면
        end-=1
    else:
        break

print(a, b)
        




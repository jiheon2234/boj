# https://www.acmicpc.net/problem/5052
import sys
input =sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=sorted([input().rstrip() for _ in range(n)]) #정렬하면 바로 옆만 비교하면 됨!
    flag=False
    for i in range(n-1):
        if arr[i+1].startswith(arr[i]):
            flag=True
            break
    print('NO' if flag else 'YES')


        


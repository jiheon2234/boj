# https://www.acmicpc.net/problem/18405

import sys
from collections import deque
input=sys.stdin.readline
arr=[]

move=[[-1,0],[1,0],[0,-1],[0,1]]
n,k=map(int,input().split())
virus=[[] for _ in range(k+1)]

for i in range(n):
    tmp=[*map(int,input().split())]
    arr.append(tmp)
    for j in range(n):
        t=tmp[j]
        if t!=0:
            virus[t].append((i,j,0))           
s,x,y=map(int,input().split())
q=deque()
for vii in virus:
    if vii:
        for vi in vii:
            q.append(vi)

def bfs():
    while q:
        cx,cy,t=q.popleft()
        if t==s:
            print(arr[x-1][y-1])
            exit()
        for dx,dy in move:
            nx,ny=cx+dx,cy+dy
            if 0<=nx<n and 0<=ny<n and not arr[nx][ny]:
                
                arr[nx][ny]=arr[cx][cy]
                
                q.append((nx,ny,t+1))
                
            

bfs()
print(arr[x-1][y-1])

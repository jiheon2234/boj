import sys
from collections import deque
import copy
input=sys.stdin.readline
move=((-1,0),(1,0),(0,-1),(0,1))

def bfs1(i,j,color,arr):
    que=deque()
    que.append((i,j))
    arr[i][j]=-1

    while que:
        i,j=que.popleft()

        for a,b in move:
            ti,tj=i+a,j+b
            if 0<=ti<n and 0<=tj<n and arr[ti][tj]==color:
                arr[ti][tj]=-1
                que.append((ti,tj))



n=int(input())
graph=[list(input().strip())for _ in range(n)]
arr=copy.deepcopy(graph)
arr1=copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if arr1[i][j] in ('R','G'):
            arr1[i][j]='R'
answer0=0
answer1=0
for i in range(n):
    for j in range(n):
        if arr[i][j]!=-1:
            bfs1(i,j,arr[i][j],arr)
            answer0+=1
        if arr1[i][j]!=-1:
            bfs1(i,j,arr1[i][j],arr1)
            answer1+=1
print(answer0,answer1)

            

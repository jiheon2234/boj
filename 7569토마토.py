# https://www.acmicpc.net/problem/7569
import sys
input=sys.stdin.readline
from collections import deque
moves=[[-1,0,0],[0,-1,0],[0,0,-1],[1,0,0],[0,1,0],[0,0,1]]

def bfs(q):
    day=0
    while q:
        i,j,k,v=q.popleft()
        for move in moves:
            a,b,c=move
            ti=a+i
            tj=b+j
            tk=c+k
            if 0<=ti<h and 0<=tj<n and 0<=tk<m and arr[ti][tj][tk]=='0':
                q.append([ti,tj,tk,v+1])
                arr[ti][tj][tk]='-1'
              
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k]=='0':
                    print(-1)
                    return
            
    print(v)
    



    



m,n,h=map(int,input().split())

arr=[[list(input().strip().split())for _ in range(n)]for _ in range(h)]

q=deque()
answer=0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k]=='1':
                q.append((i,j,k,0))
                arr[i][j][k]='-1'
            
bfs(q)


# https://www.acmicpc.net/problem/7576
import sys
from collections import deque
input=sys.stdin.readline

def bfs(m,n,box,forbfs):
    moves=[[0,1],[0,-1],[1,0],[-1,0]]
    l=0
    while forbfs:
        i,j,l=forbfs.popleft()
        
        for move in moves:
            tmp_i=i+move[0]
            tmp_j=j+move[1]
            if 0<=tmp_i<n and 0<=tmp_j<m:

                if box[tmp_i][tmp_j]==0:
                    forbfs.append([tmp_i,tmp_j,l+1])
                    box[tmp_i][tmp_j]=1
    for aa in range(n):
        for bb in range(m):
            if  box[aa][bb]==0:

                return-1
    return l
            
                    
    # print(l)
    # print(box)   
        
        


m,n=map(int,input().split())
box=[[*map(int,input().strip().split())]for _ in range(n)]
forbfs=deque()

# visited=[[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            forbfs.append([i,j,0])
            # visited[i][j]=True
            
print(bfs(m,n,box,forbfs))


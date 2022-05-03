import sys
from collections import deque
input=sys.stdin.readline

moves=[(-1,0),(1,0),(0,-1),(0,1)]
def bfs(start_i=0,start_j=0):
   
    que=deque()
    que.append((start_i,start_j,0))

    while que:
        i,j,wall=que.popleft()
        for a,b in moves:
            tmp_i,tmp_j=i+a,j+b
            if 0<=tmp_i<m and 0<=tmp_j<n and graph[tmp_i][tmp_j]!=-1:
                if tmp_i==m-1 and tmp_j==n-1:
                    graph[tmp_i][tmp_j]=-1
                    
                    print(wall)
                    exit()

                elif graph[tmp_i][tmp_j]=='0':
                    graph[tmp_i][tmp_j]=-1
                    que.appendleft((tmp_i,tmp_j,wall))

                elif graph[tmp_i][tmp_j]=='1':
                    graph[tmp_i][tmp_j]=-1
                    
                    que.append((tmp_i,tmp_j,wall+1))



    


n,m=map(int,input().split())
if n==m==1:
    print(0)
    exit()
graph=[list(input().strip()) for _ in range(m)]

bfs()



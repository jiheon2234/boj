import sys
from collections import deque
from itertools import combinations
import copy ####중요!!!
input=sys.stdin.readline
move=[[-1,0],[1,0],[0,-1],[0,1]]
answer=0
def bfs(walls):
    global answer
    tmp_arr=copy.deepcopy(arr)

    
    tmp_answer=len(blank_list)
    for i,j in walls:
        tmp_arr[i][j]=1
        tmp_answer-=1

    que=deque()
    que.extend(virus_list)
    while que:
        i,j=que.popleft()
        for a,b in move:
            tmp_i,tmp_j=i+a,j+b
            if 0<=tmp_i<n and 0<=tmp_j<m and tmp_arr[tmp_i][tmp_j]==0:
                tmp_arr[tmp_i][tmp_j]=2
                tmp_answer-=1
                que.append((tmp_i,tmp_j))
    
    answer=max(answer,tmp_answer)

    
    
    

n,m=map(int,input().split())
arr=[]
virus_list=[]
blank_list=[]
for i in range(n):
    tmp=[* map(int,input().split())]
    arr.append(tmp)
    for j in range(len(tmp)):
        if tmp[j]==2:
            virus_list.append((i,j))
        elif tmp[j]==0:
            blank_list.append((i,j))

wall_comb=list(combinations(blank_list,3))

for walls in wall_comb:
    bfs(walls)
print(answer)

        

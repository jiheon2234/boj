import sys
from collections import deque
input=sys.stdin.readline

def dfs(start):
    one=1
    long_d=0
    visited=[-1 for _ in range(n+1)]
    que=deque([start])

    visited[start]=0
    while que:
        now=que.popleft()
        for next,weight in tree[now]:
            
            if visited[next]==-1:
                visited[next]=visited[now]+weight
                que.append(next)
                if visited[next]>long_d:
                    long_d=visited[next]
                    one=next
    return one,long_d




    



n=int(input())
tree=[[]for _ in range(n+1)]

#트리 채우기
for _ in range(n-1):
    a,b,c=map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

    
one,tresh=dfs(1) #지름중하나, 쓰레기값(거리
print(dfs(one)[1]) #거리만 출력!



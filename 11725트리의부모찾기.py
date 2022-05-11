import sys
from collections import deque
input=sys.stdin.readline

def bfs(root=1):
    que=deque([root])
    
    while que:
        node=que.popleft()
        for next_node in arr[node]:
            if parent[next_node]==-1:
                parent[next_node]=node
                que.append(next_node)
    




n=int(input())
parent=[-1 for _ in range(n+1)]

arr=[[]for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)


bfs()
for p in parent[2:]:
    print(p)

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
from collections import deque

def dfs(node,value):
    global flag
    visited[node]=value
    for i in graph[node]:
        if not visited[i]:
            dfs(i,-value)

        else:
            if value==visited[i]:
                flag=True

        if flag:
            return
        
        


for _ in range(int(input())):
    v,e=map(int,input().split())

    graph=[[]for _ in range(v+1)]
    visited=[False for _ in range(v+1)]
    for _ in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    flag=False
    for i in range(1,v+1):
        if not visited[i]:
            dfs(i,1)
            if flag:
                
                break
    print('NO' if flag else 'YES')
            


    
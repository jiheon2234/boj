import sys
from collections import deque
input=sys.stdin.readline

def bfs(start=1):
    que=deque()
    que.append(start)
    arr[start]=0

    while que:
        now=que.popleft()
        
        for i in range(1,7):
            next=now+i
            if next==100:
                print(arr[now]+1)
                
                exit()
            

            elif next<=100 and arr[next]==-1:
                arr[next]=arr[now]+1
                if next in ladder :
                    if arr[ladder[next]]==-1:
                        arr[ladder[next]]=arr[next]
                        que.append(ladder[next])
                elif next in snake :
                    if arr[snake[next]]==-1:
                        arr[snake[next]]=arr[next]
                        que.append(snake[next])
                else:
                    que.append(next)


                




ladder={}
snake={}
arr=[-1 for _ in range(101)]
n,m=map(int,input().split())
for _ in range(n):
    a,b=map(int,input().split())
    ladder[a]=b
for _ in range(m):
    a,b=map(int,input().split())
    snake[a]=b

bfs(1)











#구현하기 어지럽다 ㅅㅂ
#트리에서 임의의 한 점에서의 최대의 길이는, 항상 지름 중 하나이다!

import sys
from collections import deque
input=sys.stdin.readline


def bfs(start): 
    one=0
    max_val=0
    visited=[-1 for _ in range(v+1)]
    visited[start]=0

    que=deque([start])
    
    while que:
        now=que.popleft()
        for next,weight in arr[now]:
            if visited[next]==-1:
                visited[next]=visited[now]+weight
                if visited[next]>max_val:
                    one=next
                    max_val=visited[next]
                que.append(next)
    return one,max_val #(지름의 정점중 1, <-까지의 최댓값 )
            
    


    


v=int(input())
arr=[[]for _ in range(v+1)]

for _ in range(v):
    tmp=list(map(int,input().strip().split()))
    
    current=tmp[0]
   
    for i in range(1,len(tmp)-1,2):
        arr[current].append([tmp[i],tmp[i+1]])
        #어지럽다진짜

one,max_val=bfs(1)
print(bfs(one)[1])




    

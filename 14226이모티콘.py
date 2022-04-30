import sys
input=sys.stdin.readline
from collections import deque


n=int(input())
visited={}
que=deque()
que.append((1,0))
visited[(1,0)]=0
while que:
    tmp,clip=que.popleft()
    
    #만일 정답에도달하면 출력
    if tmp==n:
        print(visited[tmp,clip])
        exit()
    
    #tmp, tmp이면, tmp인상태에서 클립보드에 복사한거
    #따라서 복사하기전+1
    if (tmp,tmp) not in visited.keys():
        visited[(tmp,tmp)]=visited[(tmp,clip)]+1
        que.append((tmp,tmp))

    ## 만약 현재상태에서 붙여넣기한 상태를 방문하지 않았으면,
    ## 다음 상태는 현재 수,클립보드 +1
    if (tmp+clip,clip) not in visited.keys():
        visited[(tmp+clip,clip)]=visited[(tmp,clip)]+1
        que.append((tmp+clip,clip))
    
    ## 1을빼는경우
    if tmp>0 and(tmp-1,clip) not in visited.keys():
        visited[(tmp-1,clip)]= visited[(tmp,clip)]+1
        que.append((tmp-1,clip))

    


 

    



from collections import deque

#f=총 층, g=스타트링크의 층, s=내가있는층, u=u층위로, d=d층아래로
f,s,g,u,d=map(int,input().split())

arr=[-1 for _ in range(f+1)]

que=deque([s])
arr[s]=0

if s==g:
    print(0)
    exit()

while que:
    now=que.popleft()
    
    for next in (now+u,now-d):
        if 0<next<=f and arr[next]==-1:
            arr[next]=arr[now]+1
            que.append(next)

        if next==g:
            print(arr[next])
            exit()

print("use the stairs")
            
            
            



#https://www.acmicpc.net/problem/13459
import sys
from collections import deque
input=sys.stdin.readline
arr=[]
move=[[-1,0],[1,0],[0,-1],[0,1]]
s=set()
n,m=map(int,input().split())

for i in range(n):
    tmp=list(input().rstrip())
    for j in range(m):
        if tmp[j]=='B':
            blue=(i,j)
            tmp[j]='.'
        elif tmp[j]=='R':
            red=(i,j)
            tmp[j]='.'
        else:
            continue
    arr.append(tmp)
############################# arr만들기

def mv(x,y,dx,dy):
    cnt=0
    
    while arr[x+dx][y+dy] !='#':
        x+=dx
        y+=dy
        cnt+=1
        if arr[x][y]=='O':
            break
    
    return x,y,cnt



def bfs():
    q=deque()
    q.append((red[0],red[1],blue[0],blue[1],0))
    
    while q:
        rx,ry,bx,by,t = q.popleft()
        if t==10:
            print(0)
            exit(0)

        for dx,dy in move:
            rnx,rny,rcnt=mv(rx,ry,dx,dy)
            bnx,bny,bcnt=mv(bx,by,dx,dy)
            if arr[bnx][bny]!='O':
                if arr[rnx][rny]=='O':
                    print(1)
                    exit()
                if rnx==bnx and rny==bny:
                    if rcnt>bcnt:
                        rnx-=dx
                        rny-=dy
                    else:
                        bnx-=dx
                        bny-=dy

                if (rnx,rny,bnx,bny) not in s:
                    s.add((rnx,rny,bnx,bny))
                    q.append((rnx,rny,bnx,bny,t+1))



bfs()
print(0)

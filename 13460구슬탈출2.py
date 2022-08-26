#https://www.acmicpc.net/problem/13460

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
        elif tmp[j]=='O':
            target=(i,j)
        else:
            continue
    arr.append(tmp)
############################# arr만들기

def bfs():
    q=deque()
    q.append((red[0],red[1],blue[0],blue[1],0))
    
    while q:
        rcx,rcy,bcx,bcy,t = q.popleft()

        if t==10:
            # print('10보다 커서 종료')
            print(-1)
            exit()
        for dx,dy in move:
            rnx,rny = rcx,rcy # 다음에 갈 곳
            bnx,bny= bcx,bcy
            R,B=False,False #구멍에 들어갔는지 여부
            #####################################################while문
            while True:
                rflag,bflag=False,False #r,b가 더이상 움직일수 없는가
                if not R : #빨강이 아직 구멍에 안들어갔다면
                    tmp=arr[rnx+dx][rny+dy] # 다음 빨강의 위치
                    if tmp=='O': #구멍에 들어갔을 경우
                        R=t+1 #R만들어줌
                        rnx,rny=-1,-1 #-1로 바꿔서 비교할때 중복 ㅌ
                    elif tmp=='#': #벽일경우
                        rflag=True #더이상 움직일 수 없음

                    else: #움직일 수 있는경우
                        rnx,rny=rnx+dx,rny+dy
                else: # 빨강이 구멍에 들어갔을경우, 조건 만족
                    rflag=True        


                tmp=arr[bnx+dx][bny+dy]  #파란색

                if tmp=='O': #구멍에 들어갔을 경우
                    B=1 # B만들어줌
                    break #볼필요없음

                elif tmp=='#': #벽일경우
                    bflag=True  #더이상 움직일 수 없음

                else: # 움직일 수 있는 경우
                    bnx,bny=bnx+dx,bny+dy
                    
                if rnx==bnx and rny==bny : #만일 서로 같은 위치에 있다면 !!  둘다움직였다면 절대 같은 위치 불가능
                    if bflag: #만일 빨강이 움직였다면
                        rnx,rny= rnx-dx,rny-dy # 이전으로 초기화해줌
                        rflag=True

                    elif rflag:
                        bnx,bny= bnx-dx,bny-dy
                        bflag=True

                if rflag and bflag : #서로 더이상 움직일 수 없는 상태라면
                    break #드디어 종료
               
                
######################################################## While문           
            
            if B: #만일 b가 구멍에 들어갔다면
                continue; #그냥넘김
            elif R: #만일 b가 구멍에들어가지않고 R만 들어갔다면
                # print('R만 들어가서 종료')
                print(R) #출력후 종료
                exit()
                
                

            if (rnx,rny,bnx,bny) not in s: #만일 아무것도 구멍에 안들어갔다면
                q.append(((rnx,rny,bnx,bny,t+1))) #큐에삽입
                s.add((rnx,rny,bnx,bny)) #방문체크

bfs()
# print(s)
# print('끝나서 종료')
print(-1)




                        
                        
                    
                

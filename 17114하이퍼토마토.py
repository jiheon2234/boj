#https://www.acmicpc.net/problem/17114

move1=[1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
move2=[0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
move3=[0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
move4=[0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
move5=[0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0]
move6=[0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0]
move7=[0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0]
move8=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0]
move9=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0]
move10=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0]
move11=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1]






# def bfs(m, n, o, p, q, r, s, t, u, v, w):
def bfs():
    while que:
        
        ww,vv,uu,tt,ss,rr,qq,pp,oo,nn,mm,value=que.popleft()
        for i in range(22):
            mmm=    mm+move1[i]
            nnn=    nn+move2[i]
            ooo=    oo+move3[i]
            ppp=    pp+move4[i]
            qqq=    qq+move5[i]
            rrr=    rr+move6[i]
            sss=    ss+move7[i]
            ttt=    tt+move8[i]
            uuu=    uu+move9[i]
            vvv=    vv+move10[i]
            www=    ww+move11[i]
           
            if 0<=mmm<m and 0<=nnn<n and 0<=ooo<o and 0<=ppp<p and 0<=qqq<q and 0<=rrr<r and \
                0<=sss<s and 0<=ttt<t and 0<=uuu<u and 0<=vvv<v and 0<=www<w and\
                arr[www][vvv][uuu][ttt][sss][rrr][qqq][ppp][ooo][nnn][mmm] =='0':
                    que.append([www,vvv,uuu,ttt,sss,rrr,qqq,ppp,ooo,nnn,mmm,value+1])
                    arr[www][vvv][uuu][ttt][sss][rrr][qqq][ppp][ooo][nnn][mmm]='-1'

    for ww in range(w):
        for vv in range(v):
            for uu in range(u):
                for tt in range(t):
                    for ss in range(s):
                        for rr in range(r):
                            for qq in range(q):
                                for pp in range(p):
                                    for oo in range(o):
                                        for nn in range(n):
                                            for mm in range(m):
                                                
                                                if arr[ww][vv][uu][tt][ss][rr][qq][pp][oo][nn][mm]=='0':
                                                    print(-1)
                                                    return
    print(value)



import sys
input=sys.stdin.readline
from collections import deque
m, n, o, p, q, r, s, t, u, v, w=map(int,input().split())

arr=[
    [[[[[[[[[list(input().split()) for _ in range(n)
    ] for _ in range(o)
    ] for _ in range(p)
    ] for _ in range(q)
    ] for _ in range(r)
    ] for _ in range(s)
    ] for _ in range(t)
    ] for _ in range(u) 
    ] for _ in range(v)
    ] for _ in range(w)   
]

que=deque()
for ww in range(w):
    for vv in range(v):
        for uu in range(u):
            for tt in range(t):
                for ss in range(s):
                    for rr in range(r):
                        for qq in range(q):
                            for pp in range(p):
                                for oo in range(o):
                                    for nn in range(n):
                                        for mm in range(m):
                                            # print('test',ww,vv,uu,tt,ss,rr,qq,pp,oo,nn,mm)
                                            if arr[ww][vv][uu][tt][ss][rr][qq][pp][oo][nn][mm]=='1':
                                                
                                                que.append([ww,vv,uu,tt,ss,rr,qq,pp,oo,nn,mm,0])
                                                arr[ww][vv][uu][tt][ss][rr][qq][pp][oo][nn][mm]='-1'


bfs()

#머리가나쁘면 컴퓨터가 고생한다.

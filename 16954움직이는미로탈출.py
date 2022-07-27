# https://www.acmicpc.net/problem/16954
import sys
input=sys.stdin.readline
from collections import deque
move=[[-1,0],[1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1],[0,0]]
wall=set()
for i in range(8):
    tmp=list(input().rstrip())
    for j in range(8):
        if tmp[j]=='#':
            wall.add((i,j))

q=deque([(7,0)])


for _ in range(7):
    qq=set()
    while q:
        cx,cy=q.popleft()
        
        for a,b in move:
            nx,ny=cx+a,cy+b
            if 0<=nx<8 and 0<=ny<8 and(nx,ny) not in wall:
                qq.add((nx,ny))

    wall={(x[0]+1,x[1]) for x in wall if x[0]<7} #벽 이동
    if not wall: #벽이없으면 무조건 갈 수 있다.
        print(1)
        exit()
    qq-=wall #벽이랑 곂치는 부분 제외하기
    if not qq: #더 나아갈 부분이 없으면 못가는거
        print(0)
        exit()
    
    for qqq in qq:
        q.append(qqq)

print(1)


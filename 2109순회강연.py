# https://www.acmicpc.net/problem/2109
import sys
from heapq import *
input =sys.stdin.readline
n=int(input())
lect=sorted([[* map(int,input().split())]for _ in range(n)], key=lambda x: x[1]) #날짜기준으로 정렬
h=[] #최소힙
for p,d in lect:
    heappush(h,p) # 일단 무조건 힙에 pay를 넣는다.
    if len(h)>d: #만약, 강의가 모두 잡혀있는 상태라면
        heappop(h) # 가장 pay가 적은 강의를 뺀다
print(sum(h))

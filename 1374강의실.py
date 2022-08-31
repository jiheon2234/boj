#https://www.acmicpc.net/problem/1374
import sys
import heapq


input = sys.stdin.readline
lect, h = [], [] #강의들(시작시간기준) , 강의실(끝나는시간 기준)
answer = []
n = int(input())
for _ in range(n): # 강의를 시작하는순서대로 정렬
    a, b, c = map(int, input().split())
    heapq.heappush(lect, (b, c))
heapq.heappush(h, heapq.heappop(lect)[1]) #가장 빨리 시작하는 강의를 강의실에 배정
while lect: 
    start, end = heapq.heappop(lect)  
    if start >= h[0]:  #만일 가장 빨리끝나는강의실보다 같거나 늦게 시작한다면,
        heapq.heappop(h) #가장빠른강의실에
        heapq.heappush(h, end) #새로운강의를 배치함 heap성질에 의해서 정렬될것임
    else: #만일 가장 빨리끝나는강의실보다 빨리 시작한다면
        heapq.heappush(h, end) #새 강의실을 배정해야함
print(len(h))

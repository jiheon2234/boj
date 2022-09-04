#https://www.acmicpc.net/problem/1202
import sys
import heapq

input = sys.stdin.readline
jul = []
n, k = map(int, input().split())
for _ in range(n):
    heapq.heappush(jul, [*map(int, input().split())])
bag = [int(input()) for _ in range(k)]  # 작은순서대로 정렬
bag.sort()
h = []
answer = 0
for b in bag:
    while jul and jul[0][0] <= b:  # 가방에 담을수 있는 모든 보석
        heapq.heappush(h, -heapq.heappop(jul)[1])  # 무게만 담기

    if h:  # 만일 담을수 있는 보석이 있다면
        answer -= heapq.heappop(h)  # 현재 가방에 담을 수 있는 보석 중 가장 가치높은 보석만 꺼내기
print(answer)

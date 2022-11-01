# https://www.acmicpc.net/problem/13904
import sys

input = sys.stdin.readline
n = int(input())
hw = []
visit = [False] * 1001

for _ in range(n):
    d, w = map(int, input().split())
    hw.append((d, w))
hw.sort(key=lambda x: x[1], reverse=True)  # 무조건 weight가 크게 정렬함
answer = 0

for d, w in hw:
    while d > 0 and visit[d]:  # 과제를 할 수 있는 최대한의 날짜를 찾는다
        d -= 1  # 처음d값은 날짜이고, 이후 d날에 이미 과제를 했다면 그전 과제를 할 수 있는 날짜를 구한다..
    if d:  # 만일 과제를 할 수 있을경우 (w기준 최댓값순으로 정렬했으므로)
        visit[d] = True  # 그날에 과제를 한다.
        answer += w
print(answer)


# import sys
# from heapq import heappush, heappop

# input = sys.stdin.readline
# h = []
# hw = sorted([[*map(int, input().split())] for _ in range(int(input()))])
# for d, w in hw:
#     heappush(h, w)
#     if d < len(h):
#         heappop(h)
# print(sum(h))

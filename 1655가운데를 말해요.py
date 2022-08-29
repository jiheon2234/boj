# https://www.acmicpc.net/problem/1655
import sys
import heapq

input=sys.stdin.readline
left,right=[],[] #최대힙, 최소힙 중간값을 left의 root로 할거임
n=int(input().rstrip())
for _ in range(n):
    num=int(input().rstrip())

    if len(left)==len(right):
        heapq.heappush(left,-num)
    else:
        heapq.heappush(right,num)

    if right and  -left[0] > right[0]: #만일 left의 루트, 즉 중간값이 right의 루트, right의 최솟값보다 크다면
        lr=-heapq.heappop(left)
        rr=-heapq.heappop(right)
    ##각각의 루트를 바꿔준다. (중간값을 바꾸기 위해서)
        heapq.heappush(right,lr)
        heapq.heappush(left,rr)

    print(-left[0])
        

        
    

    


        

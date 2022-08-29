# https://www.acmicpc.net/problem/2696
import sys
import heapq
input=sys.stdin.readline

t=int(input().rstrip())
for _ in range(t):
    m=int(input().rstrip())
    a,b=divmod(m,10)
    if b:
        a+=1
    arr=[]
    for __ in range(a):
        arr+=[* map(int,input().rstrip().split())]
    print(len(arr)//2+1)

    left,right = [],[]
    tmp=[]
    for i in range(len(arr)):
        
        if len(left)==len(right):
            heapq.heappush(left, -arr[i])
        else:heapq.heappush(right, arr[i])

        if right and -left[0] > right[0]:
            heapq.heappush(left, -heapq.heappop(right))
            heapq.heappush(right, -heapq.heappop(left))
        if not i%2:
            tmp.append(-left[0])

        if len(tmp)==10:
            for tmptmp in tmp:
                print(tmptmp, end=' ')
            tmp=[]

    if tmp:
        for tmptmp in tmp:
            print(tmptmp, end=' ')

        

            

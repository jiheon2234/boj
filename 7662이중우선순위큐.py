# https://www.acmicpc.net/problem/7662

import heapq
import sys
from heapq import *
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    minh, maxh, dd = [], [], defaultdict(int)
    for _ in range(k):
        a, b = input().rstrip().split()
        b = int(b)

        if a == "I":
            heappush(minh, b)
            heappush(maxh, -b)
            dd[b] += 1

        else:
            if b == 1:  # 최댓값을 삭제하는 연산이라면
                while True:
                    try:
                        tmp = -heappop(maxh)
                        if dd[tmp] > 0:
                            dd[tmp] -= 1
                            break
                    except:
                        break
            elif b == -1:  # 최소값을 선택하면
                while True:  # 삭제된 값이 아닐때까지
                    try:
                        tmp = heappop(minh)
                        if dd[tmp] > 0:
                            dd[tmp] -= 1
                            break
                    except:
                        break

    try:
        while True:
            minval = heappop(minh)
            if dd[minval]:
                break
    except:
        print("EMPTY")
        continue
    while True:
        maxval = -heappop(maxh)
        if dd[maxval]:
            break
    print(maxval, minval)


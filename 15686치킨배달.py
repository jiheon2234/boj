
import sys

from itertools import combinations

input=sys.stdin.readline




n,m=map(int,input().split())
arr=[]
chickenhouse=[]
blank=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(n):

        if tmp[j]==1:
            blank.append((i,j))

        elif tmp[j]==2:
            chickenhouse.append((i,j))

chicken_comb=combinations(chickenhouse,m)
answer=1e+7
for chickens in chicken_comb:
    dist=0
    for i,j in blank:
        dist+=min([abs(i-c[0])+abs(j-c[1]) for c in chickens])
        if dist>=answer:break
    answer=min(answer,dist)
print(answer)
        




            
    

# https://www.acmicpc.net/problem/14395
from collections import deque

s,t = map(int,input().split()) #입력받고
visit=set() #방문처리
if s==t: #같으면0
    print(0)
    exit()
elif t==0: #t가0이면 -
    print('-')
    exit()
elif t==1: #t가1이면 /
    print('/')
    exit()
elif s==0 : #s가 0이면 뭔짓을해도안됨
    print(-1)
    exit()
elif s**2==t:
    print('*')
    exit()
elif s+s==t:
    print('+')
    exit()

q=deque() #
q.append((s**2,'*'))
q.append((s*2,'+'))
q.append((1,'/'))

while q:
    now,ca=q.popleft()
    tmp=(now**2,now*2)
    for i in (0,1) :
        next=tmp[i]
        qqq= '*+'[i==1]
        if next==t:
                print(ca+qqq)
                exit()
        elif next<t and next not in visit:
           
            visit.add((next))
            q.append((next,ca+qqq))


print(-1)

        

#https://www.acmicpc.net/problem/1461
n,m= map(int,input().split())
arr=[*map(int,input().split())]

plus,minus=[],[]
for a in arr:
    if a>0:
        plus.append(a)
    else:
        minus.append(abs(a))

plus.sort(reverse=True)
minus.sort(reverse=True)
answer=0
max_val=0
for ttt in (plus,minus):
    if ttt:
        a,b=divmod(len(ttt),m)
        for i in range(a):
            answer+=ttt[i*m]*2
        if ttt:tmp=ttt[0]
        if b:
            answer+=ttt[a*m]*2
        max_val=max(max_val,tmp)

print(answer-max_val)
    

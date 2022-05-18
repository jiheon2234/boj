import sys
from itertools import combinations
input=sys.stdin.readline


n,k=map(int,input().split())
must_have=0
comb=list(range(26))
for w in ('a','n','t','i','c'):
    bn=(ord(w)-ord('a'))
    must_have|=1<<bn
    comb.remove(bn)

word_list=[]
for _ in range(n):
    tmp=0
    wo=list(set(input().strip()))
    for w in wo:
        b= 1<<(ord(w)-ord('a'))
        tmp |= b
    tmp&= ~(must_have)
    word_list.append(tmp)
if k<5:
    print(0)
    exit()

    

teaches=combinations(comb,k-5)
answer=0
for teach in teaches:
    tmp_answer=0
    tmp=0
    for t in teach:
        tmp |= 1<<t
    for word in word_list:
        if (word&tmp)==word:
            tmp_answer+=1

    if tmp_answer>answer:
        answer=tmp_answer

print(answer)



a,b=map(int,input().split())

arr=[True for _ in range(b-a+1)]

num=2
while True: 
    square=num**2

    if square>b:
        break

    start,w=divmod(a,square)
    if w!=0 :
        start+=1

    while True:
        tmp=square*start
        if tmp>b:
            break
        arr[tmp-a]=False
        start+=1
    num+=1

print(sum(arr))


    
    


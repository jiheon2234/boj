import sys
input=sys.stdin.readline
n,k=map(int,input().split())
dp=[0 for _ in range(k+1)]
# dp[i]= 무계가 i일때의 최댓값
for _ in range(n):
    w,v=map(int,input().split())
    for i in range(k,w-1,-1): #이전값들을 써먹기 위해뒤에서부터 돌면서
                            #만일 w>=k이면, 반복문안돔
        dp[i]=max(dp[i],dp[i-w]+v) 
        # 무계가 i일때의 최댓값은
        # {지금 주어진물건을 포함하지 않았을때의 최댓값과
        # 무계가 i-w 즉 지금물건을 포함할 수 있는 경우 +지금물건의 가치}
        # 의 최댓값이다.
        print(dp)

        
import sys
input =sys.stdin.readline
moves=[(-1,0),(1,0),(0,-1),(0,1)]

    

def dfs(i,j,depth=1,v=0):
    global answer
    global max_val
    if answer >= v+max_val*(4-depth):
        return
   
    if depth==4:
        answer=max(answer,v)
      
        return


    for move in moves:
        tmp_i= i+move[0]
        tmp_j= j+move[1]
        if 0<=tmp_i<n and 0<=tmp_j<m and not visited[tmp_i][tmp_j]:
            if depth==2: #볼록모양
                visited[tmp_i][tmp_j]=True
                dfs(i,j,depth+1,v+arr[tmp_i][tmp_j])
                visited[tmp_i][tmp_j]=False


            visited[tmp_i][tmp_j]=True
            dfs(tmp_i,tmp_j,depth+1,v+arr[tmp_i][tmp_j])
            visited[tmp_i][tmp_j]=False
    return
        
        


    
    
    
    


answer=0
n,m=map(int,input().split())
arr=[[* map(int,input().split())]for _ in range(n)]
max_val=max(map(max,arr))
visited=[[False for _ in range(m)]for _ in range(n)]

for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i,j,1,v=arr[i][j])
        visited[i][j]=False
print(answer)

import sys
from collections import deque
input=sys.stdin.readline
move=((-1,0),(1,0),(0,-1),(0,1))

def bfs(fire,jihun):
    que=deque()
    
    for f in fire:
        que.append(f)
    que.append(jihun)

    

    while que:
        i,j,t=que.popleft()
    
        for a,b in move:
            tmp_i,tmp_j=i+a,j+b
            if 0<=tmp_i<R and 0<=tmp_j<C and arr[tmp_i][tmp_j]=='.':
                if t==-1:
                    que.append((tmp_i,tmp_j,t))
                    arr[tmp_i][tmp_j]='F'
                else:
                    if tmp_i==R-1 or tmp_i==0 or tmp_j==C-1 or tmp_j==0 :
                        # for k in arr:
                        #     print(k)
                        print(t+2)
                        exit()
                   

                    que.append((tmp_i,tmp_j,t+1))
                    arr[tmp_i][tmp_j]='J'
                    

    print("IMPOSSIBLE")
                

        

R,C=map(int,input().split())
arr=[]
for _ in range(R):
    arr.append(list(input().strip()))

fire=[]
for i in range(R):
    for j in range(C):
        
        if arr[i][j]=='J':
            arr[i][j]='@'
            jihun=((i,j,0))
            if i==0 or j==0 or i==R-1 or j==C-1:
                
                print(1)
                exit()

        elif arr[i][j]=='F':
            fire.append((i,j,-1))
            


bfs(fire,jihun)



        

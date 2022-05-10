import sys
input=sys.stdin.readline

class Node:
    def __init__(self,data,left,right,parent):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent

position=0 #가장 왼쪽부터1씩증가시키면서번호매기기
result={} #레벨에 따른 노드들위치 
def inorder(node,level=1): #중위순회
    global position 
    if node.left !=-1:
        inorder(tree[node.left],level+1)

    position+=1 #가장왼쪽부터 증가
    if level in result:
        result[level].append(position)
    else:
        result[level]=[position]
        
    if node.right != -1:
        inorder(tree[node.right],level+1)
        

n=int(input())

tree={}
#각 노드의 자기자신,left,right,parent업데이트하기
for _ in range(n):
    data,left,right=map(int,input().split())
    tree[data]=Node(data,left,right,-1)
#tree가완성되지않은상태에서하면 valueerror
for i in range(1,n+1):
    if tree[i].left != -1:
        tree[tree[i].left].parent=data
    if tree[i].right != -1:
        tree[tree[i].right].parent=data
#루트찾기
for i in tree.keys():
    if tree[i].parent==-1:
        root=i
        break;
#중위순회하면서, result에 level별 노드위치 업데이트
inorder(tree[root])
answer_idx=1
answer=-19
#가장긴것 찾기 (같으면 업데이트 x)
for i in sorted(result.keys()):
    tmp=max(result[i])-min(result[i])
    if tmp>answer:
        answer_idx=i
        answer=tmp
print(answer_idx,answer+1)


def check(strnum):
    num=int(strnum)
    if num%2==0: return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True

first=['2','3','5','7',]
def dfs(strnum): # str
    if len(strnum)==n:
        print(strnum)
        return

    for i in (1,3,5,7,9):
        tmp=strnum+str(i)
        if check(tmp):
            dfs(tmp)


n=int(input())
for start in first:
    dfs(start)

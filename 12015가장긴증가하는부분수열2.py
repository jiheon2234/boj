# https://www.acmicpc.net/problem/12015

n = int(input())
a = list(map(int, input().split()))
lis = [0]
for i in a:
    if lis[-1] < i:  # 만일 lis의 마지막 숫자가 i보다 작을 경우
        lis.append(i)  # 추가
    else:  # 이분탐색해서 가장 잘 어울리는 위치에 넣기
        start, end = 0, len(lis)
        while start < end:
            mid = (start + end) // 2
            if lis[mid] < i:
                start = mid + 1
            else:
                end = mid 
        lis[start] = i
print(len(lis) - 1)



# from bisect import bisect_left

# n = int(input())
# a = list(map(int, input().split()))
# res = [0]

# for i in a:
#     if res[-1] < i:
#         res.append(i)
#     else:
#         res[bisect_left(res, i)] = i
# print(len(res)-1)

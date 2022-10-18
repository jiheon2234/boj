#https://www.acmicpc.net/problem/1654
import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start, end = 1, max(lan)
while start <= end:  # 범위가 벗어나지 않을때까지 반복하면서
    mid = (start + end) // 2  # 이분탐색을 위한 중간값
    cnt = 0
    for l in lan:
        cnt += l // mid  # 만들 수 있는 총 갯수
    if cnt >= n:  # 만들수 있는 갯수보다 크다면, 랜선길이의 최솟값을 mid로 잡고 다시 반복 (같아도 최댓값을 구하기 때문에 계속)
        start = mid + 1 #무한반복을 피하기 위함
    else:  # 갯수만큼 만들 수 없다면, 랜선길이의 최댓값을 mid로 잡고 다시 반복
        end = mid - 1 

print(end)

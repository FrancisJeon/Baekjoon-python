# 최소, 최대 210924, 210927
# 1차 588ms
# 11개월 전에 min, max를 사용한 코드
# 2차 444ms
# n = int(input()); nums = list(map(int, input().split()))
# print(min(nums), max(nums))

# 3차 744ms, sort 후 인덱싱 하는것보다 min, max 함수를 쓰는게 더 빠르다.
# n = int(input()); nums = list(map(int, input().split()))
# nums.sort()
# print(nums[0], nums[-1])

# 4차 572ms(sys), 596ms(input) 일부러 O(N) 한번만 이동하면서 min과 max를 둘다 찾는 함수를 사용. 그렇게 빠르진 않다
from sys import stdin
input = stdin.readline
n = int(input())
num = list(map(int, input().split()))
min = 9999999
max = -9999999
for i in range(n):
    if num[i] < min: min = num[i]
    if num[i] > max: max = num[i]
print(min, max)
# 최댓값, 210924 개선판?
# 9개의 서로 다른 자연수 중 최댓값을 찾고 입력 몇번째 인지 찾기

# 1차
'''
l = []

for i in range(9):
    l.append(int(input()))

print(max(l))
print(l.index(max(l))+1))
'''

# 2차 - 2차 버전이 더 나아진건 아니고 1차 코드를 단축시킨 3차코드를 숏코딩 보고 생성
'''
lst = [int(input()) for i in range(9)]
enum = [(n, i+1) for i, n in enumerate(lst)]
enum.sort(reverse=True)
print(enum[0][0])
print(enum[0][1])
'''

# 3차
l = [int(input()) for _ in range(9)]
print(max(l), l.index(max(l))+1)

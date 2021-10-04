# 좌표 압축 211001
""" 
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
* 각 숫자들을 순서대로 정렬해서 replace 해준다. 같은 숫자는 같은 순서를 가진다.
# idx = [(n, i) for i, n in enumerate(sorted(set(coord)))] -> 좌표값들을 enum 함수를 사용해서 튜플 형태로 변경
"""
# 1번 제출, 2000ms(python) 1144ms(pypy, no readline), import sys 여부와 관계없이 2000ms 언저리에서 해답이 나왔다.
# import sys
# input = sys.stdin.readline
# n = int(input())
# coord = list(map(int, input().split()))
# d = {n:i for i,n in enumerate(sorted(set(coord)))} # 이렇게 딕셔너리를 컴프리헨션으로 제작하는게 가능하다는걸 오늘 처음 활용했다.
# for i, n in enumerate(sorted(set(coord))): # 13번 줄 컴프리헨션과 동일한 반복문
#     d[n] = i 
# answer = list(map(lambda x: d[x], coord))
# print(*answer)

# 2번 답, 은 answer의 map 함수를 만든 뒤 변수에 담아준 1번과 다르게 바로 출력시켰다.
# print(*map(lambda x: d[x], coord))

# 3번 제출, 숏코딩 응용
input()
n=[*map(int, input().split())] 
d = {j:i for i,j in enumerate(sorted(set(n)))} # set함수도 줄이기 위해 {}에 감싸준듯
print(*[d[i] for i in n])

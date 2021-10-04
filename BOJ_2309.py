# 일곱 난쟁이 210927
""" 
아홉 난쟁이의 키가 주어지면 이중 7명을 찾아야 하는데 키는 100을 넘지 않아야 하고 여러가지 정답일 때는 아무거나 출력
출력은 오름차순으로
분류: 브루트포스 알고리즘

알고리즘: 9명의 합을 구한다음 100에서 빼서 나머지 두명의 합이 100이 나오는 케이스만 찾아야함
"""
h = [ int(input()) for _ in range(9) ]
h.sort() # sorting을 하면 한결 편해질 듯
total = sum(h)
target = total - 100 # 100이 최대 합이므로 두명의 합이 target 보다 작다면 그 조합은 괜찮은 조합이다.

def find_target():
    for i in range(9): # 2중 for문을 통해서 
        for j in range(i+1, 9):
            if (h[i] + h[j]) == target:
                del h[j]
                del h[i]
                return
find_target()
for i in h:
    print(i) 

# 짧은 정답 코드 
a = [int(input()) for _ in range(9)]
a.sort()

for i in range(9):
    for j in range(i + 1, 9):
        if sum([a[k] for k in range(9) if k not in (i, j)]) == 100:
            [print(a[k]) for k in range(9) if k not in (i, j)]
            exit()

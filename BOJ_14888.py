# 연산자 끼워넣기 210928
""" 
입력
N 첫줄 수의 개수
둘째 줄에는 A1....An 의 배열이 주어진다
셋째 줄에는 합이 N-1인 정수 4개가 주어지는데 차례대로 +, -, *, /의 개수이다. (나눗셈은 몫만 취한다.)

샛째 줄의 연산자들을 활용해서 최댓값, 최솟값을 만들어서 출력하자

* 알고리즘, 주의사항
나눗셈의 경우 몫만 취한다고 했는데 음수의 경우도 생각해야 한다.
이로인해 // 연산자를 직접 사용하는것 보다 int(a/b) 함수를 사용하는게 더 낫다
"""
# 블로그에서 본 재귀 함수
from itertools import permutations
def cal(num, idx, add, sub, multi, division):
    global n, maxv, minv
    if idx == n:
        maxv = max(num, maxv)
        minv = min(num, minv)
        return
    else:
        if add:
            cal(num + num_list[idx], idx + 1, add-1, sub, multi, division)
        if sub:
            cal(num - num_list[idx], idx + 1, add, sub-1, multi, division)
        if multi:
            cal(num * num_list[idx], idx + 1, add, sub, multi-1, division)
        if division:
            cal(int(num/num_list[idx]), idx + 1, add, sub, multi, division-1)
    
if __name__ == "__main__":
    maxv = -float('inf')
    minv = float('inf')

    n = int(input())
    num_list = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    cal(num_list[0], 1, add, sub, mul, div)
    print(maxv)
    print(minv)

# 답지에 있던 dfs 함수 (비슷한데 약간 달라서 복붙)
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_v = 1e9
max_v = -1e9

def dfs(i, now):
    global min_v, max_v, add, sub, mul, div
    if i == n:
        min_v = min(min_v, now)
        max_v = max(max_v, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, int(now * data[i]))
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1


dfs(1, data[0])

print(max_v)
print(min_v)

# permutation을 활용한 답지, 숏코딩
N = int(input())
A = list(map(int, input().split()))
a, s, m, d = map(int, input().split())

rs = list()
for p in set(permutations('+'*a+'-'*s+'*'*m+'/'*d)):
    r = A[0]
    for i in range(1, N):
        r = {'+': r+A[i], '-': r-A[i], '*': r*A[i], '/': int(r/A[i])}[p[i-1]]

    rs.append(r)

print(max(rs), min(rs))

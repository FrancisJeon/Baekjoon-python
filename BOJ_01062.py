# 가르침 210930 브루트포스, 백트래킹
""" 
k개의 글자를 가지고 만들 수 있는 단어들의 개수를 최대한 가져오기
anta tica에 포함된 'antic' 도 알파벳에 포함인건가 햇갈린다. 이럴 경우 antic에 5개가 들어가면서 5개 이하의 케이스는 전부 무시해야 한다.

입력
N K 입력숫자, 단어 수
antaarctica
antahellotica
antacartica
출력 
2

* arr = [set(input()) - set('antic') for i in range(n)] 
# input을 집합자료형으로 받아서 antic과 차집합을 해주면 처음부터 알파벳만 담은 집합들의 리스트가 생성된다.

* 비트 마스크 -> 정수의 이진수 표현을 활용한 기법으로 정수의 각 요소를 인덱스처럼 표현한다.
만약 i번째 요소가 부분집합에 존재하면 1을 넣고 그렇지 않으면 0을 넣는다.
예를들어 알파벳의 경우
z->a 0*26 의 숫자로 표현한 다음 포함된 단어들을 1로 표현해준다.
z -> 10000 00000 00000 00000 00000 0
a -> 00000 00000 00000 00000 00000 1
And 연산 & -> 두 곳이 모두 1이면 1을 반환
Or 연산 | -> 두 곳중 하나만 1이면 1을 반환
* 비트 형태로 만드는 방법 << 를 활용한다.
예를들어 A를 넣는다면 cur = 0b0; cur = cur | (1 << ord('a') - ord('a'))



* 알고리즘
1. 단어를 글자 단위로 쪼갠 후 중복 제거 후 반복자로 바꿔주기(튜플이 좋을 것 같다.)
2. 이렇게 만들어진 새로운 리스트를 가지고 ord를 활용해서 비트연산 형태로 바꿔주자.
3. 비트연산을 성공적으로 했는데 문제는 그 다음 조합을 어떻게 만들지 모르겠다. -> 정답 제출하고 답지 보기로

"""

# 시도
'''
import sys
input = sys.stdin.readline

def bit_mask(array):
    bits = []
    for i in array:
        cur = 0
        # 모든 원소를 아스키 값으로 바꿔준다.
        l = [ord(j)-ord('a') for j in i]
        for j in l:
            cur = cur | (1 << j)
        bits.append(bin(cur))
    print(bits)
# 이렇게 따로 반복문 여러번 쓰게 만들지 말고 처음부터 비트마스크를 해서 그 형태를 넣어주자
    

n, k = map(int, input().split())
arr = []
for _ in range(n): # n 개의 입력값을 비트연산 해준다.
    cur = list(input().rstrip())
    bit = 0
    for i in cur:
        bit = bit | (1 << ord(i) - ord('a'))
    arr.append(bit)
# print(arr) # 비트연산을 해준 10진수 형태가 담겨있다.
'''

# 정답코드 2000ms, 블로그, 제출을 이걸로 했는데 맘에들진 않는다.
'''
import itertools
from itertools import combinations
n, k = map(int, input().split())
if k < 5:
    print(0)
else:
    k -= 5
    nece_chars = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    alpha = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z')+1))) - nece_chars))}
    cnt = 0
    for _ in range(n):
        tmp = 0
        for c in set(input())-nece_chars:
            tmp |= (1 << alpha[c])
        input_chars.append(tmp)
    power_by_2 = (2**i for i in range(21))
    for comb in combinations(power_by_2, k):
        test = sum(comb)
        
        ct = 0
        for cb in input_chars:
            if test & cb == cb:
                ct += 1
        cnt = max(cnt, ct)
    print(cnt)
'''
    
# 숏코딩, 500ms
import itertools
n, k = map(int, input().split()) # input값을 받아서 set 형태로 삽입
arr = [set(input()) for __ in range(n)]

commons = set('antatica') # 공통 5개를 포함한 antatica set와 처음 넣은 set를 차집합을 구해준다.
ts = sorted(set(chr(cc) for cc in range(ord('a'), ord('z') + 1)) - commons)
# 기본 알파벳만 빠진 ts라는 set를 생성해준다. ('a'~'z') - commons

res = 0


arr = [sum(1 << ord(c) - ord('a') for c in y) for y in arr] 
# 단어 목록에서 y를 뽑고 그 안에 있는 단어들 c를 전부 비트연산 시켜준 뒤 합쳐줌?
# 결과로 모든 단어 별로 비트연산이 성공했다. sum을 해도 괜찮은 이유는 각 연산마다 특정 자리에 위치하기 때문에 합쳐도 비트 위치가 꼬이지 않는다.

commons = sum(1 << ord(c) - ord('a') for c in commons)
# common(antatica) 들을 비트연산 시켜줌
ts = [1 << ord(c) - ord('a') for c in ts]
# ts는 sorted된 곳으로 a~z의 세트이다. 11111111111이 만들어짐

for z in [commons | sum(t) for t in (itertools.combinations(ts, k - 5) if k >= 5 else ())]: # common과 | 비트 or로 sum('a'-'z'의 k-5개 combination)을 해주면 나오는 조합이 있는데
    res = max(res, sum((z & y) == y for y in arr)) # 그 값들을 arr에서 y와 & 연산을 시켜준 값들 중 최고로 큰 값을 res에 담아준다. (최대 조합)
# ts로 21개 알파벳으로 만들어진 내용중 combinations로 2개의 조합을 sum 한 값과 common을 더해주었는데 (antatica) 나는 antatica를 이미 빼주었기 때문에 이부분은 그냥 ts로만 조합을하면 될 것 같다.
# 그리고 이렇게 만들어진 조합들은 리스트에서 반복문을 돌면서 arr의 값들을 하나씩 빼준 뒤 (z & y) == y 가 되는 부분들의 sum 중에 max를 챙긴다? 
# (z&y)? 이렇게 하면 둘 중 1의 위치가 겹치는 곳 만 나오는데 ts의 조합이 전부 y에 포함된 경우라면 True라서 1이 나온다. 이 Sum의 True 갯수가 배울수 있는 모든 조합인듯..?
print(res)

# 위 코드 더 단축시키기, pypy 1224 python 2092
'''
input = sys.stdin.readline

n, k = map(int, input().split())
commons = set('antatica')
arr = [set(input().rstrip()) - commons for _ in range(n)]
ts = sorted(set(chr(c) for c in range(ord('a'), ord('z') + 1)) - commons)
ts = [1 << ord(c) - ord('a') for c in ts]

res = 0
arr = [sum(1 << ord(c) - ord('a') for c in y) for y in arr]

for z in [sum(t) for t in (combinations(ts, k - 5) if k >= 5 else ())]:
    res = max(res, sum((z & y) == y for y in arr))
print(res)
'''


# 숏코딩 200ms
'''
read = sys.stdin.readline
n, k = map(int, read().strip().split())


def get_bit(word):
    ret = 0
    for e in word:
        ret |= 1 << (ord(e) - ord('a'))
    return ret


words = list(map(lambda x: get_bit(x), [read().strip() for _ in range(n)]))
essential = get_bit('antic')
answer = 0


def get_can_learn(cnt):
    if cnt < 0:
        return []
    return combinations(list(filter(lambda x: x not in 'antic', map(lambda x: chr(x + ord('a')), range(26)))), cnt)


for i in get_can_learn(k - 5):
    i = get_bit(i) | essential
    cnt = 0
    for word in words:
        if word & i == word:
            cnt += 1
    answer = max(answer, cnt)

print(answer)
'''

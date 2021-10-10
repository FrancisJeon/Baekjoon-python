# 애너그램 211005
""" 
글자가 주어지면 글자의 구성요소 그대로 순서를 바꾸면 다음 글자를 작성할 수 있는 경우를 애너그램이라고 한다.
애너그램 여부 확인하기

* 알고리즘
1. Counter를 활용하는게 제일 빠를것 같다.
2. 만약 Counter를 떠올리지 못한다면 set로 만들어서 갯수를 담은 array를 만들면 될 것 같다.
3. sum(ord())로 만드는 방법도 있었다.

* 팁
## Q. 딕셔너리 형태로 카운터 변수가 만들어진다. 둘을 바로 비교할 수 있을까?
A. Counter 변수는 바로 비교가 가능하다.
## print(f'{words[0]} & {words[1]} are {"" if is_anagram else "NOT "}anagrams.')
f-string 내부에서 연산을 활용하면 출력에서 조건문도 더 간결하게 만들 수 있다. 하지만 "" 와 ''의 중첩을 피해야 하고 {}뒤에 딱 붙여서 써야 한칸이 떨어지게 출력되는 점을 주의해야 한다.
"""
# Counter 방식
# from collections import Counter
# for _ in range(int(input())):
#     a, b = map(str, input().split())
#     # 애너그램 비교
#     A = Counter(a); B = Counter(b)
#     print(f'{a} & {b} are {"" if A == B else "NOT "}anagrams.')

# set 활용 -> 속도와 메모리에서 살짝 개선이 있었다.
# for _ in range(int(input())):
#     a, b = map(str, input().split())
#     cnt_a = [(i, a.count(i)) for i in sorted(set(a))]
#     cnt_b = [(i, b.count(i)) for i in sorted(set(b))]
#     print(f'{a} & {b} are {"" if cnt_a == cnt_b else"NOT "}anagrams.')
    
# defaultdict 활용
from collections import defaultdict
for _ in range(int(input())):
    d_a, d_b = defaultdict(int), defaultdict(int)
    a, b = map(str, input().split())
    for i in a:
        d_a[i] += 1
    for i in b:
        d_b[i] += 1
    print(f'{a} & {b} are {"" if d_a == d_b else "NOT "}anagrams.')


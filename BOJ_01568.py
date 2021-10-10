# 새 211005
""" 
자연수를 배우는 새
1부터 시작해서 자연수가 오름차순으로 증가하고 동시에 같은 수의 새가 날아간다
모든 새가 날아가는데 몇초 걸리는지 계산

* 알고리즘
1. 1+2+3.... 목표치보다 같거나 커지는 순간 그 숫자를 출력
1-1. 남아있는 새의 숫자가 더 작을 때 1부터 다시시작한다고 한다. -> 함수로 만들어줬다.
2. while문을 돌리면서 날아가는 숫자가 남은 새보다 많을 때 날아가는 숫자를 1로 바꾸는 방법
"""
# 함수
a = int(input())
s = 0
def count_from_one(num):
    global s
    temp = num
    for i in range(1, num+1):
        if i > temp:
            return count_from_one(temp)
        temp -= i
        s += 1
    return s
print(count_from_one(a))

# while문
n = int(input())
fly, s = 1, 0
while n > 0:
    if n >= fly: 
        n -= fly
        fly += 1; s += 1
    else: fly = 1
print(s)
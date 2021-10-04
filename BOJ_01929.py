""" 210617 09:39 항해 18번 QED 소수구하기"""
# 에라토스테네스의 체
# input 값 m n -> m 이상 n 이하의 소수를 출력

m, n = map(int, input().split())
limit = 1000002
sieve = [1] * limit
sieve[0] = 0
sieve[1] = 0

for i in range(2, int(limit ** 0.5)+1):
    if sieve[i]:
        for j in range(i+i, limit, i):
            sieve[j] = 0
    
answerlist = []
for i in range(m, n+1):
    if sieve[i]:
        answerlist.append(i)

[print(i) for i in answerlist]









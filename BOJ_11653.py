# 소인수분해 211001
""" 
에라토스테네스의 체를 10 000 000 까지 계산한 뒤 True인 애들로 나눠서 소인수 분해 시키기
"""
# 에라토스테네스의 체를 만들어서 해결했는데 시간이 어마어마하게 걸리고 비효율적인 코드라고 생각이듬
'''
n = int(input())

limit = 10000002
sieve = [0,0] + [1] * (limit -1)
prime_list = []

for i in range(2, int(limit**0.5)+1):
    if sieve[i]:
        prime_list.append(i)
        for j in range(i+i, limit, i):
            sieve[j] = 0
# 만약 에라토스테네스의 체를 dictionary로 만든다면? -> 그냥 리스트로 바꿔서 했더니 조금 더 빠르다

biggest_prime = 0
p = []
for i in range(n, 1, -1):
    if sieve[i] == 1 and n%i == 0:
        biggest_prime = max(i, biggest_prime)
        p.append(i)
# 아래의 prime_list 형식이 시간을 반으로 단축시킨다. 근데 정답지에 에러난 부분이 있는지 오답처리된다.
# 프라임 리스트는 i값만 나타내고 i+i, i로 만든 값들을 포함하질 않는다! 여기서 오답이 나온 이유
# for i in prime_list[::-1]:
#     if i >= n:
#         break
#     if sieve[i] == 1 and n%i == 0:
#         biggest_prime = max(i, biggest_prime)
#         p.append(i)

if biggest_prime == 0:
    exit()
else:
    ans = []
    for i in p: # 2
        while n % i == 0: # 72 * 36 * 18 * 9
            n //= i # 몫
            ans.append(i)
            if n % i != 0:
                break
    print(*ans, sep='\n')
'''

# 다른 정답자 코드 - 그냥 처음부터 2부터 해서 계속 나눠준다. max = int(sqrt(n))+1
n = int(input())
for i in range(2, int(n**0.5 + 1)):
    while n % i == 0:
        n //= i; print(i)
        if n == 1: break
    if n == 1: break
if n != 1: print(n)
        

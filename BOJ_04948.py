""" 210616 11:00 항해 12번 완료 에라토스테네스의 체 1824ms"""
limit = 123456
sieve = [True] * (123456 * 2 + 1)
sieve[0] = 0
sieve[1] = 0

for i in range(2, int(len(sieve) ** 0.5) ):
    if sieve[i] == True: # i가 소수인 경우
        for j in range(i+i, len(sieve), i):  # i이후 i의 배수들을 False 판정
            sieve[j] = False

answerList = []
while True:
    """ n 값 입력 """
    n = int(input())
    if n == 0:
        break
    else:
        numPrime = 0
        for i in range(2*n + 1):
            if sieve[i] == True:
                numPrime += 1
        for j in range(n+1):
            if sieve[j] == True:
                numPrime -= 1
        answerList.append(numPrime)

for i in answerList:
    print(i)
# 약수 구하기 210927

# 처음 계산한 1~n 까지 전부 계산하는 방식에서 n이 10000000인 큰 수의 경우 500ms이 넘게 걸린다.
# 2번 식, n = 987654321 7ms 걸림
# 3번 식, n = 987654321 5ms 걸림

'''
import time
n, k = map(int, input().split())
start_time = int(round(time.time() * 1000))

denoms = [i for i in range(1, n+1) if n % i == 0] 
if len(denoms) < k:
    print(0)
else:
    print(denoms[k-1])

end_time = int(round(time.time() * 1000))
print('n = 10000000 실행 시간 : %d(ms)' % (end_time - start_time))
'''


# 특정 수의 약수를 구할 때 루트값(정수) 까지만 나눠주면 좌, 우측이 대칭을 이룬다.
def this_fun_2(n, k):
    arr = []
    for i in range(1, int(n**0.5)+1):
        a, mod = divmod(n, i) # n 값은 고정이고 i값이 변한다.
        if mod == 0:
            if a != i: arr += [a, i]
            elif a == i: arr += [i]
    arr.sort()
    if len(arr) < k: print(0)
    else: print(arr[k-1])


# 1번, 2번을 합친 짧은 코드 -> 왜 틀렸습니다? sorted->set->list 가 순서를 보장하지 않는다.
def this_fun_3(n, k):
    arr = list(set(sum([[i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0], [])))
    arr.sort()
    if len(arr) < k:
        print(0)
    else:
        print(arr[k-1])

import time
n, k = map(int, input().split())

start_time = int(round(time.time() * 1000))
this_fun_2(n,k)
end_time = int(round(time.time() * 1000))
print('n = 987654321 실행 시간 : %d(ms)' % (end_time - start_time))

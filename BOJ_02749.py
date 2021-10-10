# 피보나치 수 3 211008
""" 
Fn 을 구하는데 1000000으로 나눈 나머지를 출력한다.
* 메모이제이션을 활용해서 풀어보자
최대 n이 너무 큰 숫자긴 하다. 어떤 수를 써도 recursion 에러 또는 메모리 에러를 피할 순 없었다.
* 행렬 곱셈을 활용한 풀이
너무 까다로워서 글을 봐도 바로 이해가 되진 않는다.
"""
# 메모이제이션
# n = int(input())
# # limit = 1000000000000000001
# # fibo = [0, 1, 1] + [False] * (limit - 3)
# fibo_dict = {0:0, 1:1, 2:1}

# def fb(n):
#     if fibo_dict.get(n):
#         return fibo_dict[n]
#     else:
#         fibo_dict[n] = fb(n-1) + fb(n-2)
#         return fibo_dict[n]
# print(fb(n)%1000000)

# 특이한 메모이제이션
n = int(input())
fib = [0, 1]
p = int(1000000/10*15)
for i in range(2, p):
	fib.append((fib[i-2]+fib[i-1]) % 1000000)
print(fib[int(n % p)])

# 행렬 곱셈 -> 시간초과
# import sys
# def fibo(n):
#     SIZE = 2
#     ZERO = [[1, 0], [0, 1]]  # 행렬의 항등원
#     BASE = [[1, 1], [1, 0]]  # 곱셈을 시작해 나갈 기본 행렬

#     # 두 행렬의 곱을 구한다
#     def square_matrix_mul(a, b, size=SIZE):
#         new = [[0 for _ in range(size)] for _ in range(size)]
        
#         for i in range(size):
#             for j in range(size):
#                 for k in range(size):
#                     new[i][j] += a[i][k] * b[k][j]
#         return new

#     # 기본 행렬을 n번 곱한 행렬을 만든다
#     def get_nth(n):
#         matrix = ZERO.copy()
#         k = 0
#         tmp = BASE.copy()

#         while 2 ** k <= n:
#             if n & (1 << k) != 0:
#                 matrix = square_matrix_mul(matrix, tmp)
#             k += 1
#             tmp = square_matrix_mul(tmp, tmp)

#         return matrix

#     return get_nth(n)[1][0]

# n = int(input())
# print(fibo(n)%1000000)

# 다른 행렬 곱셈 -> 76ms
# import sys
# input = sys.stdin.readline
# p = 1000000


# def dot(mat1, mat2):
#     N = len(mat1)
#     M = len(mat2)
#     K = len(mat1[0])
#     ansmat = [[0 for _ in range(K)] for _ in range(N)]
#     for i in range(N):
#         for j in range(K):
#             temp = 0
#             for k in range(M):
#                 temp += mat1[i][k] * mat2[k][j] % p
#             ansmat[i][j] = temp % p
#     return ansmat


# def power(mat, b):
#     # 행렬의 제곱은 무조건 N * N꼴이다.
#     N = len(mat)
#     ret = [[0 for _ in range(N)] for _ in range(N)]
#     # ret = 단위행렬
#     for i in range(N):
#         ret[i][i] = 1

#     while b > 0:
#         if b % 2:
#             ret = dot(mat, ret)
#         mat = dot(mat, mat)
#         b //= 2
#     return ret


# N = int(input())
# mat = [[1, 1], [1, 0]]
# if N == 1:
#     print(1)
# else:
#     fibmat = power(mat, N-1)
#     ans = fibmat[0][0]
#     print(ans)

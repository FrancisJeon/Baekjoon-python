# 수 찾기 211008
""" 
입력
N
N개의 수
M
M개의 수
출력
M개의 숫자가 N에 있으면 1 아니면 0

N과 A[1:N+1]개의 정수가 순차적으로 주어지고 다음 줄에는 M과 M개의 수들이 주어지는데 이 수들이 array A에 들어가는지 여부를 한줄씩 출력한다. 존재하면 1 없으면 B

* 이분탐색이 힌트에 있었으므로 N을 sorting
M은 sorting 하지 않고 0번째부터 끝까지 하나씩 이분탐색에 넣어주기
l, r의 절반(내림)이 mid가 된다. (+1 안한다)
반복문의 탈출조건은 l <= r로 l이 r과 같을 때는 겹친 순간이므로 답을 찾는 순간이기도 하다.

"""
# 1번, 950ms, 이분탐색 정석이지만 시간이 오래걸린다. 이분탐색 탈출 조건을 앞으로 당겨주면 조금 더 빨라질 줄 알았는데 여전히 1000ms
# 함수로 바꿔보자 -> 700 ms 약간 빨라지긴 함. 여기서 array_n을 안받게 함수를 바꿔봐도 큰 차이는 안난다.
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr_n = sorted(map(int, input().split()))
# m = int(input())
# arr_m = list(map(int, input().split()))

# """ 
# def bin_src(arr_n, i): # arr_n 받는 함수
#     l, r = 0, n-1
#     while l <= r:
#         mid = (l+r)//2
#         if arr_n[mid] == i:
#             return True
#         if arr_n[mid] < i:
#             l = mid + 1
#         elif arr_n[mid] > i:
#             r = mid -1 
# """

# def bin_src(i):
#     l, r = 0, n-1
#     while l <= r:
#         mid = (l+r)//2
#         if arr_n[mid] == i:
#             return True
#         if arr_n[mid] < i:
#             l = mid + 1
#         elif arr_n[mid] > i:
#             r = mid - 1
            
# for i in arr_m:
#     print(1 if bin_src(i) else 0)

# 2번. bisect 라이브러리를 사용해보자. X
""" # bisect_right는 검색한 값이 존재하지 않다면 무조건 len(array)가 나온다고 생각했는데 알고보니 삽입될 수 있는 위치가 출력된다.
# 만약 특정 어레이에 찾는 값이 있다면 index+1을 출력해주고 없다면 array의 범위 안에서 삽입될 수 있는 위치 또는 len(array)를 제공한다. 
# bisect_left는 검색한 값이 array에 있다면 그 인덱스를 출력하고 없다면 정렬된 array 내부에 들어갈 수 있는 위치를 출력해주므로 인덱싱을 잘 활용하면 이 문제를 풀 수 있다. """
# import sys
# import bisect
# input = sys.stdin.readline

# n = int(input())
# arr_n = sorted(map(int, input().split()))
# m = int(input())
# arr_m = list(map(int, input().split()))

# for i in arr_m:
#     print(0 if bisect.bisect_left(arr_n, i) == n or arr_n[bisect.bisect_left(arr_n, i)] != i else 1)

# 3번. 200ms, binary search 대신 i in array를 사용한게 이 문제에서의 처리 속도는 월등하다.
# 숫자로 받지 않고 list(input().split())은 시간초과 발생한다. -> arr_n만 set로 변경하니까 정답이 나옴
import sys
input = sys.stdin.readline

n = int(input())
arr_n = set(input().split())
m = int(input())
arr_m = set(input().split())

for i in arr_m: print(1 if i in arr_n else 0)

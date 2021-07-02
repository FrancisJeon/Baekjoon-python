""" 210616 14:31 항해 35번 진행중 """
# 백 트래킹 문제

n, m = map(int, input().split())
print("--- 값 입력 ---")
num_list = [i+1 for i in range(n)]
check_list = [False] * n 
# 이미 사용한 n을 거쳐가지 않도록
# num_list = [1,2,3,4]
# check_list = [f, f, f, f]
arr = []

def dfs(cnt):
    """ 주어진 갯수만큼 채워지면 출력 """
    if (cnt == m):
        print(*arr) 
        # 임의의 갯수 arr을 받는다. packing이라고 한다.
        # 빈 값을 print * 써주면 출력하는게 없음
        return

    for i in range(0, n): # 숫자 최대치까지
        # cnt == 0

        if(check_list[i]):
            continue

        check_list[i]=True
        # i번째는 거쳐가므로 True
        arr.append(num_list[i])

        dfs(cnt+1)

        arr.pop()
        # 여기서 print(arr)을 해보면 작동원리를 알 수 있다.
        print(arr)
        print(check_list)
        check_list[i] = False

dfs(0)

""" """ 210616 14: 31 진행중 """
# 백 트래킹 문제

n, m = map(int, input().split())
print("--- 값 입력 ---")
num_list = [i+1 for i in range(n)]
check_list = [False] * n 
# 이미 사용한 n을 거쳐가지 않도록
# num_list = [1,2,3,4]
# check_list = [f, f, f, f]
arr = []

def dfs(cnt):
    """ 주어진 갯수만큼 채워지면 출력 """
    if (cnt == m):
        print(*arr) 
        # 임의의 갯수 arr을 받는다. packing이라고 한다.
        # 빈 값을 print * 써주면 출력하는게 없음
        return

    for i in range(0, n): # 숫자 최대치까지
        # cnt == 0

        if(check_list[i]):
            continue

        check_list[i]=True
        # i번째는 거쳐가므로 True
        arr.append(num_list[i])

        dfs(cnt+1)

        arr.pop()
        # 여기서 print(arr)을 해보면 작동원리를 알 수 있다.
        print(arr)
        print(check_list)
        check_list[i] = False

dfs(0)
 """

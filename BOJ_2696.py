# 중앙값 210928
""" 
어떤 수열을 읽고 홀수번 줄을 읽을 때 마다 지금까지 입력받은 값의 중앙값을 출력

입력
T - 테스트케이스 수
첫째줄 - 수열의 크기 (홀수)
그 뒤로 수열의 원소가 차례대로 주어짐 (한줄에 10개까지 입력 할 수 있다. 10개가 넘으면 여러줄로 출력)
예)
9 (크기)
1 2 3 4 5 6 7 8 9 (원소)
23 (크기)
1 2 3 4 5 6 7 8 9 10 (원소 들...)
1 2 3 4 5 6 7 8 9 10
1 2 3

배열의 크기 / 10 -> 1의자리 올림
원소를 반복하면서 홀수번째 자리에서 여태까지 나온 수의 중앙값을 출력한다. -> sorting해서 중앙의 값 출력시켜야 함. 또는 입력 할 때 Tree 구조를 해서 // 방법을 사용

# extend() 메소드 

"""
# 1차 -> 알고리즘만 대충 맞춘 코드 2592ms
'''
import math
import sys
input = sys.stdin.readline

for i in range(int(input())): # Test case 갯수
    # 배열 -> ceiling 같은걸 이용해서 이번 입력값 갯수 정하기
    array, median = [], []
    
    for j in range(math.ceil(int(input())/10)):
        array += list(map(int, input().split()))
    # 만들어진 리스트를 가지고 정답 출력 작업을 해주자
    for i in range(len(array)): # 길이에서 작업
        if i % 2 == 0: # 중앙값 위치 찾기, 인덱스는 0 베이스라서 홀수 출력하려면 요렇게
            temp = sorted(array[:i+1])
            median.append(temp[(1 + i)//2]) # 시작점 + 현재 위치 / 2 ?? 1-> (1+1)/2, 3-> (1+3)/2            
            
    # 10개 잘라서 출력
    count = len(median)
    print(count)
    s, e = 0, 10
    d, m = divmod(count, 10)
    for _ in range(d):
        print(*median[s:e]) # 0~9번 출력 후 10~19번..
        s = e; e = e + 10
    print(*median[-m:]) # 마지막에 나머지 갯수 출력
'''
# 2차 96ms -> 최대한 파이써닉, 시간고려해서 만든 좌 우 스택을 최소, 최대 힙으로 활용
import math
import sys
import heapq
input = sys.stdin.readline

for test in range(int(input())): # T
    # array = []    
    # for nums in range(math.ceil(int(input())/10)): # M
    #     array += list(map(int, input().split()))
    array = sum([ list(map(int, input().split())) for _ in range(math.ceil(int(input())/10))], []) 
    # 2차원 배열 -> 1차원 배열, 60~62번줄 코드를 한줄로
    
    left, right, middle = [], [], array[0]  # 최대, 최소힙, 중앙값 (데이터를 입력받은 순으로 다루기 때문에 0번은 1번째의 median)
    result = [middle] # median 출력할 값
    
    for idx, val in enumerate(array[1:], 1):
        # if val > middle:
        #     heapq.heappush(right, val)
        # else:
        #     heapq.heappush(left, -val)
        heapq.heappush(right, val) if val > middle else heapq.heappush(left, -val) # 70~73 줄 한줄로
        if idx % 2 == 0: # 홀수번 입력을 받았다면 힙을 균형을 맞춘 뒤 median을 결과에 삽입
            if len(left) < len(right):
                heapq.heappush(left, -middle)
                middle = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, middle)
                middle = -heapq.heappop(left)
            result.append(middle) # median 삽입
    # 균형을 끝까지 맞추었다면
    count = len(result)
    print(count)
    for i in range(count): # 결과물을 출력할 시간, 10개 단위로 자름
        if (i+1) != 1 and (i+1) % 10 == 1: # 0번째는 무시하자가 앞에 담긴 조건이고 뒤에 담긴 조건은 11번째 만나면 줄바꿈을 하자
            print()
        print(result[i], end=' ')

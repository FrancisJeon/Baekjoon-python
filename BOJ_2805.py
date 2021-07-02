""" 210617 14:36 항해 21번 QED """
""" 
상근이는 절단기에 높이 H를 지정해야 한다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 
따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다.  
(총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.
이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
입력
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1, 000, 000, 1 ≤ M ≤ 2, 000, 000, 000)
둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1, 000, 000, 000보다 작거나 같은 양의 정수 또는 0이다.
출력
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
예제 입력 1
4 7
20 15 10 17
예제 출력 1
15
"""

import sys
n, m = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))
trees.sort(reverse=True)
# m 만큼 가져갈 위치 출력하자
if m == 0:
    h = trees[0]
    print(h)
elif n == 1:
    h = trees[0] - m
    print(h)
else:
    lengths = [1] # 인덱스에 1부터 넣게 만들기
    for i in range(len(trees)):
        if i == len(trees)-1:
            leng = trees[i] * (i+1)
            lengths.append(leng)
            break
        leng = (trees[i]-trees[i+1]) * (i+1)
        lengths.append(leng)
    """ 나무 사이의 간격을 인덱스 1부터 시작해서 넣어주었다. """

    length = 0
    idx = 1
    while True:
        length += lengths[idx]
        if length >= m:
            break
        idx += 1
    """ 몇번째 인덱스의 나무까지 사용하는지 확인 """
    """ 이 idx는 lengths에서 목표지점이 포함된 위치이자 나눠야 할 위치 """
    meter = int((length - m) / idx)
    # if (length - m) % idx != 0:
    #     meter = int((length - m) / idx)
    # else: 
    #     meter = int((length - m) / idx)
    print(trees[idx]+meter)


    # # m 만큼의 나무를 가져가야함
    # jIdx = 1
    # for j in range(1, idx): 
    #     m -= lengths[j] * j
    #     jIdx = j+1
    # # j번째 인덱스 다음인덱스번째에 가져갈거니까
    
    # if m%jIdx != 0:
    #     distance = int(m/jIdx) + 1
    # else:
    #     distance = int(m/jIdx)

    # # 3번 인덱스에서 더 들어갈 길이
    # # 1~2번 나무까지의 거리를 계산하자

    # h = trees[0] - trees[jIdx-1] + distance
    # h = trees[0] - h
    # print(h)

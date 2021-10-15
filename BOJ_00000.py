# 테스트용 코드
""" 
* array[n:n] 일 때 합이 0이되는지 확인해보기 -> O은 아니고 빈 값이 출력된다. (투포인터 등)
* array 내부의 원소를 뒤집는게 가능한지 확인해보기 -> 인덱스를 두개 주면 swap을 통해 주소값을 바꾸는게 가능하다.
"""
from collections import defaultdict
word = 'dragon'
d = defaultdict(int)
for i in word:
	d[i] += 1
print(d)

""" 
* heappush()를 한 array가 unpacking할 때 순서대로 heappop을 하는지 아니면 list에 담긴 순서대로 나오는지 확인하기
* heappop이 아닌 트리 형태를 그대로 출력시킨다. -> while문과 heappop 을 활용해야 할듯
"""
import heapq
arr = []
heapq.heappush(arr, 5)
heapq.heappush(arr, 1)
heapq.heappush(arr, 7)
heapq.heappush(arr, 0)
print(arr)
print(*arr)
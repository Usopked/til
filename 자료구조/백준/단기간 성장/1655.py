import sys
import heapq

n = int(sys.stdin.readline())
max_heap = []  # 중앙값보다 작거나 같은 수를 저장
min_heap = []  # 중앙값보다 큰 수를 저장

for _ in range(n):
    num = int(sys.stdin.readline())

    # max_heap의 길이는 항상 min_heap의 길이와 같거나 1 더 많아야 함
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))
    
    # max_heap의 최대값이 min_heap의 최소값보다 큰 경우, 두 값을 swap
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-min_value, min_value))
        heapq.heappush(min_heap, (max_value, max_value))

    print(max_heap[0][1])
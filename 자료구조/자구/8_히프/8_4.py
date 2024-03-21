#최대 힙 구조에 데이터 넣기
def heappush(heap, data):
    heap.append(data)
    current = len(heap) - 1
    while current > 0:
        parent = (current - 1) // 2
        if heap[parent] < heap[current]:
            heap[parent], heap[current] = heap[current], heap[parent]
            current = parent
        else:
            break

#최대 힙 구조에서 데이터 빼기
def heappop(heap):
    if not heap:
        return "Empty Heap!"
    elif len(heap) == 1:
        return heap.pop()

    pop_data, heap[0] = heap[0], heap.pop()
    current, child = 0, 1
    while child < len(heap):
        sibling = child + 1
        if sibling < len(heap) and heap[child] < heap[sibling]:
            child = sibling
        if heap[current] < heap[child]:
            heap[current], heap[child] = heap[child], heap[current]
            current = child
            child = current * 2 + 1
        else:
            break
    return pop_data

def minValue(s, k):
    counter = {}
    for ch in s:
        if ch not in counter:
            counter[ch] = 1
        else:
            counter[ch] += 1

    heap = []
    for value in counter.values():
        heappush(heap, value)

    for _ in range(k):
        temp = heappop(heap) - 1
        heappush(heap, temp)

    return sum([value ** 2 for value in heap])

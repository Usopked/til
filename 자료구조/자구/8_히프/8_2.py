'''def heapify(arr):
    current = start = len(arr)-1
    while start > 0:
        is_swaped = False
        while current > 0:
            parent = (current - 1) // 2
            if arr[parent] > arr[current]:
                arr[parent], arr[current] = arr[current], arr[parent]
                current = parent
                is_swaped = True
            else:
                break
        if is_swaped:
            current = start
        else:
            current = start = current - 1
'''

def heapify(arr):
    last = len(arr) // 2 - 1
    for current in range(last, -1, -1):
        while current <= last:
            child = current * 2 + 1
            sibling = child + 1
            if sibling < len(arr) and arr[child] > arr[sibling]:
                child = sibling
            if arr[current] > arr[child]:
                arr[current], arr[child] = arr[child], arr[current]
                current = child
            else:
                break

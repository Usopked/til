import heapq

def solution(scoville, K):
    answer = 0
    s = scoville[:]
    heapq.heapify(s)
    while s and s[0] < K:
        try:
            new_food = heapq.heappop(s) + heapq.heappop(s) * 2
            heapq.heappush(s, new_food)
            answer += 1
        except:
            return -1
    return answer

'''import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville and scoville[0] < K:
        if len(scoville) < 2:
            return -1
        new_food = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_food)
        answer += 1
    return answer
'''
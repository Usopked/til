from que import Queue
'''def josephus(n, k):
    res = []
    line = [1 for _ in range(n)] #값이 1이면 제거 대상, 0이면 제거 완료
    i = -1
    for _ in range(n-1):
        count = 0
        while count < k:
            i = (i + 1) % n #계속 순환하므로 나머지 연산으로 인덱스 계산
            if line[i]:     #제거된 것이 아닐 때만 count 증가
                count += 1
        line[i] = 0
        res.append(i+1)

    res.append(line.index(1)+1)
    return res'''

def josephus_q(n, k):
    res = []
    q = Queue() #직접 구현한 큐 클래스를 이용
    for i in range(n):
        q.enqueue(i+1)
    while q.front.next: #끝에서 두 번째 원소까지만 반복
        for _ in range(k-1):
            q.enqueue(q.dequeue())
        res.append(q.dequeue())
    res.append(q.dequeue()) #마지막 원소 출력
    return res

print(josephus_q(10, 7))
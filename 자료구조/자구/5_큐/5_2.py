from que import Queue

def generate_binary2(n):
    q = Queue() #직접 구현한 큐 클래스를 이용
    q.enqueue("1")
    for _ in range(n):
        i = q.dequeue()
        q.enqueue(i + "0")
        q.enqueue(i + "1")
        print(i)

generate_binary2(10)
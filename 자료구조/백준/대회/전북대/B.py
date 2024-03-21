N, M = map(int, input().split())
waiting_list = list(map(int, input().split()))
friends = set(map(int, input().split()))
friend_count = sum([1 for i in range(M) if waiting_list[i] in friends])
swap_count = M - friend_count

print(swap_count)

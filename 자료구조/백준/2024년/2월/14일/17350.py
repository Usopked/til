num = int(input())
arr = [[] for _ in range(num)]
for i in range(len(arr)):
    arr[i] = input()
if "anj" in arr:
    print("뭐야;")
else: print("뭐야?")

#배열 없이 풀이
# a = 0
# for i in range(int(input())):
#     if input() == "anj": 
#         print("뭐야;"); a = 1; break
# if a == 0: print("뭐야?")
import sys

n = int(input())
words = [sys.stdin.readline().strip() for _ in range(n)]

alpha = [0]*26
for word in words:
    for i in range(len(word)):
        alpha[ord(word[i])-ord('A')] += 10 ** (len(word) - i - 1)

alpha.sort(reverse=True)

answer = 0
for i in range(10):
    if alpha[i] == 0:
        break
    answer += alpha[i] * (9 - i)
print(answer)

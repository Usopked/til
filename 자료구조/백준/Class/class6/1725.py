import sys
input = sys.stdin.readline
def solve(hist):
    st = []
    max_a = 0
    hist.append(0)

    for i, h in enumerate(hist):
        while st and hist[st[-1]] > h:
            H = hist[st.pop()]
            W = i if not st else i - st[-1] - 1
            max_a = max(max_a, H * W)
        st.append(i)
    
    return max_a

cnt = int(input())
hist = [int(input()) for _ in range(cnt)]
print(solve(hist))

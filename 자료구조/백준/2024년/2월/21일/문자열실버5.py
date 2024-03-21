# 백준 25584번

cnt = int(input())
dic = {}

def time(name, time):
    if name in dic:
        if time == 0 or time == 2:
            dic[name] += 4
        elif time == 1:
            dic[name] += 6
        else:
            dic[name] += 10
    else:
        if time == 0 or time == 2:
            dic[name] = 4
        elif time == 1:
            dic[name] = 6
        else:
            dic[name] = 10
l;
for _ in range(cnt):
    for i in range(4):
        user = input().split()
        for j in user:
            time(j, i)

dic.pop('-', None)
if not dic:
    print("No")
elif max(dic.values()) - min(dic.values()) < 12:
    print("Yes")
else:
    print("No")

            
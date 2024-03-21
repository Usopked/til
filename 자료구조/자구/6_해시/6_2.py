def maxLen_dic2(arr):
    dic = {0: -1}
    ans = 0
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        if total in dic:
            ans = max(ans, i - dic[total])
        else:
            dic[total] = i
    # print(dic)
    return ans

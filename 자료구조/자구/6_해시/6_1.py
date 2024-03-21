from collections import Counter

def first_unique_char_dic2(s):
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1

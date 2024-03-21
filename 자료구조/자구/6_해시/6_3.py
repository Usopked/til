def solution(n, words):
    check = set()
    tail = words[0][0]
    for i, word in enumerate(words):
        if word in check or tail != word[0]:
            return [i % n + 1, i // n + 1]
        check.add(word)
        tail = word[-1]
    return [0, 0]

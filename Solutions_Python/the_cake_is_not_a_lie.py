def solution(s):
    best = 1
    # lets try from len(subarray) n to 1
    for i in range(len(s)):
        length = len(s) / (i + 1)
        succ = True
        for j in range(len(s)):
            if s[j] != s[j % length]:
                succ = False
                break

        if succ:
            best = i + 1

    return best
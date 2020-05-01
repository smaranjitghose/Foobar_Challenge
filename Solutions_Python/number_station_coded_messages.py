def solution(l, t):
    length = len(l)
    for start_index in range(length):
        for end_index in range(start_index, length):
            goal = sum(l[start_index:end_index+1])
            if (goal > t):
                break
            if (goal == t):
                return [start_index, end_index]
    return [-1, -1]

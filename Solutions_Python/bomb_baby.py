def solution(x, y):
    generations = 0
    min_max = [int(x), int(y)]
    while min_max[0] > 1 and min_max[1] > 1:
        min_max.sort()
        if min_max[1] %  min_max[0] == 0:
            return "impossible"
        generations += min_max[1] // min_max[0]
        min_max[1]  = min_max[1] %  min_max[0]
    generations += max(min_max) - 1
    return str(generations)
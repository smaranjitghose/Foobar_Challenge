def solution(x, y):
    return list(set(x).symmetric_difference(set(y)))[0]

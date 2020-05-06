def solution(l):
    parsed = [e.split(".") for e in l]
    toSort = [map(int, e) for e in parsed]
    sortedINTs = sorted(toSort)
    sortedJoined = [('.'.join(str(ee) for ee in e)) for e in sortedINTs]
    return sortedJoined
from itertools import combinations
def solution(l):
	l.sort(reverse=True)
	for i in reversed(range(1, len(l) + 1)):
	    for tup in list(combinations(l, i)):
	        if sum(tup) % 3 == 0:
	            return int(''.join(map(str, tup)))
	return 0

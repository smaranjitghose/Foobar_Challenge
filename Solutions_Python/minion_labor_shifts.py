def solution(data, n):
	counter = {}
	for i in range(len(data)):
		counter[data[i]] = counter.get(data[i], 0) + 1
	remove = []
	for k, v in counter.items():
		if(v > n):
			for i in range(v):
				data.remove(k)
	return data



    
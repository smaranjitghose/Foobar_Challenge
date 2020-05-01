def answer(s):
	return ''.join([chr(ord('z') - ord(c) + ord('a')) if ord('a') <= ord(c) <= ord('z') else c for c in x])

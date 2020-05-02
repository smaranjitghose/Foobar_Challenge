def solution(l):
    div = [[]] * len(l)
    for i in range(1, len(l)):
        div[i] = [j for j in range(i) if l[i] % l[j] == 0]
    count = 0
    for i in range(2, len(l)):
        count += sum(len(div[j]) for j in div[i])
    return count

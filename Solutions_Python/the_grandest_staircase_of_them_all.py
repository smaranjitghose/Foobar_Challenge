def solution(n):
    st = [[0] * n for _ in range(n + 1)]
    st[0][0] = st[1][1] = st[2][2] = 1

    for j in range(1, n):
        for i in range(n + 1):
            st[i][j] = st[i][j - 1]
            if i >= j:
                st[i][j] += st[i - j][j - 1]

    return st[-1][-1]

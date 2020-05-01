def solution(start, length):

    def bulk_xor(m, n):
        m -= 1
        f_m = [m, 1, m + 1, 0][m % 4]
        f_n = [n, 1, n + 1, 0][n % 4]
        return f_m ^ f_n

    xor = 0
    for i in range(length):
        xor ^= bulk_xor(start, start + length - i - 1)
        start += length

    return xor

def solution(n):
    n = int(n)
    operations = 0
  
    while n > 1:
        if n % 2 == 0:
            n = n >> 1
        else:
            n = (n - 1) if (n == 3 or n % 4 == 1) else (n + 1)

        operations += 1
    return operations
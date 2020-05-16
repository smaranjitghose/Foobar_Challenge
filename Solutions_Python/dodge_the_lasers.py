#Beatty seq formula derivation at 
#https://math.stackexchange.com/a/2053713/666385
sqrt2 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

n1 = lambda n: (sqrt2*n)//(10**100)

def s(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    return n*n1(n) + ((n*(n+1))>>1) - ((n1(n)*(n1(n)+1))>>1) - s(n1(n))

def solution(n):
    return str(s(long(n)))

def calculateSum(n) : 
    if (n <= 0) : 
        return 0
    if (n == 1) : 
        return 1
    # fibo=[]
    fibo =[0] * (n)
    fibo[0] = 1
    fibo[1] = 1
   
    # Initialize result 
    sm = fibo[0] + fibo[1] 
   
    # Add remaining terms 
    for i in range(2,n) : 
        fibo[i] = fibo[i-1] + fibo[i-2] 
        sm = sm + fibo[i] 
          
    return sm

def solution(l):
    if l ==0 :
        return 0
    # if l == 
    ma=0
    for i in range(0,32):
        if pow(2,(i+1)) -1 <= l:
            ma=i
        else:
            break
    ma = ma+1
    mi =0
    for i in range(0,100):
        if calculateSum(i) <= l:
            mi = i
        else:
            break
    return mi - ma

def climbStairs(n):
    res = [0] * (n+1)
    res[0] = 1
    res[1] = 1
    if n==1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(2,n+1):
            res[i] = res[i-2] + res[i-1] 
            
    return res[n]
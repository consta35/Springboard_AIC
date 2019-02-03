def fib(N):
    ans = [0,1]
    """
    :type N: int
    :rtype: int
    """
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        for i in range (1,N):
            ans.append(ans[i-1] +ans[i]) 
    return ans[-1]

print(fib(9))
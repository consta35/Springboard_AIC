def Fibonacci(x):
    ans = [0,1]
    for i in range (1,x):
        ans.append(ans[i-1] +ans[i]) 
    return ans
print(Fibonacci(13))
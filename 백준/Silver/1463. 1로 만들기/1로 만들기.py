
a = int(input())
dp = [0] * 1000001
dp[1] = 0
def dyna(num):
    for i in range(2,num+1):
        dp[i] = dp[i-1] + 1
        if i%3 ==0:
            dp[i] = min(dp[i], dp[i//3]+1)
        if i%2 ==0:
            dp[i] = min(dp[i], dp[i//2]+1)
    return dp[num]
print(dyna(a))
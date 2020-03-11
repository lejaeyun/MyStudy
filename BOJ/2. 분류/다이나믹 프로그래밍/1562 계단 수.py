import sys
input = sys.stdin.readline

n = int(input())
dp = [[0,1,1,1,1,1,1,1,1,1] for _ in range(n)]

for i in range(1, n) :
    for j in range(10) :
        if j != 0 :
            dp[i][j] = dp[i-1][j-1]
        try :
            dp[i][j] += dp[i-1][j+1]
        except :
            pass
        dp[i][j] %= 1000000000

print(sum(dp[n-1])%1000000000)


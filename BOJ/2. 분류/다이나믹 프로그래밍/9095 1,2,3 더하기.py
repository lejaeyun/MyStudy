import sys
input = sys.stdin.readline

dp = [0, 1, 2, 4]
for i in range(4, 11) :
    dp.append(dp[i-3] + dp[i-2] + dp[i-1])
for _ in range(int(input())) :
    print(dp[int(input())])

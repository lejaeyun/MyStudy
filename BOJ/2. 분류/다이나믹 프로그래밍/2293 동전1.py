import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list()
dp = [0 for i in range(k+1)]
dp[0] = 1
for _ in range(n) :
    arr.append(int(input()))

for i in arr :
    for j in range(i,k+1) :
        dp[j] += dp[j-i]

print(dp[k])

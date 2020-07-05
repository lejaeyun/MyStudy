import sys
input = sys.stdin.readline

n = int(input()) + 1
arr = list(map(int, input().split()))
arr.insert(0,0)

dp = [0 for j in range(n)]

for i in range(1, n) :
    for j in range(i, n) :
        dp[j] = max(dp[j], dp[j-i] + arr[i])

print(dp[-1])

    

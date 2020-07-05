import sys
input = sys.stdin.readline

arr = list()
for _ in range(int(input())) :
    arr.append(int(input()))

dp = [0 for i in range(len(arr))]
dp[0] = arr[0]
if len(arr) > 1 :
    dp[1] = dp[0] + arr[1]
    for i in range(2, len(dp)) :
        dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2])
    
print(dp[-1])

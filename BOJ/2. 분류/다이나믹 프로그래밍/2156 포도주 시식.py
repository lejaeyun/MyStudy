import sys
input = sys.stdin.readline

arr = list()
for _ in range(int(input())) :
    arr.append(int(input()))

dp = [0 for i in range(len(arr)+2)]
dp[2] = arr[0]
for i in range(3, len(dp)) :
    j = i - 2
    dp[i] = max(arr[j] + arr[j-1] + dp[i-3], arr[j] + dp[i-2], dp[i-1])
    
print(dp[-1])

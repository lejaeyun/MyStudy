import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_lst = list()
for _ in range(n) :
    coin_lst.append(int(input()))

coin_lst.sort(reverse = True)

INF = sys.maxsize
dp = [INF for _ in range(k+1)]
dp[0] = 0

for i in coin_lst :
    for j in range(i,k+1) :
        dp[j] = min( dp[j], dp[j-i] + 1 )

print(dp[-1] if dp[-1] != INF else '-1')

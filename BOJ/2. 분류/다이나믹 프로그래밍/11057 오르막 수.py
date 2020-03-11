#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    n = int(input())
    dp = [[1 for _ in range(10)]]*n
    for i in range(0,n-1) :
        for j in range(10) :
            for k in range(j+1,10) :
                dp[i][j] += dp[i][k]%10007
    print(sum(dp[n-1])%10007)
        
main()

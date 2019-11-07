#https://www.acmicpc.net/problem/11726
import sys
input = sys.stdin.readline

def main() :
    n = int(input())
    dp = [1,1]

    for num in range(2,1001) :
        dp.append( dp[num-2] + dp[num-1])

    print(dp[n]%10007)
    
    return 0;
        
main()


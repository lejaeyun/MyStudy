#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
import copy

def main() :
    n = int(input())
    arr = list(map(int,input().split()))
    dp = copy.deepcopy(arr)
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[j]+arr[i],dp[i])
    print(max(dp))
        
main()

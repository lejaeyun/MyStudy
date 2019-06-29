#https://www.acmicpc.net/problem/2193
import sys
input = sys.stdin.readline

def main() :
    dp0 = 0
    dp1 = 1
    result = []
    for _ in range(int(input())-1) :
        temp = dp1
        dp1 = dp0
        dp0 = dp0 + temp
        
    print(dp0 + dp1)
        
main()

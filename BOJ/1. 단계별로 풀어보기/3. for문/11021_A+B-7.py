#https://www.acmicpc.net/problem/11021
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    for i in range(N) :
        A,B = map(int, input().split())
        print("Case #"+str(i+1) +": " + str(A+B))
    
main()

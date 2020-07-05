#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    R1,S = map(int, input().split())
    R2 = 2*S-R1
    print(R2)
        
main()

#https://www.acmicpc.net/problem/2884
import sys
input = sys.stdin.readline

def main() :
    H,M = map(int, input().split())
    if M >= 45 :
        print(H, M - 45)
    else :
        if H == 0 :
            H = 24
        H = H - 1
        M = M + 60 - 45
        print(H,M)
    
main()

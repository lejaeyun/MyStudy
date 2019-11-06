#https://www.acmicpc.net/problem/10250
import sys
input = sys.stdin.readline

def main() :
    for _ in range(int(input())) :
        H,W,N = map(int, input().split())
        print(int( str(N - H * (N//H)) + "0" + str(N//H + 1) ))
        
    return 0;
        
main()

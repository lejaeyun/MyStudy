#https://www.acmicpc.net/problem/2751
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    srt = []
    for _ in range(N) :
        srt.append(int(input()))
    srt.sort()
    for i in srt :
        print(i)
        
    return 0;
        
main()

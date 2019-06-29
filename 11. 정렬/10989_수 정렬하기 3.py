#https://www.acmicpc.net/problem/10989
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    srt = [0]*10001
    for _ in range(N) :
        srt[int(input())] += 1
    for i in range(10001) :
        if srt[i] != 0 :
            for _ in range(srt[i]) :
                print(i)
        
    return 0;
        
main()

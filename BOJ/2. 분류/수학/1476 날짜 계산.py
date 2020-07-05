#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    E,S,M = map(int, input().split())
    i = 0
    j = True
    while j :
        if (i % 15) == E-1 :
            if (i % 28) == S-1 :
                if (i % 19) == M-1 :
                    j = False
        i += 1
    print(i)
    return 0;
        
main()

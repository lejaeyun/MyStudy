#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    listen = dict()
    see = dict()
    result = list()
    N,M = map(int, input().split())
    for _ in range(N) :
        s = input().rstrip()
        listen[s] = True
        
    for _ in range(M) :
        s = input().rstrip()
        if s in listen.keys() :
            result.append(s)
        see[s] = True
    result.sort()

    print(len(result))
    for i in result :
        print(i)
        
    return 0;
        
main()

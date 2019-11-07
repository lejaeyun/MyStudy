#https://www.acmicpc.net/problem/2953
import sys
input = sys.stdin.readline
import itertools

def main() :
    while True :
        s = list(map(int, input().split()))
        if s[0] == 0 :
            break
        k = s.pop(0)
        s = itertools.combinations(s, 6)
        for i in s :
            print(*i)
        print()
        
        
main()

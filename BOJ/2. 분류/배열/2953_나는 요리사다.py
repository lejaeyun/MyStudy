#https://www.acmicpc.net/problem/2953
import sys
input = sys.stdin.readline

def main() :
    point = -1
    for i in range(5) :
        bp = point
        point = max(point,sum(list(map(int,input().split()))))
        if bp != point :
            result = i+1
        
    print(result,point)
        
main()

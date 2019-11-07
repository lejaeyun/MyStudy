#https://www.acmicpc.net/problem/2588
import sys
input = sys.stdin.readline

def main() :
    A = int(input())
    B = str(input().split()[0])
    result = []
    for i in B :
        result.append(A * int(i))
    result.reverse()
    for i in result :
        print(i)
    print(A*int(B))
    
main()

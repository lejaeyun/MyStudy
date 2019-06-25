#https://www.acmicpc.net/problem/10951
import sys
input = sys.stdin.readline

def main() :
    try:
        while True:
            A, B = map(int, input().split())
            print(A + B)
    except:
        exit()
        
main()

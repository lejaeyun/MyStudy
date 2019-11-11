#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    while True :
        A,B = map(int, input().split())
        if A == B and A == 0 :
            break
        if A >= B :
            if A % B == 0 :
                print("multiple")
            else :
                print("neither")
        else :
            if B % A == 0 :
                print("factor")
            else :
                print("neither")
        
        
main()

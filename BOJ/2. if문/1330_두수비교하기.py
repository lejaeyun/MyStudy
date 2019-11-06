#https://www.acmicpc.net/problem/1330
import sys
input = sys.stdin.readline

def main() :
    A,B = map(int,input().split())
    if A < B :
        print("<")
    elif A > B :
        print(">")
    elif A == B :
        print("==")
        
    
main()

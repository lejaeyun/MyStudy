#https://www.acmicpc.net/problem/2753
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    a,b,c = N%4, N%100, N%400
    if b == 0 and c != 0 :
        print("0")
    else :
        if a == 0 :
            print("1")
        else :
            print("0")
        
    
main()

#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    X = int(input())
    X = list(str(bin(X)).split('b')[1])
    print(X.count('1'))
    
        
main()

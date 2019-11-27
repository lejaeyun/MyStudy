#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    string = input().rstrip()
    moum = ["a","e","i","o","u"]
    result = 0
    for s in string :
        if s in moum :
            result = result + 1
    
    print(result)
        
main()

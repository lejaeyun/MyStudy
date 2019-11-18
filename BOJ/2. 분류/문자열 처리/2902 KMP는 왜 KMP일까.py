#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    result = ""
    string = list(map(str, input().split("-")))
    for s in string :
        result += s[0]
    print(result)
    return 0;
        
main()

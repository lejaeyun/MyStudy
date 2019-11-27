#https://www.acmicpc.net/problem/10988
import sys
input = sys.stdin.readline

def main() :
    string = input().rstrip()
    mid = len(string) // 2
    for i in range(mid) :
        if string[i] != string[-1 - i] :
            print("0")
            return
    print("1")
            
main()

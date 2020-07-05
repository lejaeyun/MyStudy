#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    print(arr[0]* arr[-1])
        
    return 0;
        
main()

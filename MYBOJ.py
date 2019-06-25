#https://www.acmicpc.net/problem/2562
import sys
input = sys.stdin.readline

def main() :
    arr = []
    for _ in range(9) :
        arr.append(int(input()))
    print(max(arr))
    print(arr.index(max(arr)) + 1)
        
main()

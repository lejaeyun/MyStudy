#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    arr = [[1, 0], [0, 1]]
    for i in  range(2, 40) :
        zero = arr[i-1][0] + arr[i-2][0]
        one = arr[i-1][1] + arr[i-2][1]
        arr.append([zero, one])
        
    for _ in range(int(input())) :
        n = int(input())
        print(arr[n][0], arr[n][1])
        
main()

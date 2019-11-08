#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    arr = [1, 1, 1]
    for i in range(3, 100 + 1) :
        arr.append(arr[i - 2] + arr[i - 3])
    
    for _ in range(int(input())) :
        print(arr[int(input()) - 1])
    return 0;
        
main()

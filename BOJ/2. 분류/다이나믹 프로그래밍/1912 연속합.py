#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    n = int(input())
    arr = list(map(int,input().split()))
    result = list()
    result.append(arr[0])
    for i in range(1,len(arr)) :
        result.append(max(result[i-1]+arr[i],arr[i]))
    print(max(result))
        
main()

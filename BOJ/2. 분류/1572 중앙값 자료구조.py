#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
import heapq

def main() :
    arr = list()
    N,k = map(int, input().split())
    check = list()

    index = 0
    result = 0
    for _ in range(N) :
        num = int(input())
        heapq.heappush(arr, num)
        check.append(num)
        if index >= k:
            result += arr[(k)//2]
            arr.pop()
        index = index + 1
            
    print(result)
        
main()

#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
import heapq

def main() :
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort()

    print(arr[K-1])
    
        
main()

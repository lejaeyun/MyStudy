#https://www.acmicpc.net/problem/1927
import sys
input = sys.stdin.readline
import heapq

def main() :
    heap = list()
    for _ in range(int(input())) :
        n = int(input())
        if n == 0 :
            try :
                print(heapq.heappop(heap))
            except :
                print(0)
        else :
            heapq.heappush(heap, n)
        
main()

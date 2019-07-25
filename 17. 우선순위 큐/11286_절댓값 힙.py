#https://www.acmicpc.net/problem/11286
import sys
input = sys.stdin.readline
import heapq

def main() :
    heapm = list()
    heapp = list()
    for _ in range(int(input())) :
        n = int(input())
        if n == 0 :
            if len(heapm) == 0 and len(heapp) == 0 :
                print(0)
            else :
                if len(heapm) == 0 :
                    print(heapq.heappop(heapp))
                elif len(heapp) == 0 :
                    print(-heapq.heappop(heapm))
                else :
                    p = heapq.heappop(heapp)
                    m = heapq.heappop(heapm)
                    if p < m :
                        heapq.heappush(heapm, m)
                        print(p)
                    else :
                        heapq.heappush(heapp, p)
                        print(-m)
        else :
            if n > 0 :
                heapq.heappush(heapp, n)
            else :
                heapq.heappush(heapm, -n)
        
main()

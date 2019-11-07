#https://www.acmicpc.net/problem/2108
import sys
input = sys.stdin.readline
import statistics
from collections import Counter

def main() :
    N = int(input())
    
    l = list()
    for _ in range(N) :
        l.append(int(input()))
    l.sort()

    print(round(sum(l) / N))
    
    print(statistics.median(l))
    
    counts = Counter(l)
    max_count = max(counts.values())
    x = [x_i for x_i, count in counts.items() if count == max_count]
    x.sort()
    if len(x) > 1 :
        print(x[1])
    else :
        print(x[0])
    
    print(max(l) - min(l))
    
    return 0;
        
main()

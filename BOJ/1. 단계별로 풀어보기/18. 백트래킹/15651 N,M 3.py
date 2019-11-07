#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
import itertools

def main() :
    N,M = map(int, input().split())
    arr = [i for i in range(1, N + 1)]
    
    if M == 1 :
        for l in arr :
            print(l)
    else :
        arr = itertools.product(arr, repeat = M)
        
        
        for l in arr :
            ll = str(l)[1:len(str(l))-1].split(",")
            print("".join(ll))
            
            
        
main()

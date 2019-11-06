#https://www.acmicpc.net/problem/2407
import sys
input = sys.stdin.readline
from math import factorial

def main() :
    N,K = map(int,input().split())

    denominator = 1
    molecule = 1
    for _ in range(K) :
        denominator = denominator * N
        N = N - 1
        molecule = molecule * K
        K = K - 1
        

    print((denominator // molecule))


    
    return 0;
        
main()

#https://www.acmicpc.net/problem/11051
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
        

    print((denominator // molecule) % 10007)


    
    return 0;
        
main()

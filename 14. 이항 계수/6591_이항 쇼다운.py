#https://www.acmicpc.net/problem/6591
import sys
input = sys.stdin.readline
from math import factorial

def main() :
    while True :
        N,K = map(int,input().split())
        if K > N-K :
            K = N-K
        if N == K and N == 0 : break
        denominator = 1
        molecule = 1
        for _ in range(K) :
            denominator = denominator * N
            N = N - 1
            molecule = molecule * K
            K = K - 1
            

        print(denominator // molecule)


    
    return 0;
        
main()

#https://www.acmicpc.net/problem/2747
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    fibo = [0] * (N+1)
    fibo[0],fibo[1] = 0, 1
    
    for i in range(2,N+1) :
        fibo[i] = fibo[i-1] + fibo[i-2]
        
    print(fibo[N])
    return 0;
        
main()

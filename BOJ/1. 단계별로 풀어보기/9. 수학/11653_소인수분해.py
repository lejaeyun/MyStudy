#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    while N != 1 :
        for i in range(2, 10000000) :
            if N % i == 0 :
                N /= i
                print(i)
                break
    return 0;
        
main()

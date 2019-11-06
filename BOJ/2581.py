#https://www.acmicpc.net/problem/2581
import sys
input = sys.stdin.readline

def prime_list(n):
    n += 1
    sieve = [0] * n
    sieve[0],sieve[1] = 1,1

    for i in range(2, n):
        if sieve[i] == 0:
            for j in range(i+i, n, i):
                nn = j
                while nn % i == 0 :
                    nn //= i
                    sieve[j] += 1

    return sieve

def main() :
    pl = prime_list(10000)
    sum = 0
    fir = 0
    A = int(input())
    B = int(input())
    for i in range(A,B + 1) :
        if (pl[i] == 0) :
            if fir == 0 :
                fir = i
            sum += i

    if sum == 0 :
        print(-1)
    else :
        print(sum)
        print(fir)
    
    return 0;
        
main()

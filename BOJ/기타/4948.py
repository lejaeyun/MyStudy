#https://www.acmicpc.net/problem/1978
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
    pl = prime_list(2 * 123456)
    while True :
        cnt = 0
        num = int(input())
        if num == 0 : break
        
        for i in range(num + 1, 2 * num + 1) :
            if (pl[i] == 0) :
                cnt += 1
        print(cnt)
            
    return 0;
        
main()

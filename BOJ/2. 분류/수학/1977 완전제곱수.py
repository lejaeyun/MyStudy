#https://www.acmicpc.net/problem/
import sys
import math
input = sys.stdin.readline

def main() :
    M = int(input())
    N = int(input())
    
    if int(str(M**(1/2)).split('.')[1]) == 0 :
        s = int(M**(1/2))
    else :
        s = round(M**(1/2)+0.5)
                
    sum = 0
    for i in range(s, int(N**(1/2)) + 1) :
        sum += i*i

    if sum == 0 :
        print( '-1' )
    else :
        print(sum )
        print(s**2)
    
    return 0;
        
main()

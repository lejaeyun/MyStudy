#https://www.acmicpc.net/problem/2798
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    
    for i in range(1, 1000001) :
        s = i
        j = i
        while j != 0 :
            s += j % 10
            j =  j // 10
        if s == N :
            print(i)
            return
    print(0)
            
        
main()

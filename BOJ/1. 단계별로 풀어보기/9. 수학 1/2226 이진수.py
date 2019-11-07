#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    arr = [0]
    N = int(input())
    for i in range(N - 1) :
        if i%2 == 0 :
            arr.append(arr[i]*2+1)
        else :
            arr.append(arr[i]*2-1)
            
    print(arr[-1])
    
        
main()

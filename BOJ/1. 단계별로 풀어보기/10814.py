#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    arr = list()
    for _ in range(int(input())) :
        i = input().split()
        a, n = int(i[0]), i[1]
        arr.append([a,_,n])
    arr.sort()
    
    for i,j,k in arr :
        print(i,k)
        
main()

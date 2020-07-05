#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    arr = list()
    result = 1
        
    for _ in range(int(input())) :
        arr.append(int(input())-1)
    result += sum(arr)
    print(result)
        
    return 0;
        
main()

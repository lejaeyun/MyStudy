#https://www.acmicpc.net/problem/10773
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    stack = list()
    
    for _ in range(N) :
        num = int(input())
        
        if num == 0 :
            stack.pop(-1)
        else :
            stack.append(num)

    print(sum(stack))
    
    return 0;
        
main()

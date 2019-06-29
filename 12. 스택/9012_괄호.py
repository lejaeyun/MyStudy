#https://www.acmicpc.net/problem/9012
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    
    for _ in range(N) :
        a = str(input())
        a = a.rstrip('\n')
        stack = 0
        for i in a :
            if i == "(" :
                stack += 1
            else :
                if stack != 0 :
                    stack -= 1
                else :
                    stack = -1
                    break
        if stack == 0 :
            print("YES")
        else :
            print("NO")
            
    
    return 0;
        
main()

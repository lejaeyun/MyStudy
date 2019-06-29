#https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    stack = [-1]
    
    for _ in range(N) :
        a = str(input())
        a = a.rstrip('\n')
        if a.find("push") != -1 :
            stack.append(int(a.split()[1]))
        else :
            if a == "top" :
                print(stack[-1])
            elif a == "size" :
                print(len(stack)-1)
            elif a == "pop" :
                if len(stack) == 1 :
                    print("-1")
                else :
                    print(stack.pop(-1))
            elif a == "empty" :
                if len(stack) == 1 :
                    print("1")
                else :
                    print("0")
    
    return 0;
        
main()

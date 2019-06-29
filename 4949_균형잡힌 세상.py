#https://www.acmicpc.net/problem/4949
import sys
input = sys.stdin.readline

def main() :
    while True:
        a = str(input())
        a = a.rstrip('\n')
        if a == "." : break
        
        stack = list()
        for i in a :
            if i == "(" or i == ")" or i == "[" or i == "]" :
                stack.append(i)

                
        if len(stack) == 0 :
            print("yes")
        else :
            print("no")
            
    
    return 0;
        
main()

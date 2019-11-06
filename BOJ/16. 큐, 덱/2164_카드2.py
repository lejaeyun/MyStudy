#https://www.acmicpc.net/problem/2164
import sys
input = sys.stdin.readline
from collections import deque

def main() :
    stack = deque()
    for i in range(1,int(input())+1) :
        stack.append(i)
        
    while stack :
        nxt = stack.popleft()
        if stack :
            stack.append(stack.popleft())

    print(nxt)
    
        
main()

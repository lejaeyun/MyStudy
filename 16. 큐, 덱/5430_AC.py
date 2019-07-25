#https://www.acmicpc.net/problem/5430
import sys
input = sys.stdin.readline
from collections import deque

def main() :
    stack = deque()
    for _ in range(int(input())) :
        string = list(input().split()[0])
        N = int(input())
        if N < string.count("D") :
            input()
            print("error")
        else :
            type = 0
            S = deque(str(input())[1:-1-1].split(","))
            for s in string :
                if s == "R" :
                    if type == 0 :
                        type = 1
                    else :
                        type = 0
                elif s == "D" :
                    if type == 0 :
                        S.popleft()
                    else :
                        S.pop()
            if type == 1 :
                S.reverse()
            
            print("[",end = "")
            for i in range(len(S)) :
                if i + 1 == len(S) :
                    print(S[i],end="")
                else :
                    print(S[i],end=",")
            print("]")
    
        
main()

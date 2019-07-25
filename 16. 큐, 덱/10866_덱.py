#https://www.acmicpc.net/problem/10866
import sys
input = sys.stdin.readline
from collections import deque

def main() :
    queue = deque()
    for _ in range(int(input())) :
        a = list(input().split())
        s = a[0]
        if s == "push_back" :
            queue.append(a[1])
        elif s == "push_front" :
            queue.appendleft(a[1])
        elif s == "front" :
            try :
                t = queue.popleft()
                queue.appendleft(t)
                print(t)
            except :
                print(-1)
        elif s == "back" :
            try :
                t = queue.pop()
                queue.append(t)
                print(t)
            except :
                print(-1)
        elif s == "size" :
            print(len(queue))
        elif s == "pop_front" :
            try :
                print(queue.popleft())
            except :
                print(-1)
        elif s == "pop_back" :
            try :
                print(queue.pop())
            except :
                print(-1)
        elif s == "empty" :
            if queue :
                print(0)
            else :
                print(1)
        
main()

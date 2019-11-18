#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
from collections import deque

def dfs(array, start) :
    stack = deque()
    visit = dict()

    stack.append(array[start])
    while stack :
        nxt = stack.popleft()
        if nxt not in visit.keys() :
            visit[nxt] = True
            stack.extendleft(array[nxt])
        
    return visit.keys()


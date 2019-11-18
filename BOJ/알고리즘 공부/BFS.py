#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
import collections.deque

def bfs(array,start) :
    queue = deque()
    visit = dict()

    queue.extend(array[start])
    while queue :
        nxt = queue.popleft()
        if nxt not in visit.keys() :
            visit[nxt] = True
            queue.extend(array[nxt])

    return visit.keys()

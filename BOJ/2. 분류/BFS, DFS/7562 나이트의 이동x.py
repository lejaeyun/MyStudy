#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
from collections import deque

def main() :
    for _ in range(int(input())) :
        N = int(input())
        nowx, nowy = map(int,input().split())
        desx, desy = map(int,input().split())
        queue = deque()
        visit = dict()
        queue.append((nowx,nowy,0))
        while queue :
            nxt = queue.popleft()
            nowx,nowy,time = nxt[0],nxt[1],nxt[2]
            if (nowx,nowy) == (desx,desy) :
                print(time)
                break
            if (nowx,nowy) not in visit.keys() :
                visit[(nowx,nowy)] = "True"
                queue.extend(inside(nowx,nowy,time,N,visit))
            
def inside(x,y,time,n,visit) :
    canvisit = list()
    canvisit.append((x-2,y+1))
    canvisit.append((x-2,y-1))
    canvisit.append((x-1,y+2))
    canvisit.append((x-1,y-2))
    canvisit.append((x+1,y+2))
    canvisit.append((x+1,y-2))
    canvisit.append((x+2,y+1))
    canvisit.append((x+2,y-1))
    rtnvisit = list()
    for i,j in canvisit :
        if i < 0 :
            continue
        elif j < 0 :
            continue
        elif i >= n :
            continue
        elif j >= n :
            continue
        elif (i,j) in visit.keys() :
            continue
        else :
            rtnvisit.append((i,j,time+1))
    return rtnvisit
main()

#https://www.acmicpc.net/problem/14671
import sys
input = sys.stdin.readline

def main() :
    N,M,K = map(int,input().split())
    visit = list()
    for _ in range(K) :
        x,y = map(int,input().split())
        point_arr = [ [x-1, y-1], [x-1, y+1], [x+1, y-1], [x+1, y+1] ]
        for l,k in point_arr :
            if l != 0 and l <= M :
                if k != 0 and k <= N :
                    if [l,k] not in visit :
                        visit.append([l,k])
    if len(visit) == N*M :
        print("YES")
    else :
        print("NO")
    
        
main()

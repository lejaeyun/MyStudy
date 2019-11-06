#https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

def main() :
    N, K = map(int,input().split())

    queue = [i+1 for i in range(N)]
    result = list()
    pp = list()
    num = N
    nxt = 0
    while queue :
        nxt += K
        if N < nxt :
            nxt = nxt - N
            print(nxt,queue)
            for i in pp :
                queue.pop(i)
                N = N - 1
            pp.clear()
        if queue[nxt - 1] != 0 :
            result.append(queue[nxt - 1])
            queue[nxt-1] = 0
            pp.insert(0,nxt - 1)
        
    print("<", end = "")
    for i in result :
        print(i, end = ", ")
    print(">", end = "")
    
    return 0;
        
main()

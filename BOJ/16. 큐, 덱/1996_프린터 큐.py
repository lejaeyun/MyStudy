#https://www.acmicpc.net/problem/1966
import sys
input = sys.stdin.readline
import copy

def main() :
    
    for _ in range(int(input())) :
        queue = list()
        N,M = map(int, input().split())
        queue.extend(list(map(int, input().split())))
        q = copy.deepcopy(queue)
        
        for i in range(len(q)) :
            q[i] = [q[i],i]
            
        cnt = 0
        
        while q :
            chk = q.pop(0)
            if chk[0] == max(queue) :
                queue.pop(queue.index(chk[0]))
                cnt = cnt + 1
                if chk[1] == M :
                    print(cnt)
            else :
                q.append(chk)
        
    
    return 0;
        
main()

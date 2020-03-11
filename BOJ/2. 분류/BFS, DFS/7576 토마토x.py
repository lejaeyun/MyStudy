#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
import copy

def bfs(li) :
    time = 0
    queue = list()
    visit = dict()
    notvisit = dict()
    M,N = len(li[0]),len(li)
    for i in range(N) :
        for j in range(M) :
            if li[i][j] == 1 :
                queue.append((i,j))
            elif li[i][j] == -1 :
                notvisit[ (i,j) ] = 'True'

    while queue :
        tmpqueue = copy.deepcopy(queue)
        queue = []
        while tmpqueue :
            nxt = tmpqueue.pop(0)
            i,j = nxt[0],nxt[1]
            if nxt not in visit.keys() :
                visit[nxt] = 'True'
            try :
                if (i+1, j) not in visit.keys() and li[i+1][j] == 0 :
                    li[i+1][j] = 1
                    queue.append((i+1,j))
            except :
                pass
            try :
                if (i-1, j) not in visit.keys() and li[i-1][j] == 0 and i-1 >= 0 :
                    li[i-1][j] = 1
                    queue.append((i-1,j))
            except :
                pass
            try :
                if (i, j+1) not in visit.keys() and li[i][j+1] == 0 :
                    li[i][j+1] = 1
                    queue.append((i,j+1))
            except :
                pass
            try :
                if (i, j-1) not in visit.keys() and li[i][j-1] == 0 and j-1 >= 0 :
                    li[i][j-1] = 1
                    queue.append((i,j-1))
            except :
                pass
        time = time + 1
        
    for i in range(N) :
        if 0 in li[i] :
            return -1
        
    return time-1


def main() :
    M,N = list(map(int, input().split()))
    tomato_li = list()
    for _ in range(N) :
        tomato_li.append(list(map(int, input().split())))

    print(bfs(tomato_li))
        
main()

#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def inorout(y, x , M, N) :
    if x >= 0 and x < N :
        if y >= 0 and y < M :
            return 1
    return 0

def bfs(array, col, row) :

    queue = list()
    visit = dict()
    index = 0
    result = 0
    while index < col*row :
        if not queue and index not in visit.keys() :
            if array[index // col][index % col] == 1 :
                result += 1
                queue.append(index)
                
        while queue :
            nxt = queue.pop()
            i,j = nxt // col, nxt % col
            if nxt not in visit.keys() :
                visit[nxt] = True
                
                #상    
                if inorout(i-1,j,row,col) == 1 and array[i-1][j] == 1  :
                    queue.append(nxt - col)
                    
                #하
                if inorout(i+1,j,row,col) == 1 and array[i+1][j] == 1  :
                    queue.append(nxt + col)
                    
                #좌    
                if inorout(i,j-1,row,col) == 1 and array[i][j-1] == 1  :
                    queue.append(nxt - 1)

                #우
                if inorout(i,j+1,row,col) == 1 and array[i][j+1] == 1  :
                    queue.append(nxt + 1)

                #우상
                if inorout(i-1,j+1,row,col) == 1 and array[i-1][j+1] == 1  :
                    queue.append(nxt - col + 1)

                #좌상
                if inorout(i-1,j-1,row,col) == 1 and array[i-1][j-1] == 1  :
                    queue.append(nxt - col - 1)

                #우하
                if inorout(i+1,j+1,row,col) == 1 and array[i+1][j+1] == 1  :
                    queue.append(nxt + col + 1)

                #좌
                if inorout(i+1,j-1,row,col) == 1 and array[i+1][j-1] == 1 :
                    queue.append(nxt + col - 1)

        index += 1
    
    return result

def main() :
    while True :
        col,row = map(int, input().split())
        if col == row and col == 0 :
            break
        
        arr = [0 for _ in range(row)]
        for i in range(row) :
            arr[i] = list(map(int,input().split()))
            
        print(bfs(arr, col, row))
    return 0;
        
main()

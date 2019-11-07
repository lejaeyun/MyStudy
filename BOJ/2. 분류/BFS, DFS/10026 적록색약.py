#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def inorout(x, y , M, N) :
    if x >= 0 and x < N :
        if y >= 0 and y < M :
            return 1
    return 0

def bfs(array, num) :

    queue = list()
    visit = list()
    index = 0
    result = 0
    while index < num*num :
        if not queue and index not in visit :
            queue.append([index, array[index // num][ index % num ]])
            result += 1
        while queue :
            tmp = queue.pop(0)
            nxt,color = tmp[0], tmp[1]
            i,j = nxt // num, nxt % num
            if nxt not in visit :
                visit.append(nxt)
                
                if inorout(i+1,j,num,num) == 1 and color == array[i+1][j] :
                    queue.append([nxt + num, array[i+1][j]])
                    
                    
                if inorout(i-1,j,num,num) == 1 and color == array[i-1][j] :
                    queue.append([nxt - num, array[i-1][j]])
                    
                if inorout(i,j+1,num,num) == 1 and color == array[i][j+1] :
                    queue.append([nxt + 1, array[i][j+1]])
                    
                if inorout(i,j-1,num,num) == 1 and color == array[i][j-1] :
                    queue.append([nxt - 1, array[i][j-1]])
                    
                continue

        index += 1
    
    return result

def main() :
    num = int(input())
    arr = [[] for _ in range(num)]
    color_arr = [[] for _ in range(num)]
    for n in range(num) :
        string = input().split()[0]
        for s in string :
            arr[n].append(s)
            if s == "G" :
                color_arr[n].append("R")
            else :
                color_arr[n].append(s)
    
        
    print(bfs(arr, num), bfs(color_arr,num))
    return 0;
        
main()

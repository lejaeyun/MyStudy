#https://www.acmicpc.net/problem/2667
import sys
input = sys.stdin.readline
import copy
import itertools

def Search(arr, row, col) :
    queue = list()
    num = 0
    while num < row * col :
        if arr[num] == 2 :
            queue.append(num)
            while queue :
                nxt = queue.pop(0)

                if arr[nxt] == 0 :
                    arr[nxt] = 2
                
                # 상
                if nxt - col >= 0 and arr[nxt - col] == 0 :
                    if nxt - col not in queue :
                        queue.append(nxt - col)
                    
                # 하
                if nxt + col < row * col and arr[nxt + col] == 0 :
                    if nxt + col not in queue :
                        queue.append(nxt + col)
                    
                # 좌
                if nxt % col != 0 and arr[nxt - 1] == 0 :
                    if nxt - 1 not in queue :
                        queue.append(nxt - 1)
                    
                # 우
                if (nxt - (col - 1)) % col != 0 and arr[nxt + 1] == 0 :
                    if nxt + 1 not in queue :
                        queue.append(nxt + 1)
        num += 1
        
    return 
        

def main() :
    r,c = map(int, input().split())
    Lab = list()
    comb_arr = list()
    result = list()
    for _ in range(r) :
        Lab.extend(list(map(int, input().split())))
        
    for i in range(r*c) :
        if Lab[i] == 0 :
            comb_arr.append(i)
            
    comb_arr = list(itertools.combinations(comb_arr,3))
    
    for i,j,k in comb_arr :
        Temp_Lab = copy.deepcopy(Lab)
        Temp_Lab[i],Temp_Lab[j],Temp_Lab[k] = 1,1,1
        Search(Temp_Lab,r,c)
        result.append(Temp_Lab.count(0))
        
    '''
    for i in range(r*c) :
        if i % c == 0 :
            print()
        print(Temp_Lab[i], end = " ")
    '''
        
    print(max(result))
        
    return 0;
        
main()

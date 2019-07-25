#https://www.acmicpc.net/problem/2667
import sys
input = sys.stdin.readline

def Search(arr, n) :
    queue = list()
    result = list()
    num = 0
    while num < n * n :
        visit = 0
        if arr[num] == "1" :
            queue.append(num)
            while queue :
                nxt = queue.pop(0)
                if arr[nxt] == "1" :
                    visit += 1
                    arr[nxt] = 0
                # 상
                if nxt - n > 0 and arr[nxt - n] == "1" :
                    if nxt - n not in queue :
                        queue.append(nxt - n)
                    
                # 하
                if nxt + n < n * n and arr[nxt + n] == "1" :
                    if nxt + n not in queue :
                        queue.append(nxt + n)
                    
                # 좌
                if nxt % n != 0 and arr[nxt - 1] == "1" :
                    if nxt - 1 not in queue :
                        queue.append(nxt - 1)
                    
                # 우
                if (nxt - (n - 1)) % n != 0 and arr[nxt + 1] == "1" :
                    if nxt + 1 not in queue :
                        queue.append(nxt + 1)
                    
            result.append(visit)
                
        num += 1
        
    return result
        

def main() :
    num = int(input())
    Home = list()
    for _ in range(num) :
        Home.extend(list(input().split()[0]))

    rst = Search(Home,num)

    print(len(rst))
    rst.sort()
    for i in rst :
        print(i)
        
    return 0;
        
main()

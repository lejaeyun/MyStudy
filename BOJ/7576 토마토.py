#https://www.acmicpc.net/problem/7576
import sys
input = sys.stdin.readline
import copy
​
def find_tomatto(arr, M, N) :
   day = 0
   queue = list()
   visit = list()
   start = 0
   array = copy.deepcopy(arr)
   while start < M*N :
       x,y = start % M, start // M
       if array[y][x] == 1 :
           queue.append(start)
       start += 1
           
   while queue :
       start = queue.pop(0)
       x,y = start % M, start // M
       day += 1
       if array[y][x] == 1 :
           if start not in visit :
               visit.extend( BFS(array,M,N,start) )
           try :
               if array[y][x + 1] == 0 :
                   queue.append(nxt + 1)
           except :
               pass
           try :
               if array[y][x - 1] == 0 and x != 0 :
                   queue.append(nxt - 1)
           except :
               pass
           try :
               if array[y+1][x] == 0 :
                   array[y+1][x] = 1
           except :
               pass
           try :
               if array[y-1][x] == 0 and y != 0 :
                   queue.append(nxt - M)
           except :
               pass
   return day
​
def main() :
​
    M,N = map(int, input().split())
    arr = []
    ​
    for i in range(N) :
        arr.append(list(map(int, input().split())))

    ​
    print(calculate_date(arr, M, N))
    ​
    ​
main()
​​

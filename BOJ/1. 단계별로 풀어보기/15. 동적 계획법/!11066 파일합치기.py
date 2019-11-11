#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
import copy

def main() :
    for _ in range(int(input())) :
        arr = list()
        N = int(input())
        arr.extend(list(map(int, input().split())))
        s = 0
        while True :
            arr.sort()
            new_arr = list()
            if N % 2 == 1 :
                for i in range(0,N-1,2) :
                    new_arr.append(arr[i]+arr[i+1])
                temp = arr[-1]
                arr = copy.deepcopy(new_arr)
                s = s + sum(arr)
                arr.append(temp)
                N = N // 2 + 1
            else :
                for i in range(0,N,2) :
                    new_arr.append(arr[i]+arr[i+1])
                arr = copy.deepcopy(new_arr)
                N = N // 2
                s = s + sum(arr)

            if N == 1 :
                break
        print(s)
    
    return 0;
        
main()

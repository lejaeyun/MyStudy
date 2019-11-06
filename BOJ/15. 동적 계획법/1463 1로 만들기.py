#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
import copy

def main() :
    num = int(input())
    arr = [1]
    index = 0
    while True :
        if num in arr :
            break
        newarr = copy.deepcopy(arr)
        arr = []
        for i in newarr :
            arr.append(i*3)
            arr.append(i*2)
            arr.append(i+1)
        arr = list(set(arr))
        index = index + 1
    print(index)
        
main()

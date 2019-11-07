#https://www.acmicpc.net/problem/1463
import sys
input = sys.stdin.readline

def main() :
    num = int(input())
    arr = [1]
    index = 0
    check = [0] * 1000001
    while True :
        if num in arr :
            break
        newarr = arr
        arr = []
        for i in newarr :
            if i*3 < 10**6 + 1 and check[i*3] == 0 :
                arr.append(i*3)
                check[i*3] = 1
            if i*2 < 10**6 + 1 and  check[i*2] == 0 :
                arr.append(i*2)
            if i+1 < 10**6 + 1 and  check[i+1] == 0 :
                arr.append(i+1)
        index = index + 1
        
    print(index)
        
main()

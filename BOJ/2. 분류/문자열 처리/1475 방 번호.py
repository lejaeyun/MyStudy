#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    arr = [ 0 for _ in range(10) ]
    result = 0
    string = input().split()[0]
    for s in string :
        tmp = int(s)
        if arr[tmp] == 0 :
            for i in range(10) :
                arr[i] += 1
                if i == 6 :
                    arr[9] += 1
                if i == 9 :
                    arr[6] += 1
            result += 1
        if tmp == 6 :
            arr[9] -= 1
        if tmp == 9 :
            arr[6] -= 1
        arr[tmp] -= 1
    print(result)
    return

main()

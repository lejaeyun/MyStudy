#https://www.acmicpc.net/problem/5397
import sys
input = sys.stdin.readline

def main() :
    for _ in range(int(input())) :
        arr = []
        idx = 0
        s = str(input().split()[0])
        for i in s :
            if i == "<" :
                if idx != 0 :
                    idx = idx - 1
            elif i == ">" :
                if idx != len(arr) :
                    idx = idx + 1
            elif i == "-" :
                if len(arr) != 0 and idx != 0 :
                    arr.pop(idx - 1)
                    idx = idx - 1
            else :
                arr.insert(idx,i)
                idx = idx + 1
                
        for i in arr :
            print(i, end = "")
            
        print()
main()

#https://www.acmicpc.net/problem/1978
import sys
input = sys.stdin.readline

def main() :
    rec = list()
    for _ in range(3) :
        rec.append(list(map(int, input().split())))
    rec.sort()
    if rec[0][0] == rec[1][0] :
        if rec[0][1] == rec[2][1] :
            print(rec[2][0], rec[1][1])
        else :
            print(rec[2][0], rec[0][1])
    else :
        if rec[0][1] == rec[2][1] :
            print(rec[0][0], rec[1][1])
        else :
            print(rec[0][0], rec[2][1])
        
main()

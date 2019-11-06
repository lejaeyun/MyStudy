#https://www.acmicpc.net/problem/1978
import sys
input = sys.stdin.readline

def main() :
    x,y,w,h = map(int, input().split())
    chk = list()

    chk.append(h - y)
    chk.append(y)
    chk.append(w - x)
    chk.append(x)

    print(min(chk))
        
main()

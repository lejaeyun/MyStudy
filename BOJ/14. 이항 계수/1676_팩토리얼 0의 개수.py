#https://www.acmicpc.net/problem/1676
import sys
input = sys.stdin.readline
from math import factorial

def main() :
    
    denominator = 1
    for i in range(1, int(input())+1) :
        denominator = denominator * i
        
    chk = str(denominator)

    cnt = 0
    for i in range(len(chk)-1,-1,-1) :
        if chk[i] == "0" :
            cnt += 1
        else : break
    print(cnt)
    return 0;
        
main()

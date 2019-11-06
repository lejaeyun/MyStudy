#https://www.acmicpc.net/problem/1427
import sys
input = sys.stdin.readline

def main() :
    N = str(input().split()[0])
    num = []
    for i in N :
        num.append(int(i))
    num.sort()
    num.reverse()

    for i in num :
        print(i,end = "")
    return 0;
        
main()

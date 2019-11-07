#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    num = int(input())
    arr = list(map(int, input().split()))
    money = 0

    for i in range(num - 1, -1, -1) :
        for j in range(num) :
            print(i, j, int( (num + 1) / ((num - i)+1)))
        
main()

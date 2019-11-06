#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    side = list(map(int, input().split()))
    while (side[0] != 0 and side[1] != 0 and side[2] != 0) :
        z = side.pop(side.index(max(side)))
        x,y = side[0], side[1]
        if x**2 + y**2 == z**2 :
            print("right")
        else :
            print("wrong")
        side = list(map(int, input().split()))
        
main()

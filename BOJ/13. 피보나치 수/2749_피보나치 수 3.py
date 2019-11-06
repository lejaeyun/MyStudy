#https://www.acmicpc.net/problem/2749
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    Cycle = 1000000//10*15
    list = [0,1]
    for i in range(2,Cycle):
        list.append((list[i-1]+list[i-2])% 1000000)
    print(list[N%Cycle])

        
main()

#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dic = dict()
    for s in arr :
        dic[s] = 0
    for s in input().split()[0] :
        dic[s] += 1

    for s in arr :
        print(dic[s], end=" ")
    return 0;
        
main()

#https://www.acmicpc.net/problem/3052
import sys
input = sys.stdin.readline

def main() :
    result = list()
    for _ in range(10) :
        num = int(input())
        aa = num % 42
        if aa not in result :
            result.append(aa)
    print(len(result))
        
main()

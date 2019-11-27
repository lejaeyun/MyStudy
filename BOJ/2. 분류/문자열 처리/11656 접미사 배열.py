#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    string = input().rstrip()
    s = list()

    for i in range(len(string)) :
        s.append(string[i:])
    s.sort()

    for i in s :
        print(i)
    
    return 0;
        
main()

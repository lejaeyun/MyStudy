#https://www.acmicpc.net/problem/11051
import sys
input = sys.stdin.readline
from math import factorial

def main() :
    
    denominator = 1
    for i in range(1, int(input())+1) :
        denominator = denominator * i
        

    print(denominator)


    
    return 0;
        
main()

#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    m, n = map(int, input().split())
    result = ""
    while True :
        if m%n < 10 :
            result = str(m%n) + result
        else :
            if m%n == 10 :
                result = "A" + result
            elif m%n == 11 :
                result = "B" + result
            elif m%n == 12 :
                result = "C" + result
            elif m%n == 13 :
                result = "D" + result
            elif m%n == 14 :
                result = "E" + result
            elif m%n == 15 :
                result = "F" + result
                
        m = m // n
        if m == 0 :
            break
    print(result)
        
main()

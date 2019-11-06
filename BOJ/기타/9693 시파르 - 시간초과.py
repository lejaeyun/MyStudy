#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    n = 1
    case = 0
    while True :
        n = int(input())
        if n == 0 : break
        
        two, five = 0, 0
        for i in range(1, n + 1) :
            if i % 2 == 0 or i % 5 == 0 :
                nn = i
                while nn % 2 == 0 or nn % 5 == 0 :
                        
                    if nn % 2 == 0 :
                        nn = nn // 2
                        two += 1
                        
                    if nn % 5 == 0 :
                        nn = nn // 5
                        five += 1
        case += 1
        print("Case #" + str(case) + ": " + str(min(two,five)))        
main()

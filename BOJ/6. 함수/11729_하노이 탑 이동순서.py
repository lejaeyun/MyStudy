#https://www.acmicpc.net/problem/11729
import sys
input = sys.stdin.readline
result = list()
def hanoi(n,s = 1, c = 2, e = 3) :
    global result
    if n == 1 or n == 0 :
        result.append([s,e])
        return
    hanoi(n - 1 , s , e, c)
    result.append([s, e])
    hanoi(n - 1 , c, s , e)

def main() :
    global result
    hanoi(int(input()))
    print(len(result))
    for i,j in result :
        print(i,j)
    
    return
        
main()

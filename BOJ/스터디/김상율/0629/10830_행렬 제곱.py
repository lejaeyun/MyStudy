#https://www.acmicpc.net/problem/10830
import sys
input = sys.stdin.readline

def sqare(r,a,n) :
    tr = []
    for k in range(n) :
        tl = []
        for i in range(n) :
            temp = 0
            for j in range(n) :
                temp += r[k][j] * a[j][i]
            tl.append(temp%1000)
        tr.append(tl)
    return tr

def main() :
    N,B = map(int,input().split())
    A = [[] for _ in range(N)]
    for i in range(N) :
        A[i] = list(map(int,input().split()))

    for i in range(N):
        for j in range(N):
            A[i][j] = A[i][j] % 1000

    a = str(bin(B)).split("b")[1][::-1]

    t = A
    result = -1
    for i in a :
        if i == "1" :
            if result == -1 :
                result = t
            else :
                result = sqare(result, t, N)
        t = sqare(t,t,N)
        
    for u in result :
        for r in u :
            print(r,end = " ")
        print()
    
main()

#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def Matrix_Mul(arr1, arr2, M, N, B) :
    Matrix = [ [ 0 for _ in range(B)] for __ in range(M) ]
    
    for i in range(M) :
        for j in range(B) :
            tmp = 0
            for k in range(N) :
                tmp += arr1[i][k] * arr2[k][j]
            Matrix[i][j] = tmp
            
    return Matrix
            
    

def main() :
    M,N = map(int, input().split())
    arr1 = list()
    for _ in range(M) :
        arr1.append(list(map(int, input().split())))

    A,B = map(int, input().split())
    arr2 = list()
    for _ in range(A) :
        arr2.append(list(map(int, input().split())))

    C = Matrix_Mul(arr1, arr2, M, N, B)
    for l in C :
        for j in l :
            print(j, end = " ")
        print()
main()

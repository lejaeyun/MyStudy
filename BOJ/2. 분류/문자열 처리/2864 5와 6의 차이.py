#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    A,B = input().rstrip().split()
    five_a, five_b = 0,0
    six_a, six_b = 0,0
    
    for i in range(len(A)) :
        tmp = int(A[i])
        if tmp == 5 or tmp == 6 :
            five_a = five_a*10 + 5
            six_a = six_a*10 + 6
        else :
            five_a = five_a*10 + tmp
            six_a = six_a*10 + tmp
        
    for i in range(len(B)) :
        tmp = int(B[i])
        if tmp == 5 or tmp == 6 :
            five_b = five_b*10 + 5
            six_b = six_b*10 + 6
        else :
            five_b = five_b*10 + tmp
            six_b = six_b*10 + tmp
            
    A = [five_a, six_a]
    B = [five_b, six_b]
    result = []

    for i in range(2) :
        for j in range(2) :
            result.append(A[i] + B[j])

    print(min( result ), max( result ))
    
    return 0;
        
main()

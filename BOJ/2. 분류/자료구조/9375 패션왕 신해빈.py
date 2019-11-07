#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :

    for _ in range(int(input())) :
        fashon_arr = list()
        num_arr = list()
        for __ in range(int(input())) :
            Str = input().split()
            if Str[1] not in fashon_arr :
                fashon_arr.append(Str[1])
                num_arr.append(2)
            else :
                num_arr[fashon_arr.index(Str[1])] += 1
        result = 1
        for i in num_arr :
            result *= i
        print(result - 1)
        
main()

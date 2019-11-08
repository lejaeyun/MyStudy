#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    stair = list()
    for _ in range(int(input())) :
        stair.append(int(input()))

    stair_sum_1 = [0, 0]
    stair_sum_2 = [0, 0]
    for i in range(len(stair)) :
        try :
            s = stair_sum_1[-1]
            if stair_sum_1[-1]
            stair_sum_1.append( max(stair_sum_2[-1], ) + stair[i] )
        except :
            stair_sum_1.append(0)

        try :
            stair_sum_2.append( max(stair_sum_2[-1-2], stair_sum_1[-1-2]) + stair[i] )
            print(stair_sum_1 , stair_sum_2)
        except :
            stair_sum_2.append(0)

    print(max(stair_sum_1[-1] , stair_sum_2[-1]))
    print((stair_sum_1 , stair_sum_2))
    
    return 0;
        
main()

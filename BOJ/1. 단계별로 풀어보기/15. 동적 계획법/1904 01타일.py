#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    n = 1000000
    num = int(input()) - 1
    zero = [0, 1]
    one = [1, 1]
    result = [1,2]
    for i in range(2, n + 1) :
        z, o = (zero[i-2] + one[i-2]) % 15746, (zero[i-1] + one[i-1]) % 15746
        r = (z + o) % 15746
        zero.append(z)
        one.append(o)
        result.append(r)
        
    print(result[num])
    return 0;
        
main()

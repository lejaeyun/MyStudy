#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    arr = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white' ]
    
    
    ohm = dict()
    for i in range(len(arr)) :
        ohm[arr[i]] = [i, 10**i]

    result = ''
    for i in range(2) :
        color = input().rstrip()
        result += str(ohm[color][0])
        
    result = int(result)
    color = input().rstrip()
    result = result * ohm[color][1]
    
    print(result)
        
main()

#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    mydict = dict()
    
    for _ in range(int(input())) :
        Str = input().split()
        index = 0
        if Str[1] == "leave" :
            del mydict[Str[0]]
        else :
            mydict[Str[0]] = True
            
    arr = list(mydict.keys())
    arr.sort(reverse = True)
    for s in arr :
        if mydict[s] == True :
            print(s)
            
main()

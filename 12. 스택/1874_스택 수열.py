#https://www.acmicpc.net/problem/4949
import sys
input = sys.stdin.readline

def main() :

    chk = list()
    for _ in range(int(input())) :
        chk.append( int(input()) )
        
    cnt = 0
    pm = list()
    idx = 0
    for i in chk :
        while cnt < i :
            pm.append("+")
            cnt += 1
        if cnt == i :
            pm.append("-")
            idx = i
        if i < cnt :
            if i > idx :
                print("NO")
                return
            pm.append("-")
            idx = i
            
    for i in pm :
        print(i)
            
    
    return 0;
        
main()

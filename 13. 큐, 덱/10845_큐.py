#https://www.acmicpc.net/problem/11866
import sys
input = sys.stdin.readline

def main() :
    queue = list()
    
    for _ in range(int(input())) :
        a = str(input())
        a = a.rstrip('\n')
        if a.find("push") != -1 :
            queue.append(int(a.split()[1]))
        else :
            if a == "back" :
                if queue :
                    print(queue[-1])
                else :
                    print("-1")
            elif a == "front" :
                if queue :
                    print(queue[0])
                else :
                    print("-1")
            elif a == "size" :
                    print(len(queue))
            elif a == "pop" :
                if queue :
                    print(queue.pop(0))
                else :
                    print("-1")
            elif a == "empty" :
                if queue :
                    print("0")
                else :
                    print("1")
    
    return 0;
        
main()

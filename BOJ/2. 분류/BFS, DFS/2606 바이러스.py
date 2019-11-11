#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    computer_num = int(input())
    computer_arr = [[] for _ in range(computer_num + 1)]
    
    for _ in range(int(input())) :
        v,e = map(int, input().split())
        computer_arr[v].append(e)
        computer_arr[e].append(v)
    
    queue = list()
    visit = list()
    queue.append(1)
    while queue :
        nxt = queue.pop(0)
        if nxt not in visit :
            visit.append(nxt)
            queue.extend(computer_arr[nxt])
            
    print(len(visit) - 1)
        
main()

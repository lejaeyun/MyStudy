#https://www.acmicpc.net/problem/1991
import sys
input = sys.stdin.readline
import copy

def f(d) :
    queue = list()
    visit = list()
    queue.extend(["A"])
    result = ""
    
    while queue :
        nxt = queue.pop(0)
        if nxt == "." :
            continue
        if nxt not in visit :
            visit.append(nxt)
            queue = d[nxt] + queue
            result += nxt
    return result

def m(d) :
    queue = list()
    visit = list()
    queue.extend(["A"])
    result = ""
    d = copy.deepcopy(d)
    
    while queue :
        nxt = queue.pop()
        if nxt in visit :
            continue
        
        if nxt == "." :
            continue
        
        while True :
            if d[nxt][0] != "." :
                queue.append(nxt)
                nxt = d[nxt][0]
            else :
                if queue :
                    a = queue.pop()
                    if a != "." :
                        if a not in visit :
                            queue.append(a)
                        d[a][0] = "."
                visit.append(nxt)
                queue.extend(d[nxt])
                break
            
        queue.extend(d[nxt])
        result += nxt
        
    return result
    

def l(tree):
    stack = []
    result = ''
    stack.append("A")
    data = "A"
 
    while True:
        while tree[data][0] != '.':
            if tree[data][0] not in result:
                stack.append(tree[data][0])
                data = tree[data][0]
            else:
                break
 
        last_data = stack[-1]
 
        if tree[last_data][1] == '.':
            result += stack.pop()
 
            if stack:
                data = stack[-1]
            else:
                break
        else:

            if tree[data][1] not in result:
                stack.append(tree[data][1])
                data = tree[data][1]
            else:
                result += stack.pop()
                if 0 < len(stack):
                    data = stack[-1]
                else:
                    break
    return result

def main() :
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    tree = dict()
    N = int(input())
    for i in range(1,N+1) :
        t = list(map(str, input().split()))
        tree[t[0]] = [t[1],t[2]]
        
    print(f(tree))
    print(m(tree))
    print(l(tree))
        
    return 0;
        
main()

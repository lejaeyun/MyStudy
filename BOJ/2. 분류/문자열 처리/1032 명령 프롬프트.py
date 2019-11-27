#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    pattern = list()
    for _ in range(int(input())) :
        s = input().rstrip()
        if not pattern :
            for i in s :
                pattern.append(i)
        else :
            for i in range(len(s)) :
                if pattern[i] != "?" :
                    if pattern[i] != s[i] :
                        pattern[i] = "?"

    result = ""
    for i in pattern :
        result = result + i
    print(result)
        
    return 0;
        
main()

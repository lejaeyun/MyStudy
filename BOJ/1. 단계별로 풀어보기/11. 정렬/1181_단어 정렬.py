#https://www.acmicpc.net/problem/1181
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    word = []
    for _ in range(N) :
        s = str(input()).split()[0]
        word.append(s)

    word = list(set(word))
    for i in range(len(word)) :
        word[i] = [len(word[i]),word[i]]
    word.sort()
    for i in word :
        print(i[1])
    return 0;
        
main()

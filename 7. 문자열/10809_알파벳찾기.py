#https://www.acmicpc.net/problem/10809
import sys
input = sys.stdin.readline

def main() :
   
   alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   index = [-1 for _ in range(26)]
   s = str(input().split()[0])
   for i in range(len(s)) :
      if index[alpha.index(s[i])] == -1 :
         index[alpha.index(s[i])] = i
   for i in index :
      print(i, end = " ")
      
main()

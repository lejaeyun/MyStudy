#https://www.acmicpc.net/problem/1316
import sys
input = sys.stdin.readline

def main() :

   N = int(input())
   word = list()
   result = 0
   for _ in range(N) :
      word.append(str(input().split()[0]))

   for w in word :
      alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
      index = [-1 for _ in range(26)]
      nw = ""
      plus = True
      for j in w :
         if nw != j :
            if index[alpha.index(j)] == -1 :
               index[alpha.index(j)] = 0
            else :
               plus = False
               break
         nw = j
      if plus == True :
         result += 1
      
   print(result)
   
main()

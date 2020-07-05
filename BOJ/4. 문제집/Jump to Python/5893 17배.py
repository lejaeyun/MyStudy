import sys
input = sys.stdin.readline

n = list(str(input()).strip())
n.reverse()
num = 0
index = 1
for i in n :
    if int(i) == 1 :
        num = num + index
    index = index * 2
    
print(bin(num*17).split('b')[1])

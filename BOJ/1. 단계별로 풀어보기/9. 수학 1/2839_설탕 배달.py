a = int(input())
b = a // 5
c = 0
d = 0
Result = False
for i in range(0,b+1) :
    c = a - ((b - i)*5)
    if c%3 == 0 :
        d = c//3
        b = b - i
        Result = True
        break
if Result == True :
    print(b+d)
else : print(-1)

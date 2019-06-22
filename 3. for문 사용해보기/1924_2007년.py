a = [31,28,31,30,31,30,31,31,30,31,30,31]
c = input().split()
b = 0
for i in range(int(c[0])-1) :
    b += a[i]
d = (b +int(c[1]) - 1 ) % 7
if d == 0 :
    print("MON")
elif d == 1 :
    print("TUE")
elif d == 2 :
    print("WED")
elif d == 3 :
    print("THU")
elif d == 4 :
    print("FRI")
elif d == 5 :
    print("SAT")
elif d == 6 :
    print("SUN")

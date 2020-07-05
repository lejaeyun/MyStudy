#14
def T(n) :
    if n == 1 :
        return 1
    return 7*T(n//5)+10*n

print(T(625))

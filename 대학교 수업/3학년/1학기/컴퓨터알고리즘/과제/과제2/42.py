#42
import numpy
# n 은 2의 제곱수, empty는 트로미노가 빈 좌표 (L자 모형이라 defalt = 1로 둔다.)
count = 1
def tromino(n, array, empty = 1) :
    global count
    # n이 2일 때 타일링
    if n == 2 :
        if empty != 0 :
            array[0][0] = count
        if empty != 1 :
            array[0][1] = count
        if empty != 2 :
            array[1][0] = count
        if empty != 3 :
            array[1][1] = count
        count = count + 1
    else :
        # 중앙의 empty 부분이 빈 사각형 모양
        tromino(n//2,array[n//4:(n//4)*3, n//4:(n//4)*3], empty) 
        if empty != 0 :
            tromino(n//2,array[0:n//2, 0:n//2], 3) # 오른쪽 아래가 빈 사각형 모양
        if empty != 1 :
            tromino(n//2,array[:n//2, n//2:], 2) # 왼쪽 아래가 빈 사각형 모양
        if empty != 2 :
            tromino(n//2,array[n//2: , 0:n//2], 1) # 오른쪽 위가 빈 사각형 모양
        if empty != 3 :
            tromino(n//2,array[n//2:, n//2:], 0) # 왼쪽 위가 빈 사각형 모양

m = 8
array = numpy.array([[0]*m for _ in range(m)])
tromino(m, array,1)
for arr in array :
    for i in arr :
        print("%3d"%i, end = " ")
    print()

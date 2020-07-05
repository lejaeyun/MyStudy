import sys
import time

# x1 < x2, y1 < y2
# 겹치는 부분을 반환한다. ( 대각선 두 점 )
def FindPoints(rec1, rec2): 
    x1, y1, x2, y2 = rec1
    x3, y3, x4, y4 = rec2
    
    intersecting_rec_x1 = max(x1, x3) 
    intersecting_rec_y1 = max(y1, y3) 
  
    intersecting_rec_x2 = min(x2, x4) 
    intersecting_rec_y2 = min(y2, y4) 
    
    # 겹치지 않는다면 return False
    if (intersecting_rec_x1 >= intersecting_rec_x2 or intersecting_rec_y1 >= intersecting_rec_y2) : 
        return False
    
    # 겹치는 부분이 있다면 list로 변환하여 반환
    rec3 = [intersecting_rec_x1, intersecting_rec_y1, intersecting_rec_x2, intersecting_rec_y2]
    return rec3

# FindPoints 를 이용하여 겹치는 사각형을 반환한다
# 브루트포스
def find_intersecting_rectangle_area(Rectangle_list) :
    
    intersecting_rectangle = list()
    
    # 사각형이 겹치는지 확인하여 겹친다면 리스트에 삽입한다.
    for i in range(len(Rectangle_list)) :
        for j in range(i+1, len(Rectangle_list)) :
            result = FindPoints(Rectangle_list[i], Rectangle_list[j])
            
            if result != False and result not in intersecting_rectangle :
                intersecting_rectangle.append(result)
    
    return intersecting_rectangle

# find_intersecting_rectangle_area을 이용하여
# 모든 사각형의 겹치는 부분을 반환한다
def check_intersecting_rectangle_area(Rectangle_list) :
    
    intersecting_rectangle = find_intersecting_rectangle_area(Rectangle_list)
    result_area = rec_area(intersecting_rectangle)
    
    # 중복되어 겹치는 부분을 제거한다.
    # 중복되는 부분이 없을 때 까지 반복
    while intersecting_rectangle :
        intersecting_rectangle = find_intersecting_rectangle_area(intersecting_rectangle)
        result_area = result_area - rec_area(intersecting_rectangle)
    
    return result_area

# 리스트 내 모든 사각형의 넓이를 반환
def rec_area(rec_list) :
    area = 0
    for x1,y1,x2,y2 in rec_list :
        area = area + abs(x1-x2) * abs(y1-y2)
    return area

# x1 < x2, y1 < y2
# list를 정렬하여 list로 반환
def sort_rectangle(tmplist) :
    x1, y1, x2, y2 = tmplist
    
    x1, x2 = min(x1,x2), max(x1,x2)
    y1, y2 = min(y1,y2), max(y1,y2)
    rec = [x1, y1, x2, y2]
    return rec
  
def main():
    
    if len(sys.argv) != 2 :
        print("Usage : PA04.py [INPUT FILE]")
        return
    
    start = time.time()

    Rectangle_list = list()
    filename = sys.argv[1].rstrip()
    with open(filename,'r') as f :
        for l in f.readlines() :
            tmplist = list(map(int, l.split()))
            if len(tmplist) > 1 :
                Rectangle_list.append(sort_rectangle(tmplist))
                
    
    area = check_intersecting_rectangle_area(Rectangle_list)
    end = time.time() - start
    with open("output.txt",'w+') as f :
        f.write("Intersection Area : " + str(area) + "\n")
        f.write("Elapsed time : " + str(end))
    
    print("Intersection Area : " + str(area))
    print("Elapsed time : " + str(end))
            
main()

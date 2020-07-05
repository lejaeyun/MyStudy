
# From Stackoverflow Alex Martelli
# Distance Between Two Segments
# 두 선분 사이의 최단거리 알고리즘

import copy
import sys
import math


class Point(object):
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class LineSegment(object):
    def __init__(self, p1, p2):
        assert isinstance(p1, Point), \
            "p1 is not of type Point, but of %r" % type(p1)
        assert isinstance(p2, Point), \
            "p2 is not of type Point, but of %r" % type(p2)
        self.p1 = p1
        self.p2 = p2

def side(a,b,c):
    d = (c.y-a.y)*(b.x-a.x) - (b.y-a.y)*(c.x-a.x)
    return 1 if d > 0 else (-1 if d < 0 else 0)

def is_point_in_closed_segment(a, b, c):
    if a.x < b.x:
        return a.x <= c.x and c.x <= b.x
    if b.x < a.x:
        return b.x <= c.x and c.x <= a.x

    if a.y < b.y:
        return a.y <= c.y and c.y <= b.y
    if b.y < a.y:
        return b.y <= c.y and c.y <= a.y

    return a.x == c.x and a.y == c.y

def segments_intersect(segment1, segment2):
    a, b = segment1.p1, segment1.p2
    c, d = segment2.p1, segment2.p2
    if a == b:
        return a == c or a == d
    if c == d:
        return c == a or c == b

    s1 = side(a,b,c)
    s2 = side(a,b,d)

    if s1 == 0 and s2 == 0:
        return \
            is_point_in_closed_segment(a, b, c) or is_point_in_closed_segment(a, b, d) or \
            is_point_in_closed_segment(c, d, a) or is_point_in_closed_segment(c, d, b)

    if s1 and s1 == s2:
        return False

    s1 = side(c,d,a)
    s2 = side(c,d,b)

    if s1 and s1 == s2:
        return False

    return True

def segments_distance(segment1, segment2):
    if segments_intersect(segment1, segment2):
        return 0

    distances = []
    distances.append(point_segment_distance(segment1.p1, segment2))
    distances.append(point_segment_distance(segment1.p2, segment2))
    distances.append(point_segment_distance(segment2.p1, segment1))
    distances.append(point_segment_distance(segment2.p2, segment1))
    return min(distances)

def point_segment_distance(point, segment):    
    dx = segment.p2.x - segment.p1.x
    dy = segment.p2.y - segment.p1.y
    if dx == dy == 0:  # the segment's just a point
        return math.hypot(point.x - segment.p1.x, point.y - segment.p1.y)

    if dx == 0:
        if (point.y <= segment.p1.y or point.y <= segment.p2.y) and \
           (point.y >= segment.p2.y or point.y >= segment.p2.y):
            return abs(point.x - segment.p1.x)

    if dy == 0:
        if (point.x <= segment.p1.x or point.x <= segment.p2.x) and \
           (point.x >= segment.p2.x or point.x >= segment.p2.x):
            return abs(point.y - segment.p1.y)


    t = ((point.x - segment.p1.x) * dx + (point.y - segment.p1.y) * dy) / \
        (dx * dx + dy * dy)

    if t < 0:
        dx = point.x - segment.p1.x
        dy = point.y - segment.p1.y
    elif t > 1:
        dx = point.x - segment.p2.x
        dy = point.y - segment.p2.y
    else:
        near_x = segment.p1.x + t * dx
        near_y = segment.p1.y + t * dy
        dx = point.x - near_x
        dy = point.y - near_y

    return math.hypot(dx, dy)


# closet pair algoritms

from math import sqrt, pow
import sys
INF = sys.maxsize

def distance(a, b):
    global Segments
    # 두 점이 같은 선분 내일 때 INF 반환
    for i in Segments :
        if a in i :
            if b in i :
                return INF
    
    return sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1],2))

def bruteMin(points, current=INF):
    if len(points) < 2: return current
    else:
        head = points[0]
        del points[0]
        newMin = min([distance(head, x) for x in points])
        newCurrent = min([newMin, current])
        return bruteMin(points, newCurrent)

def divideMin(points):
    half = len(sorted(points))//2
    minimum = min([bruteMin(points[:half]), bruteMin(points[half:])])
    nearLines = filter(lambda x: x[0] > half - minimum and x[0] < half + minimum, points)
    nearLine = list()
    for l in nearLines :
        nearLine.append(l)
    return min([bruteMin(nearLine), minimum])


# Main

Segments = list()

def main() :
    
    if len(sys.argv) != 2 :
        print("Usage : PA01-1.py [INPUT FILE]")
        return
    
    inputFilename = sys.argv[1]

    global Segments
    line_segments = list()
    points = list()
    del_array = list()
    Distance = list()
    
    # 파일을 읽어 배열에 저장
    with open(inputFilename, "r") as f :
        tmpList = f.readlines()
        for b in tmpList :
            tmpSegment = list(map(int, b.rstrip().split()))
            if tmpSegment[0] == -1 :
                break
            
            if len(tmpSegment) != 1 : # 처음 개수, -1 제외
                point1 = Point(tmpSegment[0], tmpSegment[1])
                point2 = Point(tmpSegment[2], tmpSegment[3])
                line_segments.append(LineSegment(point1, point2))
                
                # 교차점 있는 선분 확인.
                # 교차점이 있는 선분 확인
                # O(n^2)  -> 파일 for list,  순회 for   n*n
                for i in range(0, len(line_segments)-1) :
                    if segments_intersect( line_segments[i], line_segments[-1] ) :
                        del_array.extend([line_segments[i],line_segments[len(line_segments)-1]])

    # 교차점이 있는 선분 제거
    del_array = set (del_array)
    line_segments = list(set(line_segments) - del_array)

    # 교차점을 모두 제거한 이후 선분이 1개 이하일 때 거리 0을 출력후 리턴.
    if len(line_segments) <= 1 :
        print("0")
        print("Line Segments Less than 2")
        return

    # Closest point 알고리즘을 위해 선분 점들을 배열에 저장
    for i in range(len(line_segments)) :
        l = line_segments[i]
        p1 = (l.p1.x, l.p1.y)
        p2 = (l.p2.x, l.p2.y)
        points.append(p1)
        points.append(p2)
        Segments.append([p1, p2])
        # 모든 선분의 거리를 배열에 추가
        for j in range(i+1, len(line_segments)) :
            Distance.append( segments_distance(line_segments[i], line_segments[j]) )

    # Closest pair 거리 추가
    Distance.append(divideMin(points))
    points.sort()
    outputFilename = "PA01-1.out"
    with open(outputFilename, "w+") as f :
        f.write(str(min(Distance))+"\n")


main()





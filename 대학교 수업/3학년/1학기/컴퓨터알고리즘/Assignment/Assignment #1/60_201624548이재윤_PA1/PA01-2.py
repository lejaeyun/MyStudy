import sys

def skyline(buildingList) :
    
    # empty
    if not buildingList : 
        return list()

    if len(buildingList) == 1 :
        return [[buildingList[0][0], buildingList[0][1]], [buildingList[0][2] , 0]]
    
    count = len(buildingList)
    
    mid = count // 2
    left = skyline(buildingList[:mid])
    right = skyline(buildingList[mid:])
    
    return merge_sort(left, right)

def merge_sort(left, right) :
    i,j = 0,0
    leftMaxHeight,rightMaxHeight = 0,0
    result = list()
    while i < len(left) and j < len(right) :
        if left[i][0] < right[j][0]:
            leftMaxHeight = left[i][1]
            point = left[i][0]
            i += 1
        elif right[j][0] < left[i][0]:
            rightMaxHeight = right[j][1]
            point = right[j][0]
            j += 1
        else:
            leftMaxHeight = left[i][1]
            rightMaxHeight = right[j][1]
            
            # 오른쪽 꼭짓점이 추가되는 튜플의 기준
            point = right[j][0]
            i += 1
            j += 1
        
        if valid_check(result, max(leftMaxHeight, rightMaxHeight)) :
            result.append([point, max(leftMaxHeight, rightMaxHeight)])
            
    # 사용되지 않은 인자 Merge
    result.extend(right[j:])
    result.extend(left[i:])
    
    return result

def valid_check(tmpList, height):
     return not tmpList or tmpList[-1][1] != height

def main() :
    if len(sys.argv) != 2 :
        print("Usage : PA01-2.py [INPUT FILE]")
        return

    inputFilename = sys.argv[1]
    
    buildings = list()
    
    with open(inputFilename, "r") as f :
        tmpList = f.readlines()
        for b in tmpList :
            tmpBuilding = list(map(int, b.rstrip().split()))
            if len(tmpBuilding) != 1 : # 처음 개수, -1 제외
                buildings.append(tmpBuilding)

    result = skyline(buildings)
    outputFilename = "PA01-2.out"
    with open(outputFilename, "w+") as f :
        for b in result :
            f.write(str(b[0]) + ", " + str(b[1]) + "\n")

    print("Success!!")

main()
